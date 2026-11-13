(function(){
 'use strict';
 var themeToggle=document.getElementById('fit-theme-toggle');
 function setTheme(theme){
  document.documentElement.dataset.theme=theme;
  var dark=theme==='dark';
  themeToggle.setAttribute('aria-pressed',String(dark));
  themeToggle.setAttribute('aria-label','Switch to '+(dark?'light':'dark')+' theme');
  themeToggle.querySelector('.fit-theme-label').textContent=dark?'Light':'Dark';
  themeToggle.querySelector('.fit-theme-icon').textContent=dark?'☀':'☾';
  try{localStorage.setItem('fit-theme',theme)}catch(e){}
 }
 setTheme(document.documentElement.dataset.theme==='dark'?'dark':'light');
 themeToggle.addEventListener('click',function(){setTheme(document.documentElement.dataset.theme==='dark'?'light':'dark')});
 var offers={
 'Weight Gain':'Explore a programme focused on your weight-gain goals. Programme contents, duration, suitability and pricing will be confirmed before enrolment.',
 'Weight Loss':'Explore a programme focused on your weight-loss goals. Programme contents, duration, suitability and pricing will be confirmed before enrolment.',
 'Nutrition Guide':'Explore general nutrition education for everyday food choices. Guide contents, access and pricing will be confirmed before purchase.',
 'One-on-One':'Ask about personal fitness support. Session format, availability, scope and pricing will be confirmed before booking.'
 };
 ['Sports Water Bottle','Men’s Climacool Leap Running Tennis Shoe','Gym Tights','Gym Workout Top'].forEach(function(name){offers[name]='Ask about '+name+'. Confirm size, colour, stock and delivery before ordering.'});
 var form=document.getElementById('fit-enquiry');
 var summary=document.createElement('div');summary.className='fit-offer-summary';summary.setAttribute('role','status');form.before(summary);
 function choose(name){
  if(!offers[name])return;
  summary.replaceChildren();var h=document.createElement('h3');h.textContent=name;var p=document.createElement('p');p.textContent=offers[name];summary.append(h,p);
  form.elements.subject.value=name+' enquiry';
 }
 document.addEventListener('click',function(e){var a=e.target.closest('[data-offer]');if(a)choose(a.dataset.offer);var slide=e.target.closest('[data-fit-target]');if(slide)location.hash=slide.dataset.fitTarget;});
 document.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){var t=e.target.closest('[data-fit-target],.sc_matches_next .sc_match');if(t){e.preventDefault();t.click();}}});
 form.addEventListener('submit',function(e){
  e.preventDefault();e.stopImmediatePropagation();if(!form.reportValidity())return;
  var text='Fit is Lit enquiry draft\n\nName: '+form.elements.username.value+'\nEmail: '+form.elements.email.value+'\nSubject: '+form.elements.subject.value+'\n\n'+form.elements.message.value+'\n\nSaved locally. This enquiry has not been sent.';
  var u=URL.createObjectURL(new Blob([text],{type:'text/plain'}));var a=document.createElement('a');a.href=u;a.download='fit-is-lit-enquiry.txt';a.click();setTimeout(function(){URL.revokeObjectURL(u)},1000);
  document.getElementById('enquiry-status').textContent='Your enquiry draft has been saved. Nothing has been sent.';
 },true);
})();
