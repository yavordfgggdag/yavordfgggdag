# Portfolio assets

Captured and checked on **5 October 2026** (Europe/Sofia).

## Real interface captures

| Files | Source | Treatment |
| --- | --- | --- |
| `screens/before-i-deploy.jpg`, `screens/bid-mission-control.jpg`, `screens/bid-command-palette.jpg` | Running Before I Deploy macOS application, using its existing demo project | Cropped to exclude account information and local filesystem paths; resized and framed |
| `screens/tlr-home.jpg` | https://the-last-republic.netlify.app/ | Public viewport capture, resized and framed |
| `screens/tlr-whitelist.jpg` | https://the-last-republic.netlify.app/whitelist | Public entry screen; no application submitted |
| `screens/police-dashboard.jpg` | https://the-last-republic.netlify.app/police | Authenticated screen; opaque redaction of profile identity, names and avatars |
| `screens/police-employees.jpg` | https://the-last-republic.netlify.app/police/employees | Authenticated screen; cropped profile header; individual record contents covered by opaque redactions |
| `screens/police-ranks.jpg` | https://the-last-republic.netlify.app/police/ranks | Authenticated screen; profile header excluded |
| `screens/police-handbook.jpg`, `screens/handbook-navigation.gif` | https://the-last-republic.netlify.app/police/handbook | Authenticated screen; profile header excluded; GIF shows three captured navigation states |

The two `*-preview.jpg` files are cropped thumbnail versions of their matching full-size captures.

The interfaces are genuine. Frames and English captions are presentation elements. Redactions are visibly labelled; they do not replace private data with fictional records. Unredacted source captures are not stored in this repository. Application counts, warnings and incident status are the captured UI state, not portfolio performance claims.

## Diagrams and animation

`bid-architecture.svg` and `tlr-architecture.svg` are explanatory architecture diagrams, not interface captures. They describe the inspected implementation at a high level; they do not certify production readiness or every integration.

The original `banner.svg` is preserved unchanged. Earlier `contact.svg`, `development-flow.svg` and `before-i-deploy-showcase.svg` are retained in the repository. The current README uses the new diagrams for its project explanations.

SVGs contain no scripts, foreign objects, remote fonts or externally loaded images. CSS animation is disabled by `prefers-reduced-motion: reduce`. The optional GIF is behind a collapsed disclosure and has a static `picture` source for reduced-motion browsers. GitHub/client support can vary; the static handbook image is always available separately.

The README keeps essential descriptions and contact information as selectable text. Primary screenshots use full-width images; detail views can be opened individually. JPEGs are optimized; the GIF is deliberately short.

## Evidence boundaries

- Technologies and engineering descriptions are based on inspected source manifests, implementation files and project documentation, supported by the displayed application and site states.
- Before I Deploy is described as actively developed. No public download, release certification, customer metric or end-to-end validation of external providers is claimed.
- TLR's public website and authenticated Police Portal were opened for the captures. The police section concerns a FiveM roleplay community, not a real law-enforcement deployment.
- Private repository URLs are not presented as public code links. Unverified client projects and template-only repositories are not presented as completed original products.

## Additional public work

`community-platform.jpg` and `community-rules.jpg` are real browser screenshots of the unmodified `yavordfgggdag/chillrp-website` frontend running locally on 2026-10-05. Production Supabase configuration was overridden with empty environment values. No account was used; server addresses and status labels are repository defaults, not verified live claims. Public source is linked in the profile.

`fraisbg1` is listed as a source-only experiment because referenced CSS/JS assets are absent from the public checkout. No replacement interface was fabricated.

## Languages and client website

English lives in README.md; Bulgarian lives in README.bg.md. Local SVG link buttons connect the two GitHub views. The original banner and captured UI remain unchanged. `client-education.jpg` and `client-education-faq.jpg` were captured from https://pomoshtotpriyatel.com/ on 2026-10-05. The homepage crop excludes the presenter video and contact strip; FAQ capture follows a real click. No form was submitted. WordPress and WPForms are evidenced by public page assets and the form markup. The TLR main-site gallery was withdrawn pending the owner’s current URL; local chillrp screenshots are explicitly distinguished from the current site.

## Studio visual system

The `studio/` directory contains original, repository-local SVG diagrams and chapter panels, plus a composition of existing genuine captures. CSS animations use slow orbits, paths and opacity changes; `prefers-reduced-motion` disables them. Manifesto and selected-work art have dedicated narrow-screen variants via `picture`. Real screenshots have not been replaced with generated interfaces. The original banner and contact panel remain intact.

On 2026-10-05 all other owned repositories were made private at the owner's request. Any earlier references to public source describe visibility at capture time. The portfolio no longer links visitors to those private repositories.

## Activity and language panels

`metrics/` SVGs are generated by `scripts/update_metrics.py`. Activity uses the unauthenticated public contribution calendar, refreshed by the repository workflow; the current streak permits an unfinished current day. Yearly statistics are limited to the fetched calendar, not lifetime records. The mobile heatmap shows 26 weeks. The language panel uses an explicitly dated aggregate snapshot from GitHub language bytes across owned project repositories, excluding this profile; no private names or contents are published. Language shares do not measure hours or proficiency. The snapshot stays fixed until explicitly remeasured with authorized access. All animation is decorative and respects reduced motion.
