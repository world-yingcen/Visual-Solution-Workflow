(() => {
  'use strict';

  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'scroll-top';
  button.hidden = true;
  button.setAttribute('aria-label', '回到頂部');
  button.title = '回到頂部';
  button.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 11 6-6 6 6M12 5v14"/></svg>';
  document.body.append(button);

  const update = () => { button.hidden = window.scrollY < 320; };
  let pending = false;
  window.addEventListener('scroll', () => {
    if (pending) return;
    pending = true;
    window.requestAnimationFrame(() => {
      update();
      pending = false;
    });
  }, { passive: true });
  window.addEventListener('pageshow', update);

  button.addEventListener('click', () => {
    const top = document.getElementById('top');
    if (top) {
      top.setAttribute('tabindex', '-1');
      top.focus({ preventScroll: true });
    }
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: 0, behavior: reduceMotion ? 'instant' : 'smooth' });
  });
  update();
})();
