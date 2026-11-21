"""Apply the supplied Cunnet frames, footer and motion to active Sheba pages."""
from pathlib import Path
from bs4 import BeautifulSoup as S
import tinycss2 as css
R=Path(__file__).resolve().parents[1]; D=R/'dist'; T=R/'scripts/templates'
EMAIL='Shebasimprint@gmail.com'; MAIL='mailto:'+EMAIL
logo='<img src="/images/brand/sheba-imprint.webp" alt="Sheba Imprint" width="1721" height="914" decoding="async">'
f=S((T/'cunnet-footer.html').read_text(),'html.parser').footer
f['class']=['sheba-footer']
h=f.select_one('.tp-footer-title-wrap h2')
for n in list(h.children):
 if not getattr(n,'name',None): n.extract()
h.insert(0,'Let’s move forward together. ')
for n in f.select('svg,i'): n.decompose()
for a in f.select('.tp-btn,.tp-footer-bigtext a'): a['href']=MAIL
for n in f.select('.text-2'): n['aria-hidden']='true'
links=[('About','about.html'),('Fit is Lit','fit-is-lit.html'),('Services','service-details.html'),('Lit Store','shop.html'),('Podcast','podcast.html'),('Sheba Care','sheba-care.html'),('Contact','contact.html')]
nav=f.select_one('.tp-hero-social'); nav.clear()
for text,url in links: nav.append(S(f'<a href="/{url}">{text}</a>','html.parser'))
f.select_one('.tp-footer-dec').string='Get in touch'
a=f.select_one('.tp-footer-email a'); a.string=EMAIL; a['href']=MAIL
wrap=f.select_one('.tp-footer-logo'); wrap.clear(); wrap.append(S(f'<a href="/" aria-label="Sheba Imprint home">{logo}</a>','html.parser'))
for n in f.select('.tp-footer-copyright'): n.string='© 2026 Sheba Imprint'
social=f.select_one('.tp-footer-copyright-social'); social.clear()
for title,url in [('Services & products','services.html'),('Lit Store','shop.html'),('Contact','contact.html')]: social.append(S(f'<a href="/{url}">{title}</a>','html.parser'))
# Remove the template's duplicate copyright line, retaining its grid and spacing.
for n in f.select('.tp-footer-copyright-area .col-xl-3')[-1:]: n.clear()
# Service page: use the actual template grid, sections and Bootstrap accordion.
s=S((T/'service-details.html').read_text(),'html.parser'); m=s.main
m.select_one('.tp-service-details-hero-subtitle span').string='Fit is Lit'
h=m.select_one('.tp-service-details-hero-title h2'); h.name='h1'; h['class']=h.get('class',[])+['sheba-service-title']; h.string='Fitness & Wellbeing'
for a,(title,url) in zip(m.select('.tp-service-details-hero-link a'),[('Weight Gain','weight-gain.html'),('Weight Loss','weight-loss.html'),('Nutrition Guide','nutrition-guide.html'),('Lit Store','shop.html'),('Podcast','podcast.html'),('Sheba Care','sheba-care.html')]):
 a['href']=url; a.span.string=title; a.span['data-text']=title
for im,stock in zip(m.select('.tp-banner-thumb img'),['studio','community']):
 im['src']=f'images/stock/{stock}-2560.webp'; im['alt']='Movement and community'; im['loading']='lazy'; im['class']=['img-cover','scale-up']
m.select_one('.tp-process-area h2').string='Find your routine.'
for item,(title,desc) in zip(m.select('.tp-process-item'),[('Choose your focus','Weight gain, weight loss or everyday nutrition.'),('Find your guide','Browse classes and nutrition resources.'),('Make it yours','Choose a routine that fits your day.'),('Stay connected','Discover conversations and community.')]):
 item.h3.string=title; item.p.string=desc
p=m.select_one('.tp-process-bottom-para'); p.clear(); p.append(S(f'<a class="tp-btn tp-btn-border" href="{MAIL}">Get in touch</a>','html.parser'))
m.select_one('.tp-service-overview-top h2').string='Fit is Lit'
m.select_one('.tp-service-details-dec').string='Classes, nutrition guides and active essentials from Sheba Imprint. Find your next step with Fit is Lit.'
m.select_one('.tp-service-details-title').string='Made for your everyday'
for p,text in zip(m.select('.tp-service-details-content li p'),['Weight Gain classes','Weight Loss classes','Nutrition Guide','Activewear and workout essentials']): p.string=text
im=m.select_one('.tp-service-thumb img'); im['src']='images/stock/yoga-1280.webp'; im['alt']='Women practising yoga'; im['loading']='lazy'
faqs=m.select('.tp-faq-area')
for extra in faqs[1:]: extra.decompose()
faq=faqs[0]; faq.select_one('.tp-faq-subtitle span').string='Good to know'; faq.select_one('h2.tp-section-title').string='Your questions, answered.'
questions=[('What can I find at Fit is Lit?','Browse Weight Gain and Weight Loss classes, a Nutrition Guide, and active essentials in Lit Store.'),('Are the classes available now?','Course access is not yet available. Contact us for updates.'),('How do I enquire about a product?','Email '+EMAIL+' with the product name and your question.'),('Where can I find the community?','Visit Com. Support for Sheba Care, and the podcast page for upcoming conversations.')]
for idx,item in enumerate(faq.select('.tp-faq-item')):
 if idx>=len(questions): item.decompose(); continue
 q,a=questions[idx]; item.button.string=f'{idx+1:02}. {q}'; item.select_one('.tp-faq-body').clear(); item.select_one('.tp-faq-body').append(S('<p>'+a+'</p>','html.parser'))
