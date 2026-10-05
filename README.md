<p align="center">
<a href="https://github.com/yyakowvw"><img src="assets/languages/en.svg" alt="English" width="146" height="42" /></a>
<a href="https://github.com/yyakowvw/yyakowvw/blob/main/README.bg.md"><img src="assets/languages/bg.svg" alt="Български" width="166" height="42" /></a>
</p>

<img src="assets/banner.svg" alt="Yavor — Websites. Software. Games. Built around your vision. Available for paid projects." width="100%" />

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/hero-en-mobile.svg" />
<img src="assets/motion/hero-en.svg" alt="Yavor Yakow, independent developer. Products with systems behind them: websites, online stores, web and desktop software, admin panels, Discord bots, games and FiveM, APIs and AI. Featured: Before I Deploy, TLR Police Portal, The Last Republic. Contact: Fraisbg1@gmail.com · Discord Fraisbg · Instagram @y.yakowvw.sales." width="100%" />
</picture>

<p align="center"><b><a href="#work">Work</a> · <a href="#services">Services</a> · <a href="#technology">Technology</a> · <a href="#certificates">Certificates</a> · <a href="#activity">Activity</a> · <a href="#process">Process</a> · <a href="#contact">Contact</a></b></p>

## 👋 Hi, I'm Yavor

I build digital products that connect design, code and real-world workflows. My work spans web development, custom software, Discord bots, games, FiveM systems, automation and developer tools.

**I take on paid development projects** — from a focused feature or a new website to a complete custom platform. I can help turn an early idea into a clear scope, build the product, connect its systems and prepare it for launch.

<a name="work"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-01-en-mobile.svg" />
<img src="assets/motion/divider-01-en.svg" alt="" width="100%" />
</picture>

## 🚀 Selected Work

<table>
<tr>
<td width="50%" valign="top">

### 🟣 [Before I Deploy](#before-i-deploy)
**Know before you ship.** A native macOS app that checks web projects before production: environments, dependencies, linting, types, tests, builds, security and configuration.

**Developer tools · Automation · Release readiness**

</td>
<td width="50%" valign="top">

### 🔵 [TLR Police Portal](#tlr-police-portal)
Internal management for employee profiles, departments, ranks, callsigns, certificates and strikes, with permissions and audit logs.

