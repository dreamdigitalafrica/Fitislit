(function () {
  var header = document.querySelector('.header');
  var nav = header && header.querySelector('nav');
  if (!nav) return;
  nav.id = 'primary-navigation';
  var toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'mobile-menu-toggle';
  toggle.setAttribute('aria-controls', nav.id);
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-label', 'Open menu');
  toggle.innerHTML = '<span></span><span></span>';
  header.appendChild(toggle);
  header.classList.add('menu-ready');
  function setOpen(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    nav.classList.toggle('is-open', open);
  }
  toggle.addEventListener('click', function () { setOpen(toggle.getAttribute('aria-expanded') !== 'true'); });
  header.addEventListener('keydown', function (event) { if (event.key === 'Escape') { setOpen(false); toggle.focus(); } });
  nav.addEventListener('click', function (event) { if (event.target.closest('a')) setOpen(false); });
  window.matchMedia('(max-width:700px)').addEventListener('change', function () { setOpen(false); });
})();