for n in m.select('a svg,.tp-service-details-content i'): n.decompose()
# The second banner finishes the template composition without a redundant second FAQ.
base=S((D/'services.html').read_text(),'html.parser'); base.main.replace_with(m)
base.html['class']=['cunnet-dark']; base.body['class']=['sheba-theme','service-detail-page']; base.title.string='Services | Sheba Imprint'
(D/'service-details.html').write_text(str(base))
# Scope the original Bootstrap and theme rules to footer so older Fit is Lit pages keep their content styling.
def scoped(rules):
 out=[]
 for r in rules:
  if r.type=='qualified-rule':
   selectors=[]
   for sel in css.serialize(r.prelude).split(','):
    sel=sel.strip()
    if sel in ['html','body',':root']: sel='.sheba-footer'
    elif sel.startswith('.cunnet-dark '): sel='.cunnet-dark .sheba-footer '+sel[len('.cunnet-dark '):]
    else: sel='.sheba-footer '+sel
    selectors.append(sel)
   out.append(','.join(selectors)+'{'+css.serialize(r.content)+'}')
  elif r.type=='at-rule':
   pre='@'+r.at_keyword+' '+css.serialize(r.prelude)
   if r.content is None: continue
   if r.lower_at_keyword in ['media','supports','layer']: content=scoped(css.parse_rule_list(r.content,skip_whitespace=True,skip_comments=True))
   else: content=css.serialize(r.content)
   out.append(pre+'{'+content+'}')
 return ''.join(out)
styles=''
for name in ['bootstrap.min.css','spacing.css','main.css']:
 styles+=scoped(css.parse_stylesheet((D/'cunnet-assets/css'/name).read_text(),skip_comments=True,skip_whitespace=True))
styles=styles.replace('../fonts/','../cunnet-assets/fonts/').replace('../img/','../cunnet-assets/img/')
(D/'css/sheba-footer.css').write_text(styles)
for path in D.glob('*.html'):
 doc=S(path.read_text(),'html.parser')
 if not doc.select_one('.site-header'): continue
 for a in doc.select('.site-header .site-brand'): a.clear(); a.append(S(logo,'html.parser'))
 if doc.footer: doc.footer.replace_with(S(str(f),'html.parser'))
 for name in ['sheba-footer.css','theme-refinements.css']:
  if not doc.select_one(f'link[href="css/{name}"]'): doc.head.append(S(f'<link rel="stylesheet" href="css/{name}">','html.parser'))
 if path.name=='podcast.html':
  ref=S((T/'podcast.html').read_text(),'html.parser')
  for sel in ['.tp-breadcrumb-main','.tp-breadcrumb-dec-wrap','.postbox-item','.tp-blog-list-item']:
   for i,n in enumerate(doc.select(sel)):
    n['class']=list(dict.fromkeys(n.get('class',[])+['tp_fade_anim'])); n['data-delay']=str(.3+.2*(i%2))
  for n in doc.select('.tp-banner-thumb'): n['class']=list(dict.fromkeys(n['class']+['scale-up-img'])); n.img['class']=['img-cover','scale-up']
 if path.name=='contact.html':
  doc.title.string='Contact | Sheba Imprint'
  doc.select_one('.contact-layout>div').clear(); doc.select_one('.contact-layout>div').append(S(f'<h2>Get in touch.</h2><p><a href="{MAIL}">{EMAIL}</a></p>','html.parser'))
  doc.select_one('#enquiry-form button').string='Open email'
  doc.select_one('.demo-message').string='Opens your email app with your enquiry.'
 for a in doc.select('a[href^="mailto:"]'): a['href']=MAIL
 # Reuse GSAP / ScrollTrigger already bundled with the licensed theme.
 existing=[n.get('src','') for n in doc.select('script[src]')]
 if not any('plugin.js' in x for x in existing):
  for src in ['cunnet-assets/js/vendor/jquery.js','cunnet-assets/js/plugin.js']:
   if src not in existing: doc.body.append(S(f'<script src="{src}"></script>','html.parser'))
 if not doc.select_one('script[src="js/sheba-motion.js"]'): doc.body.append(S('<script src="js/sheba-motion.js"></script>','html.parser'))
 for n in doc.select('a.tp-btn i,a.tp-btn svg,button.tp-btn i,button.tp-btn svg'): n.decompose()
 path.write_text(str(doc))
print('Refined active pages, service detail, shared footer and identity.')
