"""Render the three class previews using the supplied class-detail frame."""
from pathlib import Path
import json, re
root = Path(__file__).resolve().parents[1] / 'dist'
catalog = json.loads((root/'js/course-catalog.json').read_text())
source=(root/'courses.html').read_text()
head=source.split('<main>')[0].replace('class="collection-page"','class="collection-page class-preview"')
if 'css/class-preview.css' not in head: head=head.replace('</head>','<link rel="stylesheet" href="css/class-preview.css"></head>')
footer=source[source.index('<footer'):]
if 'js/store.js' not in footer: footer=footer.replace('</body>','<script src="js/store.js"></script></body>')
content={
 'weight-gain':{
  'headline':'Build strength, one step at a time.',
  'focus':'Weight gain',
  'intro':'Give your strength goals a place in your everyday routine. Explore a prerecorded programme built around movement, consistency and your next step.',
  'benefits':['A clear strength-training focus','A prerecorded class format','Space to build a routine','A goal-led starting point','One-time purchase'],
  'steps':[('Find your starting point','Think about your current routine and the strength goals you want to work towards.'),('Explore the programme','The lesson outline and sample videos will be added here before the programme launches.'),('Make room for consistency','Choose a regular time for movement and build a routine that works for you.')],
 },
 'weight-loss':{
  'headline':'Make movement part of your everyday life.',
  'focus':'Weight loss',
  'intro':'Create space for your fitness goals with a prerecorded programme focused on movement and consistency. Start with your next step and build from there.',
  'benefits':['A clear weight-loss focus','A prerecorded class format','Movement that fits your routine','A goal-led starting point','One-time purchase'],
  'steps':[('Choose your focus','Take a moment to consider your goals and how movement can fit into your week.'),('Explore the programme','The lesson outline and sample videos will be added here before the programme launches.'),('Build your routine','Make time for regular movement and focus on the habits you can keep returning to.')],
 },
 'nutrition-guide':{
  'headline':'Bring more intention to everyday meals.',
  'focus':'Everyday nutrition',
  'intro':'Explore a digital guide designed around everyday food choices. Bring your nutrition goals into focus and make space for more thoughtful meal planning.',
  'benefits':['An everyday nutrition focus','A digital guide format','A companion to your fitness goals','Space to plan your meals','One-time purchase'],
  'steps':[('Start with your habits','Think about the food choices and meal routines you would like to explore.'),('Preview the guide','The contents and sample pages will be added here before the guide launches.'),('Put your plans into practice','Use your goals as a starting point for building a more intentional everyday food routine.')],
 }
}
for item in catalog:
 key=item['id']; c=content[key]; name=item['name']; price='₦'+format(item['price'],',')
 h=re.sub(r'<title>.*?</title>',f'<title>{name} preview | Fit is Lit</title>',head)
 h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{item["desc"]}">',h)
 h=h.replace('<a href="courses.html">Classes</a>','<a href="courses.html" aria-current="page">Classes</a>')
 facts=[('Format',item['type']),('Focus',c['focus']),('Price',price),('By','Fit is Lit')]
 tiles=''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a,b in facts)
 benefits=''.join(f'<li>{b}</li>' for b in c['benefits'])
 steps=''.join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t,d in c['steps'])
 main=f'''<main id="main-content">
<section class="preview-hero wrap" aria-labelledby="course-title">
<h1 id="course-title">{name}</h1>
<div class="preview-visual"><img src="images/fitislit/{item['image']}" alt="{name} programme artwork" fetchpriority="high"><dl class="preview-facts">{tiles}</dl></div>
</section>
<section class="preview-details wrap">
<aside class="preview-sidebar" aria-label="Programme access and purchase">
<h2>{'Guide access' if key=='nutrition-guide' else 'Class access'}</h2>
<div class="access-card"><h3>{'Digital guide' if key=='nutrition-guide' else 'At your own pace'}</h3><p>{'Explore nutrition in your own time.' if key=='nutrition-guide' else 'Prerecorded classes to fit around your routine.'}</p><span>No live timetable</span></div>
<div class="access-card"><h3>One-on-one mentorship</h3><p>Coming soon</p><span>Bookings are not open yet.</span></div>
<div class="preview-purchase"><span class="eyebrow">ONE-TIME PURCHASE</span><strong>{price}</strong><form class="fit-add-form" data-product="{key}"><label for="quantity">Quantity</label><input id="quantity" name="quantity" type="number" min="1" max="10" value="1" required><button class="button" type="submit">Add to cart</button></form><p class="fit-cart-status" role="status" aria-live="polite"></p><a class="text-link" href="cart.html">View cart (<span data-cart-count>0</span>)</a><p class="demo-message">Demo checkout only. No payment is taken and no course access is issued.</p></div>
</aside>
<div class="preview-body"><section><h2>{c['headline']}</h2><p>{c['intro']}</p><p>{item['desc']}</p></section>
<section><h2>{'Why explore this guide?' if key=='nutrition-guide' else 'Why choose this programme?'}</h2><ul class="preview-benefits">{benefits}</ul></section>
<section><h2>What to expect</h2><ol class="preview-journey">{steps}</ol></section>
<p class="preview-availability">{'Sample pages and the full guide contents' if key=='nutrition-guide' else 'Sample videos, lesson details and class durations'} are coming soon. This page is a preview; purchases are currently a demonstration.</p>
</div></section>
<section class="preview-team wrap"><h2>Meet Fit is Lit</h2><div class="preview-people">
<a class="preview-person" href="about.html"><img src="images/fitislit/sheba-founder.jpg" alt="Faith Sheba Gamde" loading="lazy"><h3>Faith Sheba Gamde</h3><p>Founder, Fit is Lit</p></a>
<a class="preview-person" href="about.html"><img src="images/fitislit/community-workout.jpg" alt="The Fit is Lit community working out together" loading="lazy"><h3>Movement & community</h3><p>Make room for your goals</p></a>
<article class="preview-person"><img src="images/fitislit/coaching-sheba.jpg" alt="Sheba in a gym coaching scene" loading="lazy"><h3>One-on-one mentorship</h3><p>Coming soon</p></article>
</div></section>
<section class="preview-closing wrap"><div><h2>Your next step starts with Fit is Lit.</h2><p>Movement, nutrition and the everyday commitment to keep going. Find the focus that fits your goals.</p><a class="text-link" href="courses.html">Explore all classes & guides</a><a class="button" href="contact.html">Contact us</a></div><img src="images/fitislit/community-workout.jpg" alt="Outdoor group fitness session" loading="lazy"></section>
</main>'''
 (root/f'{key}.html').write_text(h+main+footer)
