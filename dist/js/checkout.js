(function(){
 'use strict';
 var products={
  'weight-gain':{name:'Weight Gain',kind:'Prerecorded classes',image:'weight-gain-square.jpg'},
  'weight-loss':{name:'Weight Loss',kind:'Prerecorded classes',image:'weight-loss-square.jpg'},
  'nutrition-guide':{name:'Nutrition Guide',kind:'Digital guide',image:'nutrition-chef.jpg'}
 };
 var slug=new URLSearchParams(window.location.search).get('product');
 var product=Object.prototype.hasOwnProperty.call(products,slug)?products[slug]:null;
 var content=document.getElementById('checkout-content');
 if(!product){content.hidden=true;document.getElementById('checkout-error').hidden=false;return;}
 document.getElementById('checkout-name').textContent=product.name;
 document.getElementById('checkout-kind').textContent=product.kind;
 var image=document.getElementById('checkout-image');image.src='images/fitislit/'+product.image;image.alt=product.name;
 document.getElementById('demo-purchase').addEventListener('click',function(){
  content.hidden=true;
  document.getElementById('demo-result').textContent=product.name+' · Demo total: US$100.00.';
  var success=document.getElementById('demo-success');success.hidden=false;success.focus();
 });
})();
