## Color and motion revision

All 68 original Shields.io badges are stored locally in `journal/badges/` and composed into five bilingual responsive collections. Original brand colors and logos are retained. The new introduction, soft radial backgrounds, rotating dotted accents and moving card outlines are decorative. Labels remain still. `prefers-reduced-motion` disables CSS motion. Metric artwork remains static. No Discord screenshot from the latest message was included, as requested.

# Portfolio assets

## Engineering journal update — 5 October 2026

The current README composition leads with actual products, followed by the complete
language/tool collection, services, metrics, working process and contact details.
The original banner, original screenshots and previous SVG artwork remain in place.
Both language versions retain the same project, service and technology scope.

New artwork lives in `journal/` and is reproducible with
`python3 scripts/render_journal.py`. Its shared palette is midnight indigo
`#0B1020`, deep violet `#151632`, lilac `#B8A1FF`, ice blue `#83C9F4`,
seafoam `#73DFCA`, off-white `#EEF2FF` and muted text `#B2BED5`.
Architecture diagrams use static labels and slow signal motion with pauses.
The working-process line has a distinct, slower cycle. All new motion has a
`prefers-reduced-motion` fallback. No animation represents measured live activity.
The original banner's animation and source bytes are unchanged.

### Exact screenshot viewports

`journal/screens/*.svg` are self-contained presentation compositions containing
the **unchanged bytes** of the existing redacted JPEG captures. No product UI,
record, count or warning was generated or retouched. Desktop viewports omit the
former decorative headers so each project is titled once in Markdown. The same
quiet 1 px frame is used for all three lead images.

Narrow-screen sources are explicitly identified in both READMEs as details from
desktop captures, not screenshots of responsive product versions. Full originals
are linked next to each image. The mobile Police Portal detail shows radio codes;
all earlier redactions remain intact.

| Source JPEG | Desktop viewport (x, y, width, height) | Narrow viewport |
| --- | --- | --- |
| before-i-deploy.jpg | 28, 105, 1344, 934 | 48, 190, 680, 830 |
| police-dashboard.jpg | 28, 105, 1344, 738 | 610, 475, 377, 190 |
| client-education.jpg | 28, 105, 1344, 1139 | 170, 470, 1000, 742 |

### Metrics presentation

`journal/metrics/` reads the existing `data/activity.json` and fixed
`data/languages.json`, reusing the existing `stats()` function. The workflow first
refreshes the public calendar using the unchanged source script, then renders
the new presentation with `--metrics-only`. Existing workflow permissions and
schedule are unchanged. There is no new token or private-repository access.
Language bytes remain a fixed, explicitly dated snapshot; no recalculation from
private repositories is performed. New charts are static.

### Content retained and relocated

All 68 distinct entries from the original wider technology collection remain (plus Higgsfield, 69 in total)
visible as selectable text. Project-specific technology roles are added without
promoting exploratory tools to proven experience. The full service catalogue,
metric methodology, secondary galleries, community implementation and incomplete
Space Control experiment remain available in disclosures. Private repository
names are not needed in the new README copy. Old files and history are retained.

The main The Last Republic URL, current Police Portal entry and the driving
instructor site's URL/current screenshots remain unconfirmed. No substitute
interface is presented for them. The educational site and existing documentation
are the sources for its description; a new authenticated source-code audit was
not performed during this design update.

---

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

`community-platform.jpg` and `community-rules.jpg` are real browser screenshots of the unmodified community-site frontend (a separate repository, now private) running locally on 2026-10-05. Production Supabase configuration was overridden with empty environment values. No account was used; server addresses and status labels are repository defaults, not verified live claims. The profile does not link to the private source.

Space Control is listed as a source-only experiment because referenced CSS/JS assets are absent from the public checkout. No replacement interface was fabricated.

## Languages and client website

English lives in README.md; Bulgarian lives in README.bg.md. Local SVG link buttons connect the two GitHub views. The original banner and captured UI remain unchanged. `client-education.jpg` and `client-education-faq.jpg` were captured from https://pomoshtotpriyatel.com/ on 2026-10-05. The homepage crop excludes the presenter video and contact strip; FAQ capture follows a real click. No form was submitted. WordPress and WPForms are evidenced by public page assets and the form markup. The TLR main-site gallery was withdrawn pending the owner’s current URL; local community-site screenshots are explicitly distinguished from the current site.

## Studio visual system

The `studio/` directory contains original, repository-local SVG diagrams and chapter panels, plus a composition of existing genuine captures. CSS animations use slow orbits, paths and opacity changes; `prefers-reduced-motion` disables them. Manifesto and selected-work art have dedicated narrow-screen variants via `picture`. Real screenshots have not been replaced with generated interfaces. The original banner and contact panel remain intact.

On 2026-10-05 all other owned repositories were made private at the owner's request. Any earlier references to public source describe visibility at capture time. The portfolio no longer links visitors to those private repositories.

## Activity and language panels

`metrics/` SVGs are generated by `scripts/update_metrics.py`. Activity uses the unauthenticated public contribution calendar, refreshed by the repository workflow; the current streak permits an unfinished current day. Yearly statistics are limited to the fetched calendar, not lifetime records. The mobile heatmap shows 26 weeks. The language panel uses an explicitly dated aggregate snapshot from GitHub language bytes across owned project repositories, excluding this profile; no private names or contents are published. Language shares do not measure hours or proficiency. The snapshot stays fixed until explicitly remeasured with authorized access. All animation is decorative and respects reduced motion.

