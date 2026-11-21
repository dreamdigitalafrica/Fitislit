# Sheba Imprint and Fit is Lit

Static website deployed from `dist` through the existing Vercel Git connection.
Production: https://sheba-imprint.vercel.app/
Source: https://github.com/dreamdigitalafrica/Shebaimprint

## Pages and styling

- `/` uses the supplied Cunnet fonts and components. The opening frame sizes itself to the viewport, with nine service thumbnails and on-demand background previews.
- `/fit-is-lit.html` (also `/fit-is-lit`) contains the fitness homepage. `/shop.html` contains the merchandise store.
- `/podcast.html` and `/sheba-care.html` are initial pages awaiting episode and programme details.
- All active pages share one static header: About, Fit is Lit, Podcast, Com. Support.
- Shared header: `dist/css/site-header.css`, `dist/js/site-header.js`. Homepage: `dist/css/shiba.css`. Fitness/store refinements: `dist/css/fitness-refresh.css`.

## Photography

Ten supplied stock photos have responsive 640, 1280 and 2560 pixel WebP copies in `dist/images/stock`. The original files are unchanged. `scripts/prepare-stock-images.py` reproduces these copies using Pillow. Nine initial hero thumbnails total approximately 413 KB; full background images load on interaction. Founder portraits and actual product imagery remain separate from illustrative stock photos.

## Local preview and verification

Run `python3 -m http.server 8766 --directory dist` and visit http://localhost:8766/.

Validated all 27 active pages for local assets/links, one shared header, navigation labels, button arrows, and nine gallery images/backgrounds. JavaScript syntax checks pass. The desktop homepage was visually reviewed in Chrome. Further emulated viewport checks were interrupted by browser automation failure.

## Content and functional status

The replacement headline for “Live in Motion” is still awaiting the approved wording. Existing catalogue prices have been retained. Cart/checkout are demos; the enquiry form opens an email draft addressed to Shebasimprint@gmail.com; the visitor sends it from their email app. No payment or donation processing is configured. This update does not configure a custom domain.

## Cunnet refinements

`/services.html` uses the portfolio catalogue, `/service-details.html` uses the dark service layout, and the shop/product/podcast pages retain the reference image proportions. The homepage portfolio cards use 830:632 frames. All active pages use the extracted Sheba Imprint identity and a shared Cunnet footer. `scripts/refine-theme.py` applies the footer and service template; it requires BeautifulSoup4 and tinycss2. GSAP, ScrollTrigger and Bootstrap are supplied in the theme assets; motion respects reduced-motion preferences.

The Vercel project is named `sheba-imprint` and connected to the renamed GitHub repository. Product filters, sorting, cart totals, quantity bounds and Bootstrap tabs pass automated DOM checks. Desktop shop, service and podcast layouts were reviewed. The final mobile visual check was interrupted when the browser window became unavailable.
