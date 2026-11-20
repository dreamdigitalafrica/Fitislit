"""Build Sheba catalogue pages with the supplied Cunnet HTML/CSS structure."""
from pathlib import Path
from html import escape as e
from bs4 import BeautifulSoup as Soup
from PIL import Image, ImageChops
import json, re
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'dist'
T=Path('/Users/mac/Downloads/cunnet-creative-agency-portfolio-html-template-2026-07-13-05-30-05-utc/cunnet')
B=D/'images/brand'; B.mkdir(exist_ok=True)
for name,src in [('sheba-logo','/var/folders/fz/m1q3s_fx655b6jlrxqhl1lj80000gn/T/codex-clipboard-e072d119-b4ef-4a11-ba87-0f6e486d1cb2.png'),('sheba-mark','/var/folders/fz/m1q3s_fx655b6jlrxqhl1lj80000gn/T/codex-clipboard-a7404897-3d8f-4063-a451-f00729a81cfc.png')]:
 im=Image.open(src).convert('RGB'); mask=im.convert('L').point(lambda p:255 if p<200 else 0); box=mask.getbbox(); im=im.crop(box)
 if name=='sheba-logo':
  im.thumbnail((900,450),Image.Resampling.LANCZOS); im.save(B/(name+'.webp'),lossless=True)
 else:
  size=max(im.size)+80; square=Image.new('RGB',(size,size),'white'); square.paste(im,((size-im.width)//2,(size-im.height)//2))
  for n in [32,180,192,512]: square.resize((n,n),Image.Resampling.LANCZOS).save(B/f'favicon-{n}.png')
  square.save(D/'favicon.ico',sizes=[(16,16),(32,32),(48,48)])
P=D/'images/products'; P.mkdir(exist_ok=True)
merch=[('sports-water-bottle','Sports Water Bottle',154700,'Accessories','Black bottle. Green lid. Ready for your next workout.'),('running-shoes','Men’s Climacool Leap Running Tennis Shoe',284500,'Footwear','Black running shoes with a lime-green sole.'),('gym-tights','Gym Tights',97800,'Activewear','Classic black tights for your workout wardrobe.'),('gym-workout-top','Gym Workout Top',332500,'Activewear','A bright green sleeveless top for your next session.')]
sheet=Image.open(D/'images/fitislit/shop-products.jpg')
items=[]
for i,(slug,name,price,cat,desc) in enumerate(merch):
 im=sheet.crop((round(i*sheet.width/4),0,round((i+1)*sheet.width/4),sheet.height)); im.save(P/f'{slug}.webp',quality=95,method=6)
 items.append(dict(id=slug,name=name,price=price,category=cat,group='products',desc=desc,image=f'images/products/{slug}.webp'))
for obj in json.loads((D/'js/course-catalog.json').read_text()):
 stock={'weight-gain':'studio','weight-loss':'rope','nutrition-guide':'nutrition'}[obj['id']]
 items.append(dict(id=obj['id'],name=obj['name'],price=obj['price'],category=obj['type'],group='guides' if obj['id']=='nutrition-guide' else 'classes',desc=obj['desc'],image=f'images/stock/{stock}-1280.webp',stock=stock))
logo='<img src="/images/brand/sheba-logo.webp" alt="Sheba Imprint" width="872" height="450" decoding="async">'
header=f'''<header class="site-header"><div class="site-header-inner"><a class="site-brand" href="/">{logo}</a><nav aria-label="Main navigation" id="site-navigation"><a href="/about.html">About</a><a href="/fit-is-lit.html">Fit is Lit</a><a href="/podcast.html">Podcast</a><a href="/sheba-care.html">Com. Support</a></nav><button aria-controls="site-navigation" aria-expanded="false" aria-label="Open menu" class="site-menu"><span></span><span></span></button></div></header>'''
def button(text,href,cls='tp-btn tp-btn-grey'):
 return f'<a class="{cls}" href="{href}"><span><span class="text-1">{text}</span><span class="text-2" aria-hidden="true">{text}</span></span></a>'
footer=f'''<footer><div class="tp-footer-area pt-145"><div class="container"><div class="row"><div class="col-xl-9"><div class="tp-footer-title-wrap mb-55"><h2 class="tp-section-title">Let’s talk. {button('Get in touch','contact.html','tp-btn tp-btn-border')}</h2></div></div></div><div class="tp-about-border pt-50"><nav class="sheba-footer-links" aria-label="Footer"><a href="services.html">Services &amp; products</a><a href="shop.html">Lit Store</a><a href="podcast.html">Podcast</a><a href="sheba-care.html">Sheba Care</a><a href="cart.html">Cart (<span data-cart-count>0</span>)</a></nav><div class="row align-items-end mt-35"><div class="col-lg-4"><div class="tp-footer-logo mb-30"><a class="site-brand" href="/">{logo}</a></div></div><div class="col-lg-8"><div class="tp-footer-text text-lg-end"><h2 class="tp-footer-bigtext text-uppercase tp-ff-sequel-bold-head"><a href="contact.html">Say Hello!</a></h2></div></div></div></div></div></div></footer>'''
def page(title,main,kind=''):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | Sheba Imprint</title><meta name="description" content="{e(title)} from Sheba Imprint. Fitness, wellbeing and community."><link rel="icon" href="/favicon.ico"><link rel="icon" type="image/png" sizes="32x32" href="/images/brand/favicon-32.png"><link rel="apple-touch-icon" href="/images/brand/favicon-180.png"><link rel="stylesheet" href="cunnet-assets/css/bootstrap.min.css"><link rel="stylesheet" href="cunnet-assets/css/spacing.css"><link rel="stylesheet" href="cunnet-assets/css/main.css"><link rel="stylesheet" href="css/site-header.css"><link rel="stylesheet" href="css/sheba-catalog.css"></head><body class="sheba-theme {kind}">{header}<main>{main}</main>{footer}<script src="cunnet-assets/js/bootstrap.min.js"></script><script src="js/store.js?v=2"></script><script src="js/catalog.js"></script><script src="js/site-header.js"></script></body></html>'''
def img(p,cls='w-100',eager=False):
 attrs=f'srcset="images/stock/{p["stock"]}-640.webp 640w, images/stock/{p["stock"]}-1280.webp 1280w, images/stock/{p["stock"]}-2560.webp 2560w" sizes="(max-width:767px) 100vw, 50vw"' if p.get('stock') else 'width="543" height="724"'
 return f'<img class="{cls}" src="{p["image"]}" {attrs} alt="{e(p["name"])}" loading="{"eager" if eager else "lazy"}" decoding="async">'
def top(title,crumb='Lit Store'):
 return f'''<div class="tp-pd-2-ptb pt-200"><div class="container"><div class="row"><div class="col-12"><div class="tp-pd-2-top tp-breadcrumb-border pb-90 text-center"><div class="tp-pd-2-categories mb-10"><span><a href="/">Sheba</a></span><span>{crumb}</span></div><h1 class="tp-section-title fs-92 tp-ff-sequel-semi-bold">{title}</h1></div></div></div></div></div>'''
def card(p):
 return f'''<div class="col-xl-3 col-lg-4 col-md-6" data-product-card data-price="{p['price']}" data-name="{e(p['name'])}"><article class="shop-product-item mb-60"><div class="shop-product-thumb p-relative mb-30"><a href="{p['id']}.html">{img(p)}</a><div class="shop-product-btn"><button type="button" class="tp-btn tp-action-btn" data-add="{p['id']}" aria-label="Add {e(p['name'])} to cart"><span><span class="text-1">Add to cart</span><span class="text-2" aria-hidden="true">Add to cart</span></span></button></div></div><div class="shop-product-content-wrap d-flex justify-content-between gap-3"><div class="shop-product-content"><h2 class="shop-product-title tp-title-anim d-inline-block fix tp-ff-inter fw-500 mb-0 lh-1"><a class="tp-title-text" href="{p['id']}.html">{e(p['name'])}</a></h2><span class="shop-product-cetagory">{p['category']}</span></div><div class="shop-product-price"><span class="shop-product-new-price">₦{p['price']:,}</span></div></div><p class="fit-cart-status" role="status"></p></article></div>'''
# Portfolio: retain the reference's heading, sidebar, column widths and card classes.
services='''<div class="tp-breadcrumb-area about-us-spacing pb-100"><div class="container"><div class="tp-breadcrumb-border pb-20"><div class="row align-items-end"><div class="col-lg-9"><div class="tp-tp-breadcrumb-main mb-30"><h1 class="tp-breadcrumb-title tp-ff-sequel-bold-head">Services<br>&amp; Products</h1></div></div></div></div></div></div><div class="tp-portfolio-inner-ptb tp-animate-tab tp-portfolio-inner-tab-style-2 pb-75"><div class="container"><div class="row"><div class="col-xxl-4 col-xl-3"><div class="tp-portfolio-inner-tab-wrap mb-25"><nav aria-label="Filter services and products"><div class="nav nav-tabs">'''
for group,label in [('all','All'),('classes','Classes'),('guides','Guides'),('products','Products')]:
 services+=f'<button class="nav-link {"active" if group=="all" else ""}" type="button" data-filter="{group}" aria-pressed="{str(group=="all").lower()}" aria-controls="service-grid">{label}</button>'
services+='</div></nav></div></div><div class="col-xxl-8 col-xl-9"><div class="tp-portfolio-tab-content-wrap"><div class="row gx-60" id="service-grid">'
for p in items[4:]+items[:4]:
 services+=f'''<div class="col-lg-6" data-category="{p['group']}"><article class="mg-portfolio-item mb-55"><div class="mg-portfolio-thumb {'service-photo' if p.get('stock') else 'product-photo'}"><a href="{p['id']}.html">{img(p)}</a></div><div class="mg-portfolio-content cs-portfolio-content d-flex align-items-center flex-wrap justify-content-between"><h2 class="cs-portfolio-title tp-title-anim fix mr-20 tp-ff-sequel-semi-bold"><a class="tp-title-text" href="{p['id']}.html">{e(p['name'])}</a></h2><div class="cs-portfolio-tag"><ul><li><span>{p['category']}</span></li></ul></div></div></article></div>'''
services+='</div></div></div></div></div></div>'
for name in ['services','products','courses','featured']: (D/f'{name}.html').write_text(page('Services & Products',services,'services-page'))
shop=top('Lit Store')+'''<section class="tp-product-ptb pt-50 pb-100"><div class="container"><div class="row"><div class="col-sm-6"><div class="tp-product-top-result mb-30"><p>Showing all 4 products</p></div></div><div class="col-sm-6"><div class="tp-product-top-select d-flex justify-content-sm-end mb-30"><label class="visually-hidden" for="product-sort">Sort products</label><select id="product-sort"><option value="default">Default sorting</option><option value="low">Price: low to high</option><option value="high">Price: high to low</option><option value="name">Name: A to Z</option></select></div></div></div><div class="row" id="shop-grid">'''+''.join(card(p) for p in items[:4])+'''</div><p class="store-note">Checkout is a preview. No payment is taken.</p></div></section>'''
for name in ['shop','shop-list']: (D/f'{name}.html').write_text(page('Lit Store',shop,'shop-page'))
# Detail pages use the supplied two-column product layout and Bootstrap information tabs.
for p in items:
 digital=p['group']!='products'; note='Course access is not yet available.' if digital else 'Contact us for sizes and availability.'
 details=top('Product Details',f'<a href="shop.html">Lit Store</a>').replace('<h1 ', '<h2 ').replace('</h1>', '</h2>')+f'''<section class="tp-product-details-area pt-130"><div class="tp-product-details-top pb-115"><div class="container"><div class="row justify-content-center"><div class="col-xxl-10"><div class="row"><div class="col-xl-7 col-lg-6"><div class="tp-product-details-thumb-wrapper tp-tab"><div class="tab-content m-img"><div class="tp-product-details-nav-main-thumb {'digital-photo' if digital else ''}">{img(p,eager=True)}</div></div></div></div><div class="col-xl-5 col-lg-6"><div class="tp-product-details-wrapper"><div class="tp-product-details-category"><span>{p['category']}</span></div><h1 class="tp-product-details-title">{e(p['name'])}</h1><div class="tp-product-details-sort-desc"><p>{e(p['desc'])}</p></div><div class="tp-product-details-price-wrapper mb-20"><span class="tp-product-details-price new-price">₦{p['price']:,}</span></div><form class="fit-add-form tp-product-details-action-wrapper" data-product="{p['id']}"><label class="tp-product-details-action-title" for="quantity">Quantity</label><div class="tp-product-details-action-item-wrapper d-flex align-items-center"><div class="tp-product-details-quantity"><div class="tp-product-quantity mb-15 mr-15"><button type="button" class="tp-cart-minus" data-step="-1" aria-label="Decrease quantity">−</button><input class="tp-cart-input" type="number" id="quantity" name="quantity" min="1" max="10" value="1" required><button type="button" class="tp-cart-plus" data-step="1" aria-label="Increase quantity">+</button></div></div><div class="tp-product-details-add-to-cart mb-15 w-100"><button class="tp-product-details-add-to-cart-btn w-100" type="submit">Add to cart</button></div></div><a href="cart.html" class="tp-product-details-buy-now-btn w-100 d-block text-center">View cart</a></form><p class="fit-cart-status" role="status"></p><p class="store-note">Checkout is a preview. No payment is taken.</p><p>{note} <a class="sheba-text-link" href="contact.html">Get in touch</a></p></div></div></div></div></div></div></div><div class="tp-product-details-bottom pb-140"><div class="container container-1230"><div class="row justify-content-center"><div class="col-xxl-10"><div class="tp-product-details-tab-nav tp-tab"><nav><div class="nav nav-tabs" role="tablist"><button class="nav-link active" id="description-tab" data-bs-toggle="tab" data-bs-target="#description" type="button" role="tab" aria-controls="description" aria-selected="true">Description</button><button class="nav-link" id="information-tab" data-bs-toggle="tab" data-bs-target="#information" type="button" role="tab" aria-controls="information" aria-selected="false">Additional information</button></div></nav><div class="tab-content"><div class="tab-pane fade show active" id="description" role="tabpanel" aria-labelledby="description-tab" tabindex="0"><div class="tp-product-details-desc-wrapper pt-50"><h2 class="tp-product-details-desc-title">{e(p['name'])}</h2><p>{e(p['desc'])}</p></div></div><div class="tab-pane fade" id="information" role="tabpanel" aria-labelledby="information-tab" tabindex="0"><div class="tp-product-details-additional-info pt-50"><table><tbody><tr><th scope="row">Category</th><td>{p['category']}</td></tr><tr><th scope="row">Availability</th><td>{note}</td></tr></tbody></table></div></div></div></div></div></div></div></div></section><section class="shop-product-area pb-85"><div class="container"><h2 class="tp-section-title tp-ff-sequel-semi-bold mb-50">You may also like</h2><div class="row">'''+''.join(card(q) for q in items if q['id']!=p['id'] and (q['group']!='products' if digital else q['group']=='products'))+'</div></div></section>'
 (D/f'{p["id"]}.html').write_text(page(p['name'],details,'product-detail-page'))
(D/'shop-product-page.html').write_text((D/'sports-water-bottle.html').read_text())
# Podcast: preserve the blog-list composition; clearly distinguish topic previews from episodes.
main=Soup((T/'blog-list-light.html').read_text(),'html.parser').main
main.select_one('.tp-breadcrumb-title').name='h1'; main.select_one('.tp-breadcrumb-title').string='Podcast'
main.select_one('.tp-breadcrumb-date').string='Coming soon'
main.select_one('.tp-breadcrumb-dec').string='Conversations on movement, wellbeing and community.'
main.select_one('.tp-banner-thumb').clear(); main.select_one('.tp-banner-thumb').append(Soup(img(dict(name='The Sheba community',image='images/stock/voices-2560.webp',stock='voices'),'img-cover',True),'html.parser'))
features=[('Movement','Finding a routine that works for you.','studio'),('Everyday wellbeing','Making space for food, rest and feeling good.','nutrition')]
for article,(title,desc,stock) in zip(main.select('.postbox-item'),features):
 article.select_one('.postbox-thumb').clear(); article.select_one('.postbox-thumb').append(Soup(img(dict(name=title,image=f'images/stock/{stock}-1280.webp',stock=stock)),'html.parser'))
 article.select_one('.mp-blog-date').string='Topic preview'
 h=article.select_one('.postbox-title'); h.string=title
 article.select_one('p').string=desc
 article.select_one('.tp-btn').decompose()
main.select_one('.tp-blog-tag').decompose()
rows=main.select('.tp-blog-list-item')
for row in rows[1:]: row.decompose()
row=rows[0]; row.select_one('.tp-blog-list-thumb').clear(); row.select_one('.tp-blog-list-thumb').append(Soup(img(dict(name='Women sharing time after a workout',image='images/stock/outdoors-1280.webp',stock='outdoors')),'html.parser'))
content=row.select_one('.tp-blog-list-content'); content.clear(); content.append(Soup('<span class="mp-blog-date mb-10 d-block">Coming soon</span><h2 class="postbox-title mb-15 tp-ff-sequel-semi-bold">Better together.</h2><p class="mb-30">Stories and conversations from the Sheba community. Episodes will be shared here.</p>'+button('Get in touch','contact.html'),'html.parser'))
for node in main.select('.tp-pagination,.basic-pagination,.tp-blog-list-pagination'): node.decompose()
for node in main.select('svg'): node.decompose()
for node in main.select('.tp_fade_anim'): node['class']=[c for c in node['class'] if c!='tp_fade_anim']
(D/'podcast.html').write_text(page('Podcast',main.decode_contents(),'podcast-page'))
# Apply the supplied identity to all active site pages, preserving unrelated template archives.
for path in D.glob('*.html'):
 text=path.read_text(); soup=Soup(text,'html.parser')
 if not soup.select_one('.site-header'): continue
 # Correct public text and attributes without renaming internal CSS selectors/asset paths.
 for node in soup.find_all(string=re.compile('shiba',re.I)):
  if node.parent.name not in ['script','style']: node.replace_with(re.sub('shiba','Sheba',str(node),flags=re.I))
 for tag in soup.find_all(True):
  for attr in ['alt','title','aria-label','content']:
   if tag.has_attr(attr): tag[attr]=re.sub('shiba','Sheba',tag[attr],flags=re.I)
  if tag.get('href'): tag['href']=tag['href'].replace('shiba-care.html','sheba-care.html')
 for a in soup.select('a.site-brand, footer a.logo'):
  a.clear(); a.append(Soup(logo,'html.parser')); a['href']='/'
 for old in soup.select('link[rel="icon"],link[rel="shortcut icon"],link[rel="apple-touch-icon"]'): old.decompose()
 for markup in ['<link rel="icon" href="/favicon.ico">','<link rel="icon" type="image/png" sizes="32x32" href="/images/brand/favicon-32.png">','<link rel="apple-touch-icon" href="/images/brand/favicon-180.png">']:
  soup.head.append(Soup(markup,'html.parser'))
 # Expose the combined catalogue in existing footers too.
 if soup.footer and not soup.footer.select('a[href="services.html"]'):
  nav=Soup('<nav class="sheba-footer-links" aria-label="Catalogue"><a href="services.html">Services &amp; products</a><a href="shop.html">Lit Store</a></nav>','html.parser'); soup.footer.insert(0,nav)
 path.write_text(str(soup))
(D/'sheba-care.html').write_text((D/'shiba-care.html').read_text())
