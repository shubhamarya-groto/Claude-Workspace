/* GFB Testimonials: arrows, dashes and keyboard for the scroll-snap track.
   Without this script the slides still swipe/scroll; it only adds the controls. */
(function () {
  document.querySelectorAll('.gfb-tst').forEach(function (root) {
    if (root.dataset.gfbTstReady) return;
    root.dataset.gfbTstReady = '1';

    var track = root.querySelector('[data-gfb-tst-track]');
    if (!track) return;
    var slides = track.children;
    var dots = root.querySelectorAll('[data-gfb-tst-dot]');
    var prev = root.querySelector('[data-gfb-tst-prev]');
    var next = root.querySelector('[data-gfb-tst-next]');
    var current = 0;

    function go(i) {
      i = Math.max(0, Math.min(slides.length - 1, i));
      track.scrollTo({ left: slides[i].offsetLeft - track.offsetLeft, behavior: 'smooth' });
    }

    function update() {
      var i = Math.round(track.scrollLeft / track.clientWidth);
      if (i === current && root.dataset.gfbTstInit) return;
      root.dataset.gfbTstInit = '1';
      current = i;
      dots.forEach(function (d, n) { d.setAttribute('aria-selected', n === i ? 'true' : 'false'); });
      if (prev) prev.disabled = i === 0;
      if (next) next.disabled = i === slides.length - 1;
    }

    if (prev) prev.addEventListener('click', function () { go(current - 1); });
    if (next) next.addEventListener('click', function () { go(current + 1); });
    dots.forEach(function (d) {
      d.addEventListener('click', function () { go(parseInt(d.getAttribute('data-gfb-tst-dot'), 10)); });
    });
    track.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); go(current + 1); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); go(current - 1); }
    });

    var t;
    track.addEventListener('scroll', function () { clearTimeout(t); t = setTimeout(update, 60); }, { passive: true });
    window.addEventListener('resize', function () { go(current); });
    update();
  });
})();
