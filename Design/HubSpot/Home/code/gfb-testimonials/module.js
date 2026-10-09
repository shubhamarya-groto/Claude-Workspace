/* GFB Testimonials: optional swipe for touch screens.
   The slider itself is HTML + CSS (hidden radios); this only checks the next or previous radio on a swipe. */
(function () {
  document.querySelectorAll('.gfb-tst').forEach(function (root) {
    if (root.dataset.gfbTstReady) return;
    root.dataset.gfbTstReady = '1';
    var radios = root.querySelectorAll('.gfb-tst__radio');
    var viewport = root.querySelector('.gfb-tst__viewport');
    if (radios.length < 2 || !viewport) return;
    var x0 = null;
    viewport.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    viewport.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      x0 = null;
      if (Math.abs(dx) < 40) return;
      var i = Array.prototype.findIndex.call(radios, function (r) { return r.checked; });
      var j = Math.max(0, Math.min(radios.length - 1, i + (dx < 0 ? 1 : -1)));
      radios[j].checked = true;
    }, { passive: true });
  });
})();
