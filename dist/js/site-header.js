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
 new ResizeObserver(()=>document.documentElement.style.setProperty('--site-header-height',header.offsetHeight+'px')).observe(header);
 const path=location.pathname;
 nav.querySelectorAll('a').forEach(a=>{if(a.getAttribute('href')===path||(path==='/fit-is-lit'&&a.getAttribute('href')==='/fit-is-lit.html'))a.setAttribute('aria-current','page');});
 const hero=document.querySelector('.shiba-hero'),gallery=document.querySelector('.spotlight-gallery');
 if(!hero||!gallery)return;
 const backgrounds=[...hero.querySelectorAll('.spotlight-background')];
 let active=-1;
 function show(thumb){
  const index=Number(thumb.dataset.index);active=index;
  const bg=backgrounds[index],img=bg.querySelector('img');
  const reveal=()=>{if(active!==index)return; backgrounds.forEach((b,i)=>b.classList.toggle('active',i===index));hero.classList.add('previewing');};
  if(!img.src){img.src=img.dataset.src;img.addEventListener('load',reveal,{once:true});}
  if(img.complete&&img.naturalWidth)reveal();
 }
 function reset(){active=-1;hero.classList.remove('previewing');backgrounds.forEach(bg=>bg.classList.remove('active'));}
 gallery.querySelectorAll('.thumbs').forEach(thumb=>{
  thumb.addEventListener('mouseenter',()=>{if(matchMedia('(hover:hover)').matches)show(thumb);});
  thumb.addEventListener('focus',()=>show(thumb));
 });
 gallery.addEventListener('mouseleave',()=>{if(!gallery.contains(document.activeElement))reset();});
 gallery.addEventListener('focusout',e=>{if(!gallery.contains(e.relatedTarget))reset();});
 document.addEventListener('keydown',e=>{if(e.key==='Escape')reset();});
})();
