"""Looping animation: swaying tree shadows on the background + live phone UI.
Renders at source resolution (892x1124) and downsamples to 446x562.
Frame N is an exact copy of frame 0."""
import sys, subprocess, math
import numpy as np, cv2
from PIL import Image

SRC, OUT = sys.argv[1], sys.argv[2]
W, H = 446, 562
FPS, DUR = 60, 8.0
N = int(FPS * DUR)

img = np.asarray(Image.open(SRC).convert("RGB")).astype(np.float32) / 255.0
SH, SW = img.shape[:2]
yy, xx = np.mgrid[0:SH, 0:SW].astype(np.float32)

def sstep(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
def ease(x): x = min(max(x, 0.0), 1.0); return x * x * (3 - 2 * x)
def window(t, a, b):
    if t <= a or t >= b: return 0.0
    return math.sin(math.pi * (t - a) / (b - a)) ** 2

# ---------------- phone mask (rounded rect of the phone body) ----------------
phone = np.zeros((SH, SW), np.uint8)
x0, y0, x1, y1, rad = 163, 236, 727, SH + 200, 88
cv2.rectangle(phone, (x0 + rad, y0), (x1 - rad, y1), 1, -1)
cv2.rectangle(phone, (x0, y0 + rad), (x1, y1), 1, -1)
for cx in (x0 + rad, x1 - rad): cv2.circle(phone, (cx, y0 + rad), rad, 1, -1)
dist_out = cv2.distanceTransform((1 - phone).astype(np.uint8), cv2.DIST_L2, 5)
bg = (1 - phone).astype(np.float32)
phone_soft = cv2.GaussianBlur(phone.astype(np.float32), (0, 0), 1.5)

# ---------------- tree shadow model ----------------
# Low-frequency luminance (normalized convolution over background only) = light/shadow map.
luma = img @ np.array([0.299, 0.587, 0.114], np.float32)
SIG = 14
num = cv2.GaussianBlur(luma * bg, (0, 0), SIG)
den = cv2.GaussianBlur(bg, (0, 0), SIG)
light = num / np.maximum(den, 1e-4)
# fill phone area for sampling with a much wider blur
num2 = cv2.GaussianBlur(luma * bg, (0, 0), 60); den2 = cv2.GaussianBlur(bg, (0, 0), 60)
light = np.where(den > 0.15, light, num2 / np.maximum(den2, 1e-4)).astype(np.float32)
# keep the phone's own drop shadow still: no displacement close to the phone
sway_amp = sstep((dist_out - 20) / 60.0) * bg

def shadow_frame(f, t):
    p = 2 * math.pi * t
    ph1 = 0.006 * xx + 0.004 * yy
    ph2 = 0.003 * xx - 0.007 * yy + 1.3
    # branch sway (1 cycle) + leaf flutter (2 & 3 cycles) — all whole cycles, so it loops
    dx = 16 * np.sin(p + ph1) * 0.7 + 5 * np.sin(2 * p + ph2) + 2.5 * np.sin(3 * p + 2 * ph1)
    dy = 9 * np.sin(p + ph1 + 0.8) * 0.7 + 4 * np.sin(2 * p + ph2 + 0.5)
    # remove the t=0 offset so frame 0 equals the original exactly
    dx0 = 16 * np.sin(ph1) * 0.7 + 5 * np.sin(ph2) + 2.5 * np.sin(2 * ph1)
    dy0 = 9 * np.sin(ph1 + 0.8) * 0.7 + 4 * np.sin(ph2 + 0.5)
    mx = (xx + (dx - dx0) * sway_amp).astype(np.float32)
    my = (yy + (dy - dy0) * sway_amp).astype(np.float32)
    lw = cv2.remap(light, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    # light flicker through leaves: brighten lit areas slightly in a slow loop
    ratio = np.clip(lw / np.maximum(light, 1e-3), 0.35, 2.8)
    ratio = 1 + (ratio - 1) * bg
    return f * ratio[..., None]

# ---------------- UI geometry (source px) ----------------
BAR_Y0, BAR_Y1 = 646, 655
BAR_FILL_X0, BAR_FILL_X1, BAR_TARGET = 226, 264, 380
ORANGE = np.array([242, 155, 61], np.float32) / 255
BIG_PIN = (384, 646)
LOC_PIN = (321, 800)
HOUSE = (582, 790)
BELL_DOT = (662, 345)
ROUTE = np.array([(347, 797), (362, 786), (378, 775), (400, 762), (430, 749), (470, 741),
                  (520, 740), (527, 726), (528, 713), (545, 712), (558, 720), (570, 731),
                  (580, 748), (586, 766), (589, 784)], np.float32)
seg = np.linalg.norm(np.diff(ROUTE, axis=0), axis=1); cum = np.concatenate([[0], np.cumsum(seg)])

def route_point(u):
    d = u * cum[-1]; i = min(np.searchsorted(cum, d) - 1, len(seg) - 1); i = max(i, 0)
    a = (d - cum[i]) / seg[i]; return ROUTE[i] * (1 - a) + ROUTE[i + 1] * a, i

SS = 4  # sub-pixel precision for cv2 drawing
def P(p): return (int(round(p[0] * SS)), int(round(p[1] * SS)))

def layer():
    return np.zeros((SH, SW, 3), np.float32), np.zeros((SH, SW), np.float32)

def over(f, col, a):
    return f * (1 - a[..., None]) + col * a[..., None]

# wave emoji patch
EX0, EY0, EX1, EY1 = 420, 330, 458, 368
patch = img[EY0:EY1, EX0:EX1].copy()
bgcol = np.median(np.concatenate([patch[0], patch[-1], patch[:, 0], patch[:, -1]]), axis=0)
emask = sstep((np.linalg.norm(patch - bgcol, axis=2) - 0.06) / 0.12)
emask = cv2.GaussianBlur(emask, (0, 0), 0.6)
PIVOT = (430 - EX0 + 0.0, 362 - EY0 + 0.0)   # wrist, bottom-left

def ring(f, c, r, a, col, width=2.2):
    d = np.sqrt((xx - c[0]) ** 2 + (yy - c[1]) ** 2)
    m = np.exp(-((d - r) / width) ** 2) * a
    return over(f, col, m)

def ui_frame(f, t):
    # --- waving hand (two waves near the start, one near the middle) ---
    ang = 16 * (math.sin(2 * math.pi * 3 * (t - 0.04) / 0.3) * window(t, 0.04, 0.34)
                + math.sin(2 * math.pi * 2 * (t - 0.50) / 0.2) * window(t, 0.50, 0.70))
    if abs(ang) > 1e-3:
        M = cv2.getRotationMatrix2D(PIVOT, ang, 1.0)
        rp = cv2.warpAffine(patch, M, patch.shape[1::-1], flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        rm = cv2.warpAffine(emask, M, patch.shape[1::-1], flags=cv2.INTER_LINEAR)
        region = f[EY0:EY1, EX0:EX1]
        clean = region * (1 - emask[..., None]) + bgcol * emask[..., None]
        f[EY0:EY1, EX0:EX1] = clean * (1 - rm[..., None]) + rp * rm[..., None]

    # --- journey: progress bar fills to the next stop while a rider moves along the map route ---
    prog = ease((t - 0.14) / 0.42)
    fade = 1 - ease((t - 0.84) / 0.13)
    vis = fade * ease((t - 0.08) / 0.06)
    if vis > 0:
        # progress bar extension
        xend = BAR_FILL_X1 + (BAR_TARGET - BAR_FILL_X1) * prog
        if xend > BAR_FILL_X1 + 0.3:
            m = np.zeros((SH * 1, SW), np.float32)
            cv2.line(m, P((BAR_FILL_X1 - 4, 650.5)), P((xend, 650.5)), 1.0, 9, cv2.LINE_AA, shift=2)
            m = cv2.GaussianBlur(m, (0, 0), 0.5) * fade
            f = over(f, ORANGE, np.clip(m, 0, 1))
            # glowing head
            g = np.exp(-((xx - xend) ** 2 + (yy - 650.5) ** 2) / (2 * 7.0 ** 2)) * 0.5 * fade * (1 - 0.6 * ease((t - 0.56) / 0.1))
            f = f + g[..., None] * np.array([1.0, 0.75, 0.4], np.float32)
        # travelled route in orange
        pt, idx = route_point(prog)
        if prog > 0.002:
            pts = np.vstack([ROUTE[:idx + 1], pt[None]])
            m = np.zeros((SH, SW), np.float32)
            cv2.polylines(m, [(pts * SS).round().astype(np.int32)], False, 1.0, 4, cv2.LINE_AA, shift=2)
            m = cv2.GaussianBlur(m, (0, 0), 0.6)
            f = over(f, ORANGE, m * 0.9 * fade)
        # rider dot: soft shadow, white ring, orange core
        sh = np.exp(-((xx - pt[0]) ** 2 + (yy - pt[1] - 2) ** 2) / (2 * 6.0 ** 2)) * 0.35 * vis
        f = f * (1 - sh[..., None])
        d = np.sqrt((xx - pt[0]) ** 2 + (yy - pt[1]) ** 2)
        f = over(f, np.ones(3, np.float32), sstep((8.5 - d) / 1.2) * vis)
        f = over(f, ORANGE * 0.95, sstep((5.5 - d) / 1.2) * vis)
        # pulse halo while moving
        if 0.12 < t < 0.58:
            u = ((t - 0.12) * 4) % 1.0
            f = ring(f, pt, 9 + 14 * u, (1 - u) * 0.55 * vis, ORANGE)

    # start pin pulse (before departure)
    for s in (0.0, 0.07):
        w = window(t, s, s + 0.14)
        if w > 0:
            u = (t - s) / 0.14
            f = ring(f, LOC_PIN, 6 + 22 * u, (1 - u) * 0.8 * min(1, 4 * u), ORANGE)
    # arrival: house + next-stop pin ripple
    for s in (0.56, 0.63):
        w = window(t, s, s + 0.16)
        if w > 0:
            u = (t - s) / 0.16
            a = (1 - u) * 0.8 * min(1, 4 * u)
            f = ring(f, HOUSE, 10 + 24 * u, a, ORANGE)
            f = ring(f, BIG_PIN, 4 + 18 * u, a * 0.9, np.array([0.86, 0.12, 0.12], np.float32), 1.8)

    # notification bell ripple
    for s in (0.70, 0.77):
        w = window(t, s, s + 0.15)
        if w > 0:
            u = (t - s) / 0.15
            f = ring(f, BELL_DOT, 4 + 20 * u, (1 - u) * 0.85 * min(1, 4 * u), np.array([0.9, 0.16, 0.13], np.float32), 1.8)
    return f

def glass_glint(f, t):
    w = window(t, 0.86, 0.995)
    if w <= 0: return f
    u = (t - 0.86) / 0.135
    d = xx * 0.75 + yy * 0.66
    pos = 200 + u * 1300
    band = np.exp(-((d - pos) / 80.0) ** 2) * 0.10 + np.exp(-((d - pos + 150) / 28.0) ** 2) * 0.05
    L = (band * phone_soft * w)[..., None]
    return 1 - (1 - f) * (1 - L)

ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb48le",
                       "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "ffv1", "-pix_fmt", "rgb48le", OUT],
                      stdin=subprocess.PIPE)

def render(t):
    f = shadow_frame(img.copy(), t)
    f = ui_frame(f, t)
    f = glass_glint(f, t)
    fr = cv2.resize(np.clip(f, 0, 1), (W, H), interpolation=cv2.INTER_AREA)
    return (np.clip(fr, 0, 1) * 65535 + 0.5).astype(np.uint16)

if __name__ == "__main__" and OUT != "PREVIEW":
    first = None
    for i in range(N + 1):
        out = first if i == N else render(i / N)
        if i == 0: first = out
        ff.stdin.write(out.tobytes())
        if i % 60 == 0: print("frame", i, flush=True)
    ff.stdin.close(); ff.wait(); print("done")
