(() => {
 'use strict';
 const filters=[...document.querySelectorAll('[data-filter]')];
 filters.forEach(button=>button.addEventListener('click',()=>{
  filters.forEach(item=>{const active=item===button;item.classList.toggle('active',active);item.setAttribute('aria-pressed',String(active));});
  document.querySelectorAll('[data-category]').forEach(card=>{card.hidden=button.dataset.filter!=='all'&&card.dataset.category!==button.dataset.filter;});
 }));
 const grid=document.getElementById('shop-grid'),sort=document.getElementById('product-sort');
 if(grid&&sort){
  const cards=[...grid.children];
  sort.addEventListener('change',()=>{
   const ordered=[...cards];
   if(sort.value==='low')ordered.sort((a,b)=>Number(a.dataset.price)-Number(b.dataset.price));
   if(sort.value==='high')ordered.sort((a,b)=>Number(b.dataset.price)-Number(a.dataset.price));
   if(sort.value==='name')ordered.sort((a,b)=>a.dataset.name.localeCompare(b.dataset.name));
   ordered.forEach(card=>grid.append(card));
  });
 }
 document.querySelectorAll('[data-step]').forEach(button=>button.addEventListener('click',()=>{
  const input=button.closest('.tp-product-quantity').querySelector('input');
  const value=Number(input.value)||1;
  input.value=Math.min(Number(input.max),Math.max(Number(input.min),value+Number(button.dataset.step)));
  input.dispatchEvent(new Event('change',{bubbles:true}));
 }));
})();