## Studio motion system (October 2026 upgrade)

`motion/` holds every new visual: hero, chapter dividers, project accents, animated architecture illustrations, technology panels, process, finale and footer, each in English and Bulgarian and with a narrow-screen variant served through `<picture>`. They are generated by `scripts/build_visuals.py` from `data/technologies.json` and `data/tech-icons.json`; regenerate them instead of editing the SVGs by hand.

- **Palette and typography** live in `scripts/profile_style.py` and are shared with the activity/language generator, so the daily workflow keeps the same design.
- **Motion contract:** the default render of every SVG is a complete static composition. Animation runs only under `prefers-reduced-motion: no-preference`; moving elements (`live`) have static stand-ins (`still`). Nothing blinks; highlights move sequentially, one element at a time.
- **Honesty:** orbits, light and pulses are decorative or explain the documented architecture. Architecture visuals are labelled as illustrations and never represent live activity or status.
- **Technologies:** all 68 technologies from the original badge collection are shown with their original badge colours. Logos come from Simple Icons 16.34.0 (CC0; trademarks belong to their owners). SQL, C#, PowerShell, Objective-C and OpenAI had no logo in the original badges and have no Simple Icons entry, so they are text tiles. F# and Cursor gained their official icons. A mint ring marks the 12 technologies verified in the featured products; the remaining ones are interests and possible project choices.
- **Framed captures:** `screens/framed/` contains the same genuine interface areas as `screens/`, re-framed by `scripts/frame_screens.py` with a per-project accent. The original presentation caption around each capture was removed so headings are not repeated; the interface pixels are unchanged. Originals stay in `screens/`.
- Earlier visuals (`studio/`, `contact.svg`, `technology-map.svg`, `development-flow.svg`, `section-divider.svg`, `work-*.jpg`, the original architecture diagrams) remain in the repository for history and rollback.
- Checks: `python3 scripts/test_profile.py` verifies image paths, English/Bulgarian parity, the 69 technologies, contacts, absence of remote widgets and private repository names, and the reduced-motion contract.

## Certificates

`motion/certificates-*.svg` and `motion/lessons-*.svg` are generated from `data/certificates.json` by `scripts/build_visuals.py`.

To add a certificate, append an entry to `featured` (title, issuer, Simple Icons slug or a short monogram, accent colour, `issued`, and `valid_until`/`period` when known), or add a lesson to a collection, then run `python3 scripts/build_visuals.py` and `python3 scripts/test_profile.py`. Lessons are de-duplicated by title. Original certificate files, certificate IDs and QR codes are intentionally not published.

## Live product scenes and display typography

`motion/scene-*.svg` place the genuine captures from `screens/` inside a drawn laptop or browser frame and cross-fade between them with a slow scroll. The captures are embedded as JPEG data URIs (no external requests); identities stay redacted exactly as in the originals. On narrow screens the README shows the static framed capture instead. Without motion, the first screen is shown.

Display headlines (hero, project names, finale, footer) use **Unbounded** (SIL Open Font License 1.1, `fonts/unbounded/`), outlined to SVG paths by `scripts/typeset.py` because GitHub images cannot load web fonts. The same words are always present in the SVG title/description and the README alt text.

Regenerating the visuals needs Pillow and fontTools (`pip install pillow fonttools`); the daily workflow only re-renders the activity panels and does not need them.

## Before I Deploy metrics

`motion/under-hood-*.svg` are generated from `data/bid-metrics.json`: aggregate counts measured on the private repository's main branch (5 Oct 2026) — non-blank lines per language, the eight-step check pipeline, engine commands, platforms, edge functions, templates and UI languages. "172 automated tests passing" is the result of running the engine suites that CI runs (119 + 53, 0 failed). The terminal shows the engine's real NDJSON event format (`step`, `log`, `result`) with illustrative values. No source code is published.

## The Last Republic (current site)

`screens/tlr/*.jpg` were captured on 5 Oct 2026 from the current The Last Republic codebase (Next.js 16) running locally: home, application path, rules hub, server rules and the Police Portal sign-in terminal. The Next.js development indicator was hidden; no data was changed. Discord sign-in is not configured locally, so no authenticated or personal data appears. `screens/framed/tlr-home.jpg` is the framed narrow-screen fallback. The whitelist flow illustration and the "Decisions in the code" notes follow the implementation and project documentation (exam timer and attempts, signed interactions, HMAC relay, role-ID authorization). The earlier green community-site captures are no longer shown.

## Bento overview and services

`motion/bento-*.svg` replaces the plain "Selected Work" table with a bento composition: real thumbnails of Before I Deploy, TLR Police Portal and The Last Republic, plus measured facts (tests, checks, lines of code, certificates, technologies). `motion/services-*.svg` presents the six service areas from `data/services.json` (the same wording as before). Both have narrow-screen variants and follow the reduced-motion contract.

## Certificate gallery

`assets/certificates/` holds an image of every certificate, rendered from the issued files: 6 featured certificates (`featured/`, numbered by importance) and the 129 unique Google Applied Digital Skills lessons (`lessons/`, duplicates removed). Completion IDs, certification codes, certificate IDs and QR codes are covered before publishing; names and dates are kept. `scripts/certificate_gallery.py` writes the "All 135 certificates" section, with every certificate behind its own click.
