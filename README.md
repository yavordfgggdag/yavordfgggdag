<div align="center">

<img src="assets/banner.svg" alt="Yavor — Websites. Software. Games. Built around your vision. Available for paid projects." width="100%" />

### Yavor Yakow · Product-minded developer

I build the interface, the logic behind it, and the connections that make it useful.<br>
My work includes native developer tools, community websites and operational software.

**Available for paid projects** · Based in Bulgaria

[Selected work](#selected-work) · [Services](#services) · [Technology](#technology) · [Contact](#contact)

</div>

## Selected work

<img src="assets/portfolio-signal.svg" alt="Selected work: native software, community websites and connected workflows." width="100%" />

<p align="center">
<a href="#before-i-deploy"><img src="assets/screens/before-i-deploy-preview.jpg" alt="Before I Deploy: real release checks and launch workflow. Open the case study below." width="49%" /></a>
<a href="#tlr-police-portal"><img src="assets/screens/police-dashboard-preview.jpg" alt="TLR Police Portal: real operations dashboard, with identities redacted. Open the case study below." width="49%" /></a>
</p>

**[01 — Before I Deploy](#before-i-deploy)** · Native macOS tooling<br>
**[02 — The Last Republic](#the-last-republic)** · Community website & application journey<br>
**[03 — TLR Police Portal](#tlr-police-portal)** · Staff operations & Discord integration

<sub>Actual application and website captures. Private identities are cropped or visibly redacted. Click any full-size image to inspect it.</sub>

## Before I Deploy

**Make release preparation understandable, from the first check to the next action.**

A native macOS application for reviewing local web projects, understanding warnings and preparing a preview or production release. I developed the SwiftUI interface, the Node.js command engine and the connections between project checks, hosting and cloud services.

<img src="assets/screens/before-i-deploy.jpg" alt="Before I Deploy running on macOS: a demo project with a Ready with warnings verdict, check controls and a step-by-step launch checklist." width="100%" />

**What is behind the screen**

- **One check pipeline:** Git state, secrets, dependencies, lint, types, build and hosting readiness, with results returned to the app as NDJSON events.
- **Release safeguards:** the engine checks for changed project fingerprints and requires explicit confirmation before production deployment.
- **A useful control centre:** project status, site monitoring, SSL information and a command palette for moving between tasks.
- **AI-assisted repair:** an implemented review-and-apply workflow for proposed file changes. Provider setup and service availability determine what can run.

**Built with:** Swift · SwiftUI · JavaScript · Node.js · Supabase · PostgreSQL · Deno Edge Functions

<img src="assets/bid-architecture.svg" alt="Architecture diagram: SwiftUI communicates with a Node.js engine through NDJSON. The engine handles local checks and connects to hosting and optional cloud services." width="100%" />

<details>
<summary><b>Explore the application — Mission Control & keyboard navigation</b></summary>

### Mission Control

<img src="assets/screens/bid-mission-control.jpg" alt="Live Mission Control showing a demo project, monitoring status and an HTTP 404 incident; this is a captured development state, not a success metric." width="100%" />

### Command palette

<img src="assets/screens/bid-command-palette.jpg" alt="Actual Before I Deploy command palette with Mission Control, Domains, Costs, Setup, AI, Settings and History actions." width="100%" />

</details>

<sub>Actively developed product. Screens show the installed application with a demo project; they do not imply a public release or that every external integration has been validated. Source is private.</sub>

[Discuss the product or a similar tool →](mailto:Fraisbg1@gmail.com?subject=Before%20I%20Deploy)

<img src="assets/section-divider.svg" alt="" width="100%" />

## The Last Republic

**A community website with a clear route from discovery to application.**

I developed the public web experience, rules pages and Discord-connected whitelist journey for a FiveM roleplay community. The interface brings the community identity, onboarding information and application entry into one site.

<a href="https://the-last-republic.netlify.app/"><img src="assets/screens/tlr-home.jpg" alt="The Last Republic live homepage: monochrome city illustration, large editorial typography, whitelist and Discord calls to action." width="100%" /></a>

**Built with:** TypeScript · Next.js · React · Tailwind CSS · Netlify<br>
**Implemented connections:** Discord sign-in and an application workflow with staff review.

[Visit the website →](https://the-last-republic.netlify.app/) · [View the application entry →](https://the-last-republic.netlify.app/whitelist)

<details>
<summary><b>See the public whitelist entry screen</b></summary>

<img src="assets/screens/tlr-whitelist.jpg" alt="Live whitelist entry explaining Discord sign-in, the exam and the decision process. No application has been submitted for this capture." width="100%" />

</details>

## TLR Police Portal

**Turn a community's staff structure into a usable operations workspace.**

An internal portal for the TLR roleplay police department. I developed the dashboard, searchable staff directory, rank hierarchy, handbook and management workflows for certificates, strikes and callsigns, with server-side access checks and audit records.

<a href="https://the-last-republic.netlify.app/police"><img src="assets/screens/police-dashboard.jpg" alt="Actual authenticated TLR Police Portal dashboard with handbook, radio codes, districts and roster widgets. Profile names and avatars are visibly redacted." width="100%" /></a>

**The engineering decision:** Discord membership events need a persistent connection. A separate Node.js bot handles the Gateway connection and synchronizes Discord-owned roster fields into Postgres. The Next.js website handles authorized management actions. Both use a shared role map.

**Built with:** TypeScript · Next.js · React · PostgreSQL / Neon · Drizzle ORM · Node.js · discord.js

<img src="assets/tlr-architecture.svg" alt="Architecture diagram: a persistent Discord bot synchronizes roster data to Postgres; the Next.js portal reads that data and handles operations with server-side permissions." width="100%" />

### Inside the portal

<img src="assets/screens/police-employees.jpg" alt="Live employee management screen with search, rank and department filters. Individual identities, badge details and personal records are fully redacted." width="100%" />

<details>
<summary><b>Open the gallery — rank hierarchy & interactive handbook</b></summary>

### Rank hierarchy

<img src="assets/screens/police-ranks.jpg" alt="Live rank hierarchy for the Commissioner's Office, Los Santos Police Department and Blaine County Sheriff's Office." width="100%" />

### Interactive handbook

<img src="assets/screens/police-handbook.jpg" alt="Live police handbook showing The Mission, chapter tabs, page controls and structured procedure content." width="100%" />

</details>

<details>
<summary><b>Play the short handbook navigation demo (animated GIF)</b></summary>

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/screens/police-handbook.jpg" />
  <img src="assets/screens/handbook-navigation.gif" alt="Recorded navigation through three real handbook pages: The Mission, Culture and Welcome to the LSPD. Static screenshot shown when reduced motion is supported." width="100%" />
</picture>

<sub>Three captured states from real page navigation, with pauses for readability. No interface or data has been fabricated.</sub>

</details>

[Open the portal →](https://the-last-republic.netlify.app/police) · Discord authentication and department membership required. Source is private.

<img src="assets/section-divider.svg" alt="" width="100%" />

## Services

**Custom development for businesses, creators and communities.**

- **Websites & online stores** — business websites, landing pages, storefronts, checkout and third-party integrations.
- **Web & desktop software** — applications, dashboards, administrative panels, customer portals and internal tools.
- **Discord, games & FiveM** — bots, community workflows, gameplay systems, server tools and connected interfaces.
- **APIs, automation & AI** — service integrations, webhooks, scripts, AI-assisted features and workflow automation.
- **Maintenance & continued development** — new features, bug fixes, interface improvements and release preparation.

These are available service areas. The case studies above show specific implemented work; the scope, technologies and deliverables for a new project are agreed individually.

## Technology

<img src="assets/technology-map.svg" alt="Technology used in the featured projects: Swift and SwiftUI for macOS; JavaScript, Node.js and NDJSON for the engine; TypeScript, React, Next.js and Tailwind for the web; Postgres, Drizzle, Supabase and discord.js for data and integrations." width="100%" />

**Native & developer tooling:** Swift / SwiftUI for the macOS app; JavaScript / Node.js for the engine; NDJSON for structured communication.

**Web & operations:** TypeScript / React / Next.js for TLR; Tailwind CSS for styling; PostgreSQL / Neon and Drizzle for the portal's data layer; discord.js for the persistent bot.

**Cloud services:** Supabase / PostgreSQL and Deno Edge Functions in Before I Deploy; Netlify for the public TLR website.

**Exploration:** additional game engines, cross-platform desktop approaches and new AI-assisted workflows. I distinguish experiments from the implemented work shown here.

## How I work

1. **Define the problem.** Identify the users, the workflow and what a useful first release needs to do.
2. **Design the whole path.** Connect the interface, data model, permissions and integrations.
3. **Build in reviewable steps.** Deliver working features and make decisions visible.
4. **Validate the release.** Check behaviour, failure states and deployment requirements.
5. **Keep improving.** Document the handoff, maintain the product and plan the next iteration.

## Contact

<img src="assets/work-together.svg" alt="Available for paid projects. What should we build next? A clear brief, a practical scope and a working product." width="100%" />

**Tell me the problem, the main features, your timeline and your budget range.**

- **Email:** [Fraisbg1@gmail.com](mailto:Fraisbg1@gmail.com)
- **Phone:** +359 898 634 678
- **Discord:** Fraisbg
- **Instagram:** [@y.yakowvw.sales](https://www.instagram.com/y.yakowvw.sales/)

<sub>Visual assets live in this repository. SVG motion respects reduced-motion preferences where supported. [About the screenshots](assets/README.md).</sub>
