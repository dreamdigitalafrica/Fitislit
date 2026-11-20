## Cunnet restoration — 20 November 2026

Rebuilt the homepage from the supplied Cunnet `index.html`, retaining its original main CSS, hero thumbnails/background hover, mobile image sliders, section grids and animation dependencies. Replaced the long homepage copy with brief business content; removed added section labels, image captions and extra sections. Hero headline: “Live in Motion”.

All active fitness pages now use one static header matching the Cunnet navigation styling. Shared files: `dist/css/site-header.css` and `dist/js/site-header.js`. Fit is Lit has its own links within that same header style. The old header and mobile-nav script are removed from those pages. Native scrolling keeps the header in document flow.

Validation: local HTTP 200, page links/assets, single-header checks, nine hero thumbnails/backgrounds, all JS syntax and CSS asset references. Browser visual verification was unavailable in this chat.

# Shiba Imprint and Fit is Lit

The main homepage (`dist/index.html`) introduces Shiba Imprint using the supplied Cunnet typography and agency layout as a base, with existing founder and Fit is Lit assets. Content is adapted from the existing website and business profile; children’s clothing remains marked as in development.

The former Fit is Lit homepage is preserved at `/fit-is-lit.html` (also `/fit-is-lit` through a Vercel rewrite). Existing classes, products, cart and contact pages remain available at their established URLs. Their navigation links back to Shiba Imprint and to the dedicated Fit is Lit homepage.

Homepage customization: `dist/css/shiba.css` and `dist/js/shiba.js`. Cunnet CSS and fonts: `dist/cunnet-assets/`. Deployment retains the existing Vercel project and `dist` output directory. This change does not configure a custom domain.

Validation: desktop and 390px mobile browser previews, mobile menu and round-trip navigation, local link/asset validation. Existing demo checkout and local-only enquiry behavior are unchanged.

---

# Fit is Lit landing page

Static homepage adapted from the supplied TennisClub HTML template. The original section sequence, grids, three-frame Revolution Slider and four-offer cards are retained.

## Offers
- Weight Gain
- Weight Loss
- Nutrition Guide
- One-on-One

Kids clothing is excluded from this homepage.

## Preview
Run `python3 -m http.server 8765 --directory dist` and open http://localhost:8765.

Edit `dist/index.html`, `dist/css/fitislit.css` and `dist/js/fitislit.js`. The other original template pages are retained as source material and are not linked from the adapted homepage.

## Assets and launch details
The supplied Fit is Lit brand board is displayed using a CSS crop. Strength and coaching images are illustrative AI imagery, not actual client photographs. Nutrition images use stock photography. The hero is an AI-assisted fitness composite using the supplied Sheba portraits as identity references.

Pricing, programme contents, durations, availability, payment integration and real contact delivery remain unconfirmed. Offer buttons select the enquiry topic. The enquiry form validates and downloads a local text draft; it does not send messages or collect data on a server. No checkout or booking is enabled. Brand philosophy copy replaces template testimonials to avoid fictional customer endorsements.

Private Sites deployment is configured in `.openai/hosting.json`. GitHub source: https://github.com/dreamdigitalafrica/Fitislit.

## Stock photography
Nutrition placements use a real stock photograph from Pexels: https://www.pexels.com/photo/photo-of-vegetable-salad-in-a-bowl-3298060/ . The original AI food image is no longer referenced.

Vercel deployment uses the static `dist` output directory configured in `vercel.json`. Intended production URL: https://fitislit.vercel.app/ .
