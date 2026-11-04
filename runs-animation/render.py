import sys, subprocess, math
import numpy as np, cv2
from PIL import Image

SRC = sys.argv[1]
OUT = sys.argv[2]            # lossless intermediate .mkv
W, H = 1376, 773
FPS, DUR = 60, 8.0
N = int(FPS * DUR)           # frames 0..N inclusive; frame N == frame 0

img = np.asarray(Image.open(SRC).convert("RGB")).astype(np.float32) / 255.0
SH, SW = img.shape[:2]
yy, xx = np.mgrid[0:SH, 0:SW].astype(np.float32)

def smooth(x):
    x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)

def window(t, a, b):
    """0 outside [a,b], smooth bell inside."""
    if t <= a or t >= b: return 0.0
    u = (t - a) / (b - a); return math.sin(math.pi * u) ** 2

def poly_mask(pts, blur):
    m = np.zeros((SH, SW), np.float32)
    cv2.fillPoly(m, [np.array(pts, np.int32)], 1.0)
    return cv2.GaussianBlur(m, (0, 0), blur)

luma = img @ np.array([0.299, 0.587, 0.114], np.float32)

# --- masks (source pixel space) ---
phone = poly_mask([(905, 112), (1300, 190), (1085, 1020), (735, 955)], 6)
btn_region = poly_mask([(858, 430), (1200, 488), (1195, 545), (852, 486)], 2)
r, g, b = img[..., 0], img[..., 1], img[..., 2]
orange = ((r > 0.75) & (g > 0.45) & (g < 0.78) & (b < 0.45)).astype(np.float32) * btn_region
orange = cv2.GaussianBlur(orange, (0, 0), 1.0)
btn_glow = cv2.GaussianBlur(cv2.dilate(orange, np.ones((9, 9), np.uint8)), (0, 0), 18)
btn_glow = btn_glow / btn_glow.max() * (1 - btn_region * 0.85)

head_box = np.zeros((SH, SW), np.float32); head_box[80:145, 70:650] = 1
head_text = smooth((luma - 0.6) / 0.3) * head_box
bullet_box = np.zeros((SH, SW), np.float32); bullet_box[160:275, 100:460] = 1
bullet_text = smooth((luma - 0.55) / 0.3) * bullet_box
checks = [(119, 180), (119, 218), (119, 257)]

BELL = (1246, 244)  # notification dot

def gauss_spot(cx, cy, s):
    return np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * s * s))

def compose(t):
    f = img.copy()

    # 1. warm sunlight breathing in from the window (upper-left), screen blend
    sun_amt = 0.10 * math.sin(math.pi * t) ** 2
    if sun_amt > 0:
        ang = -0.55
        d = (xx * math.cos(ang) + yy * math.sin(ang))           # diagonal coordinate
        pos = -200 + 2600 * t
        band = np.exp(-((d - pos) / 520.0) ** 2) * 0.6 + np.exp(-((xx + 300) ** 2 + (yy + 200) ** 2) / (2 * 900.0 ** 2))
        warm = np.array([1.0, 0.82, 0.55], np.float32)
        L = (band * sun_amt)[..., None] * warm
        f = 1 - (1 - f) * (1 - L)

    # 2. headline shimmer
    w = window(t, 0.06, 0.30)
    if w > 0:
        pos = 40 + (t - 0.06) / 0.24 * 720
        s = np.exp(-(((xx + 0.35 * yy) - pos - 40) / 45.0) ** 2) * head_text * w
        f = f + s[..., None] * np.array([0.55, 0.45, 0.3], np.float32)

    # 3. checklist: each item glows in sequence
    for i, (cx, cy) in enumerate(checks):
        w = window(t, 0.16 + i * 0.06, 0.34 + i * 0.06)
        if w > 0:
            glow = gauss_spot(cx, cy, 14) * 0.45 * w
            row = np.zeros_like(bullet_text); row[cy - 18:cy + 18, :] = 1
            f = f + glow[..., None] * np.array([1.0, 0.62, 0.25], np.float32)
            f = f + (bullet_text * row * 0.18 * w)[..., None]

    # 4. notification bell ripple (two rings)
    for start in (0.30, 0.38):
        w = window(t, start, start + 0.16)
        if w > 0:
            u = (t - start) / 0.16
            rad = 6 + 34 * u
            dist = np.sqrt((xx - BELL[0]) ** 2 + (yy - BELL[1]) ** 2)
            ring = np.exp(-((dist - rad) / 2.2) ** 2) * (1 - u) * 0.9
            f = f * (1 - ring[..., None]) + ring[..., None] * np.array([1.0, 0.35, 0.3], np.float32)

    # 5. glass glint sweeping across the phone screen
    w = window(t, 0.42, 0.64)
    if w > 0:
        u = (t - 0.42) / 0.22
        d = xx * 0.8 + yy * 0.6
        pos = 900 + u * 1150
        band = np.exp(-((d - pos) / 70.0) ** 2) * 0.24 + np.exp(-((d - pos + 160) / 30.0) ** 2) * 0.10
        L = (band * phone * w)[..., None]
        f = 1 - (1 - f) * (1 - L)

    # 6. "Start Run" button pulse (two heartbeats)
    p = window(t, 0.62, 0.74) + window(t, 0.72, 0.86)
    if p > 0:
        f = f + (orange * 0.16 * p)[..., None] * np.array([1.0, 0.9, 0.7], np.float32)
        f = 1 - (1 - f) * (1 - (btn_glow * 0.38 * p)[..., None] * np.array([1.0, 0.6, 0.2], np.float32))

    return np.clip(f, 0, 1)

def camera(f, t):
    # slow push-in toward the phone and back, with gentle handheld float
    e = math.sin(math.pi * t) ** 2
    s = 1.0 + 0.045 * e
    cx, cy = 880, 560
    dx = 10 * math.sin(2 * math.pi * t) * e
    dy = -8 * math.sin(4 * math.pi * t) * e
    rot = 0.35 * math.sin(2 * math.pi * t) * e
    M = cv2.getRotationMatrix2D((cx, cy), rot, s)
    M[0, 2] += dx; M[1, 2] += dy
    return cv2.warpAffine(f, M, (SW, SH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)

ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb48le",
                       "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "ffv1", "-pix_fmt", "rgb48le", OUT],
                      stdin=subprocess.PIPE)
first = None
for i in range(N + 1):
    if i == N:
        out = first
    else:
        t = i / N
        fr = camera(compose(t), t)
        fr = cv2.resize(fr, (W, H), interpolation=cv2.INTER_AREA)
        out = (np.clip(fr, 0, 1) * 65535 + 0.5).astype(np.uint16)
        if i == 0: first = out
    ff.stdin.write(out.tobytes())
    if i % 60 == 0: print("frame", i, flush=True)
ff.stdin.close(); ff.wait()
print("done")
