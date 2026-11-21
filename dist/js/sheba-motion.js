/* Cunnet's original fade and banner timings, with reduced-motion support. */
(() => {
  if (!window.gsap || !window.ScrollTrigger || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  // The homepage already runs these effects through the theme entry point.
  if ([...document.scripts].some(s => /cunnet-assets\/js\/main\.js/.test(s.src))) return;
  gsap.registerPlugin(ScrollTrigger);
  gsap.utils.toArray('.tp_fade_anim').forEach(item => {
    const offset = Number(item.dataset.fadeOffset || 40);
    const from = item.dataset.fadeFrom || 'bottom';
    const settings = {opacity:0,duration:Number(item.dataset.duration || .75),delay:Number(item.dataset.delay || .15),ease:item.dataset.ease || 'power2.out'};
    if (from === 'top' || from === 'bottom') settings.y = from === 'top' ? -offset : offset;
    if (from === 'left' || from === 'right') settings.x = from === 'left' ? -offset : offset;
    if (item.dataset.onScroll !== '0') settings.scrollTrigger = {trigger:item,start:'top 85%',once:true};
    gsap.from(item,settings);
  });
  gsap.utils.toArray('.scale-up-img').forEach(section => {
    const photo=section.querySelector('.scale-up');
    if(photo) gsap.timeline({scrollTrigger:{trigger:section,start:'top bottom',end:'bottom center',scrub:1}}).to(photo,{scale:1.15,duration:1});
  });
  window.addEventListener('load', () => ScrollTrigger.refresh(), {once:true});
})();
