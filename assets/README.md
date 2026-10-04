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