**Management software · Role-based access · Integrations**

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 🩷 [The Last Republic](#the-last-republic)
Connected gaming and community infrastructure bringing together FiveM, web applications, Discord, databases, staff tools and permissions.

**Full-stack systems · Gaming · Community infrastructure**

</td>
</tr>
</table>

Much of my project source code is private. This profile presents the work, the capabilities and the approach behind it.

<a name="before-i-deploy"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/project-bid-en-mobile.svg" />
<img src="assets/motion/project-bid-en.svg" alt="01 · Native macOS app" width="100%" />
</picture>


**Make release preparation understandable, from the first check to the next action.**

A native macOS application for reviewing local web projects, understanding warnings and preparing a preview or production release. **My contribution:** I developed the SwiftUI interface, the Node.js command engine and the connections between project checks, hosting and cloud services.

<picture>
<source media="(max-width: 600px)" srcset="assets/screens/framed/before-i-deploy.jpg" />
<img src="assets/motion/scene-bid-en.svg" alt="Before I Deploy running on macOS: a demo project with a Ready with warnings verdict, check controls and a step-by-step launch checklist." width="100%" />
</picture>

- **One check pipeline:** Git state, secrets, dependencies, lint, types, build and hosting readiness, with results returned to the app as NDJSON events.
- **Release safeguards:** the engine checks for changed project fingerprints and requires explicit confirmation before production deployment.
- **A useful control centre:** project status, site monitoring, SSL information and a command palette for moving between tasks.
- **AI-assisted repair:** an implemented review-and-apply workflow for proposed file changes. Provider setup and service availability determine what can run.

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/arch-bid-en-mobile.svg" />
<img src="assets/motion/arch-bid-en.svg" alt="Architecture illustration: the SwiftUI app sends commands to a Node.js engine and receives NDJSON events. One chain of checks — Git, secrets, dependencies, lint, types, build, hosting — ends at an explicit confirmation before production hosting. Project files and Keychain stay local; Supabase, Postgres and Deno Edge Functions are optional cloud services." width="100%" />
</picture>

**Built with:** Swift · SwiftUI · JavaScript · Node.js · Supabase · PostgreSQL · Deno Edge Functions

<details>
<summary><b>Explore the application — Mission Control & keyboard navigation</b></summary>

### Mission Control

<img src="assets/screens/framed/bid-mission-control.jpg" alt="Live Mission Control showing a demo project, monitoring status and an HTTP 404 incident; this is a captured development state, not a success metric." width="100%" />

### Command palette

<img src="assets/screens/framed/bid-command-palette.jpg" alt="Actual Before I Deploy command palette with Mission Control, Domains, Costs, Setup, AI, Settings and History actions." width="100%" />

</details>

<sub>Actively developed product. Screens show the installed application with a demo project; they do not imply a public release or that every external integration has been validated. Source is private.</sub>

[Discuss the product or a similar tool →](mailto:Fraisbg1@gmail.com?subject=Before%20I%20Deploy)

<a name="tlr-police-portal"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/project-police-en-mobile.svg" />
<img src="assets/motion/project-police-en.svg" alt="02 · FiveM community operations" width="100%" />
</picture>


**Turn a community's staff structure into a usable operations workspace.**

An internal portal for the TLR roleplay police department. **My contribution:** I developed the dashboard, searchable staff directory, rank hierarchy, handbook and management workflows for certificates, strikes and callsigns, with server-side access checks and audit records.

<picture>
<source media="(max-width: 600px)" srcset="assets/screens/framed/police-dashboard.jpg" />
<img src="assets/motion/scene-police-en.svg" alt="Actual authenticated TLR Police Portal dashboard with handbook, radio codes, districts and roster widgets. Profile names and avatars are visibly redacted." width="100%" />
</picture>

**The engineering decision:** Discord membership events need a persistent connection. A separate Node.js bot handles the Gateway connection and synchronizes Discord-owned roster fields into Postgres. The Next.js website handles authorized management actions. Both use a shared role map.

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/arch-tlr-en-mobile.svg" />
<img src="assets/motion/arch-tlr-en.svg" alt="Architecture illustration: a persistent Discord Gateway bot synchronizes roster data to Postgres; the Next.js portal reads that data and performs authorized actions after server-side permission checks, writing audit records. Bot and portal share one role map; staff sign in with Discord." width="100%" />
</picture>

**Built with:** TypeScript · Next.js · React · PostgreSQL / Neon · Drizzle ORM · Node.js · discord.js

<details>
<summary><b>Open the gallery — rank hierarchy & interactive handbook</b></summary>

### Rank hierarchy

<img src="assets/screens/framed/police-ranks.jpg" alt="Live rank hierarchy for the Commissioner's Office, Los Santos Police Department and Blaine County Sheriff's Office." width="100%" />

### Interactive handbook

<img src="assets/screens/framed/police-handbook.jpg" alt="Live police handbook showing The Mission, chapter tabs, page controls and structured procedure content." width="100%" />

</details>

<details>
<summary><b>Play the short handbook navigation demo (animated GIF)</b></summary>

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/screens/police-handbook.jpg" />
  <img src="assets/screens/handbook-navigation.gif" alt="Recorded navigation through three real handbook pages: The Mission, Culture and Welcome to the LSPD. Static screenshot shown when reduced motion is supported." width="100%" />
</picture>

<sub>Three captured states from real page navigation, with pauses for readability. No interface or data has been fabricated.</sub>

</details>

<sub>Portal captures from the earlier review. Discord authentication and department membership required. Current entry URL is being confirmed; source is private.</sub>

<a name="the-last-republic"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/project-tlr-en-mobile.svg" />
<img src="assets/motion/project-tlr-en.svg" alt="03 · Community infrastructure" width="100%" />
</picture>


**Community infrastructure connecting the website, Discord and operational tools.**

**My contribution:** the public interface, rules and Discord-connected application journeys for the FiveM community.

<sub>The current main-site URL and version are being confirmed. Earlier homepage captures are not presented as the current website.</sub>

<a name="services"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-02-en-mobile.svg" />
<img src="assets/motion/divider-02-en.svg" alt="" width="100%" />
</picture>

## 💼 What You Can Hire Me For

<table>
<tr>
<td width="50%" valign="top">

### 🌐 Websites & Online Businesses
Business websites, landing pages, portfolios, online stores, booking interfaces, content-driven sites and complete website redesigns.

**Responsive design · UI/UX · Integrations · Performance**

</td>
<td width="50%" valign="top">

### ⚙️ Custom Software & Platforms
Web applications, desktop utilities, dashboards, admin panels, customer portals, internal tools and business management systems.

**Frontend · Backend · Databases · Authentication**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💬 Discord Bots & Communities
Custom bots, slash commands, ticket systems, moderation, roles, notifications, logging, community workflows and connected dashboards.

**Bot development · APIs · Automation · Server integrations**

</td>
<td width="50%" valign="top">

### 🎮 Games & FiveM Systems
Custom games and prototypes, gameplay systems, server resources, NUI interfaces, jobs, inventories, staff tools and community infrastructure.

**Game logic · Client/server systems · Persistence · Tooling**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🤖 Automation & AI Integrations
Workflow automation, repetitive-task scripts, AI-powered features, assistant integrations, data-processing utilities and connected services.

**APIs · Webhooks · Scripting · AI-assisted workflows**

</td>
<td width="50%" valign="top">

### 🛠️ Improvements & Ongoing Development
New features, bug fixes, refactoring, performance improvements, migrations, interface refreshes, testing and deployment preparation.

**Existing projects · Technical cleanup · Maintenance**

</td>
</tr>
</table>

**Offered · proven · exploring.** The cards above are services I offer. The projects above show the experience already implemented. The technology panels below separate tools used in those products from wider interests.

<details>
<summary><b>Explore the full development service catalogue</b></summary>

| Development area | Project types and scope |
| :--- | :--- |
| 🌍 **Websites** | Company sites, personal brands, portfolios, landing pages, campaign pages, directories and content sites |
| 🛒 **E-commerce** | Product catalogues, storefronts, checkout integrations, customer accounts and order-management tools |
| 📅 **Booking & Scheduling** | Appointment flows, availability interfaces, reservation systems, reminders and calendar integrations |
| 🧩 **Web Applications** | SaaS interfaces, membership platforms, customer portals, collaboration tools and interactive dashboards |
| 🖥️ **Desktop Software** | Custom utilities, launchers, productivity tools, installers and desktop interfaces |
| 📱 **Mobile Experiences** | Responsive mobile interfaces, progressive web apps and mobile-focused prototypes |
| 🎨 **Frontend & UI/UX** | Interface design and implementation, component libraries, design systems, animation and accessibility improvements |
| ⚙️ **Backend Systems** | Application logic, API services, background tasks, validation and integrations |
| 🗄️ **Databases** | Schema design, migrations, import/export tools, persistence, reporting and query optimization |
| 🔐 **Accounts & Permissions** | Sign-in flows, user profiles, role-based access, staff permissions and audit trails |
| 🔌 **APIs & Integrations** | Third-party services, webhooks, payment-provider integrations, notifications and connected workflows |
| 💬 **Discord Development** | Bots, commands, moderation, tickets, role systems, logs, dashboards and game-server connections |
| 🎮 **Games & Interactive Projects** | Game prototypes, gameplay features, browser games, interfaces and supporting tools |
| 🚓 **FiveM Development** | Custom resources, NUI, jobs, police/government systems, administration and database-connected features |
| 🏢 **Business Software** | CRM-style tools, employee management, inventory workflows, operations panels and custom internal systems |
| 🤖 **AI Features** | AI API integrations, assistants, content workflows and AI-supported product features |
| 🔁 **Automation & Scripting** | Task automation, file processing, data transformation, notifications and service orchestration |
| 🧰 **Developer Tools** | CLI tools, project validators, release utilities, debugging tools and workflow helpers |
| 🧪 **Testing & Quality** | Test setup, regression checks, linting, type checking, build validation and bug investigation |
| 🚀 **Deployment & Maintenance** | Environment setup, CI/CD workflows, release preparation, monitoring integrations and ongoing improvements |

**Every project is scoped individually.** Features, platform support, integrations, delivery time and pricing depend on the requirements we agree on.

</details>

> **Have something different in mind?** I also consider custom development outside this list. Start with the problem, the users and what a successful result should do.

<a name="technology"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-03-en-mobile.svg" />
<img src="assets/motion/divider-03-en.svg" alt="" width="100%" />
</picture>

## 🌈 Languages & Technology

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-used-en-mobile.svg" />
<img src="assets/motion/stack-used-en.svg" alt="Used in the featured products. Before I Deploy: Swift, SwiftUI, JavaScript, Node.js, Supabase, PostgreSQL, Deno Edge Functions. TLR Police Portal: TypeScript, Next.js, React, Tailwind CSS, Drizzle, Neon Postgres, discord.js." width="100%" />
</picture>

The 68 technologies below are the original technology collection: additional interests and possible project choices. It is not a claim of completed products or equal experience with every tool. A **mint ring** marks the tools verified in the products above.

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-tools-en-mobile.svg" />
<img src="assets/motion/stack-tools-en.svg" alt="Additional Tools & Interests, 13: TypeScript (used in featured products), JavaScript (used), Python, Lua, HTML5 (used), CSS3, SQL, Node.js (used), Astro, MySQL, MariaDB, Git, GitHub." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-languages-en-mobile.svg" />
<img src="assets/motion/stack-languages-en.svg" alt="Wider Programming Language Ecosystem, 27: C, C++, C#, Java, Kotlin, Swift (used in featured products), Go, Rust, PHP, Ruby, Dart, Scala, R, Bash, PowerShell, Elixir, Erlang, Haskell, Clojure, F#, Julia, Zig, Solidity, GDScript, Objective-C, Perl, OCaml." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-web-en-mobile.svg" />
<img src="assets/motion/stack-web-en.svg" alt="Web & Application Ecosystem, 10: React (used in featured products), Next.js (used), Vue.js, Svelte, Vite (used), Tailwind CSS (used), Express, Electron, Flutter, .NET." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-data-en-mobile.svg" />
<img src="assets/motion/stack-data-en.svg" alt="Data, Infrastructure & Delivery, 10: PostgreSQL (used in featured products), SQLite, MongoDB, Redis, Docker, Linux, macOS (used), Netlify, GitHub Actions, NGINX." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-games-en-mobile.svg" />
<img src="assets/motion/stack-games-en.svg" alt="Games, Communities & AI, 8: Discord (used in featured products), FiveM, Godot, Unity, Unreal Engine, OpenAI, Claude, Cursor." width="100%" />
</picture>

<sub>The right stack depends on the product; the panels do not imply equal specialization in every language. Specific tools and implementation scope are agreed for each engagement. Logos: original brand colours via <a href="https://simpleicons.org">Simple Icons</a> (CC0); SQL, C#, PowerShell, Objective-C and OpenAI appear as text tiles, as in the original badges.</sub>

<a name="certificates"></a>

## 🎓 Certificates

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/certificates-en-mobile.svg" />
<img src="assets/motion/certificates-en.svg" alt="Certificates: Gemini Certified Educator (Google for Education, valid until 23 Jul 2029); AI-Powered Performance Ads (Google Ads, valid until 21 Jul 2027); Digital Marketing Certified (HubSpot Academy, valid until 23 Aug 2027); Digital Marketing Specialist (Advance Academy, Feb–Apr 2026); Fundamentals of Digital Marketing (Google, 27 Jul 2026); Intro to Gemini badge (Google AI Educator Series, Foundational)." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/lessons-en-mobile.svg" />
<img src="assets/motion/lessons-en.svg" alt="129 Google Applied Digital Skills lessons completed 23–27 Jul 2026: Creative & research 47, Google Workspace 38, Career & professional 21, Data & logic 13, AI & digital safety 10." width="100%" />
</picture>

<details>
<summary><b>All 129 Google Applied Digital Skills lessons</b></summary>

**Creative & research · 47**<br>
Build a Logo to Express Who You Are · Create a Brochure · Create a Collaborative Study Guide · Create a Community My Map · Create a Crossword Puzzle · Create a Digital Picture Book · Create a Digital Postcard · Create a Flyer for a Juneteenth Celebration · Create a Guide to an Area · Create a Presentation "All About a Topic" · Create a Scrapbook · Create a Slogan for Earth Day · Create a Travel Brochure for an Exoplanet · Create a Vision Board · Create an Annotated Playlist · Design a Poster About You · Design a Website to Promote a Project · Design and Share a Digital Badge · Explore a Topic: Celebrate Black History · Explore a Topic: Celebrate Latinx History · Explore a Topic: Earth Day · Explore a Topic: Equal Access to Technology · Explore a Topic: Innovators · Explore a Topic: Technology at Work · Explore a Topic: Technology's Role in Current Events · Explore a Topic: Women's History · Explore the History of Humankind in Kenya · Go on a Scavenger Hunt Through Italy · Learn New Vocabulary with Flash cards · Make Art Inspired by Frida Kahlo and Mexico · Make Your Own Space Shuttle Adventure · Make a Promotional Flyer · Memorize Facts with a Visual Mnemonic · Organize Your Time with a Digital Agenda · Plan and Promote an Event · Present Your Ideas for Classroom Expectations · Quiz Your Classmates About the Palace of Versailles · Research and Develop a Topic · Respond to a Question in Google Classroom · Schedule Emails for Goal-Setting · Take Notes in a Table · Welcome New Students with a Presentation · Write Effectively for Your Audience · Write a Press Release · Write a Story Using Emojis · Write an If-Then Adventure Story · Write the Lyrics for a Song

**Google Workspace · 38**<br>
Annotate Text in Google Docs · Create Papel Picado in Google Slides · Create Quizzes in Google Forms · Create a Clickable Map in Google Slides · Create a Collage in Google Drawings · Create a Comic Strip in Google Drawings · Create a Meme with Google Drawings · Create a Mind Map in Google Drawings · Create a Personal Timeline in Google Drawings · Create a Photo Journal in Google Docs · Create a Schedule to Meet Your Goals · Create a Virtual Family Reunion in Google Slides · Create an Animation in Google Slides · Design an Infographic in Google Drawings · Gmail for Beginners · Google Calendar for Beginners · Google Docs for Beginners · Google Drive for Beginners · Google Meet for Beginners · Google Search for Beginners · Google Sheets for Beginners · Google Workspace: Docs - Part 1 · Google Workspace: Docs - Part 2 · Google Workspace: Drive · Google Workspace: Gmail · Google Workspace: Sheets - Part 1 · Google Workspace: Sheets - Part 2 · Google Workspace: Sheets - Part 3 · Google Workspace: Slides - Part 1 · Google Workspace: Slides - Part 2 · Google Workspace: Slides - Part 3 · Introduce Yourself in Google Slides · Make Art with Google Sheets · Make Pop Art in Google Drawings · Manage Your Time With Google Sheets · Show Appreciation with Google Slides · Track Due Dates and Tasks in Gmail · Use Drive to Organize Files

**Career & professional · 21**<br>
Ask Someone to Be a Reference · Ask for Feedback · Build Your Professional Brand · Build Your Professional Network · Build a Portfolio with Google Sites · Create a Resume in Google Docs · Draft an Application Essay · Explore Careers by Interviewing Professionals · Introduce Yourself to Potential Employers · Organize College Applications in Google Sheets · Organize College Information in Google Sheets · Prepare for Your First Day of Work · Prepare for a College Interview · Prepare for the FAFSA · Research Career Paths · Research and Interview a Person From History · Search for Colleges Online · Search for Scholarships · Search for a Part-Time or Summer Job · Track Graduation Requirements · Write a Cover Letter for Your First Job

**Data & logic · 13**<br>
Analyze Data from Images in Google Earth Engine · Calculate Percentages in Google Sheets · Calculate Probability with Google Sheets · Code a Joke-Telling Talkbot · Create a Budget in Google Sheets · Create a Guessing Game · Find the Mean, Median, or Mode of a Data Set · Make a Flowchart · Make a Word Game · Pick the Next Box Office Hit · Program a Progress Bar · Wage a Sea Battle with Google Sheets · Work with Fractions In Google Sheets

**AI & digital safety · 10**<br>
Avoid Online Scams · Build Healthy Digital Habits · Create a Responsible Blog with Google Sites · Create and Safeguard Passwords · Discover AI in Daily Life · Evaluate Credibility of Online Sources · Explore a Topic: Generative AI · Explore a Topic: Technology, Ethics, and Security · Identify Cyberbullying · Understand Your Digital Footprint

</details>

<sub>Original certificate files are kept privately; certificate IDs and verification details are available on request.</sub>

<a name="activity"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-04-en-mobile.svg" />
<img src="assets/motion/divider-04-en.svg" alt="" width="100%" />
</picture>

## 📊 Activity & language mix

<picture>
<source media="(max-width: 600px)" srcset="assets/metrics/activity-en-mobile.svg" />
<img src="assets/metrics/activity-en.svg" alt="Contributions, active days, current and longest streak, last contribution and contribution calendar." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/metrics/languages-en-mobile.svg" />
<img src="assets/metrics/languages-en.svg" alt="Languages by aggregate code volume across project repositories, including private projects, without repository names or contents." width="100%" />
</picture>

<details>
<summary><b>How these numbers are calculated</b></summary>

Activity refreshes daily from the public GitHub contribution calendar. Contributions are not just commits and do not measure hours worked. “Last contribution” is the last active calendar day, not the last login. GitHub may update the calendar with a delay.

The current streak counts consecutive active days ending today, or yesterday when today has no contribution yet. Longest streak, contribution totals and active days refer to the displayed annual window. The mobile heatmap shows the last 26 weeks; headline totals still use the annual window.

Language shares are a separate 2026-10-05 snapshot of GitHub-reported code bytes, including private projects and excluding this profile repository. They do not measure frequency, time or proficiency. The language snapshot is not refreshed automatically: the public workflow has no access to private code.

[GitHub contribution rules](https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference) · [Metrics source](scripts/update_metrics.py)

</details>

<a name="process"></a>

## 🧭 From Your Idea to a Working Product

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/process-en-mobile.svg" />
<img src="assets/motion/process-en.svg" alt="01 Discover: understand your goals, users and requirements. 02 Design: define the interface, architecture and scope. 03 Build: develop features and connect the systems. 04 Validate: test behavior, fix issues and check readiness. 05 Launch: deploy, document and plan the next improvements." width="100%" />
</picture>

### What Matters in My Work

**🎯 Purposeful design** — interfaces and features built around the people using them.<br>
**🧱 Clear architecture** — understandable code and systems that can evolve.<br>
**🔐 Thoughtful permissions** — validation, access control and sensible defaults.<br>
**🧪 Practical quality checks** — testing, diagnostics and validation before release.<br>
**🔁 Useful automation** — fewer repetitive steps and more consistent workflows.<br>
**🤝 Clear project scope** — agreed requirements, deliverables and expectations.

<a name="contact"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-05-en-mobile.svg" />
<img src="assets/motion/divider-05-en.svg" alt="" width="100%" />
</picture>

## 📬 Let's Talk About Your Project

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/finale-en-mobile.svg" />
<img src="assets/motion/finale-en.svg" alt="Available for paid projects. What should we build next? A website, a custom tool, a bot or your next big idea." width="100%" />
</picture>

<p align="center">
<a href="mailto:Fraisbg1@gmail.com"><img src="assets/motion/contact-mail-en.svg" alt="Email Fraisbg1@gmail.com" height="46" /></a>
<img src="assets/motion/contact-discord-en.svg" alt="Discord: Fraisbg" height="46" />
<a href="https://www.instagram.com/y.yakowvw.sales/"><img src="assets/motion/contact-instagram-en.svg" alt="Instagram @y.yakowvw.sales" height="46" /></a>
</p>

<p align="center"><b>Available for paid websites, software, Discord bots and games.</b><br>
Send your idea, the main features, timeline and budget — we will define the scope and a quote together.</p>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/footer-en-mobile.svg" />
<img src="assets/motion/footer-en.svg" alt="Websites · Software · Bots · Games · Automation. Your idea. A clear plan. Software that works. Build · Test · Verify · Deploy · Improve." width="100%" />
</picture>
