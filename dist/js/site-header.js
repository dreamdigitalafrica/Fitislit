(() => {
 const header=document.querySelector('.site-header');
 if(!header)return;
 const menu=header.querySelector('.site-menu'),nav=header.querySelector('nav');
 const close=()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open menu');};
 menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close menu':'Open menu');});
 nav.addEventListener('click',close);
 document.addEventListener('click',e=>{if(!header.contains(e.target))close();});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){close();menu.focus();}});
 window.addEventListener('resize',close);
 const path=location.pathname;
 nav.querySelectorAll('a').forEach(a=>{if(a.getAttribute('href')===path||(path==='/fit-is-lit'&&a.getAttribute('href')==='/fit-is-lit.html'))a.setAttribute('aria-current','page');});
 // Keyboard equivalent of the theme's thumbnail hover interaction.
 const gallery=document.querySelector('.tp-hero-scale-gallery'),hero=document.querySelector('.tp-hero-scale-content');
 const backgrounds=document.querySelectorAll('.tp-hero-scale-background .background-img');
 if(gallery&&hero){
 gallery.addEventListener('focusin',e=>{const thumb=e.target.closest('[data-index]');if(!thumb)return;hero.style.opacity='0';backgrounds.forEach((bg,i)=>bg.style.opacity=i===Number(thumb.dataset.index)?'1':'0');});
 gallery.addEventListener('focusout',e=>{if(!gallery.contains(e.relatedTarget)){hero.style.opacity='1';backgrounds.forEach(bg=>bg.style.opacity='0');}});
 }
})();
