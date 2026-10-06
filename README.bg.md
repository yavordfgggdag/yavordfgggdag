<p align="center">
<a href="https://github.com/yyakowvw"><img src="assets/languages/en.svg" alt="English" width="146" height="42" /></a>
<a href="https://github.com/yyakowvw/yyakowvw/blob/main/README.bg.md"><img src="assets/languages/bg.svg" alt="Български" width="166" height="42" /></a>
</p>

<img src="assets/banner.svg" alt="Явор — сайтове, софтуер и игри, създадени около вашата идея. Приемам платени поръчки." width="100%" />

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/hero-bg-mobile.svg" />
<img src="assets/motion/hero-bg.svg" alt="Явор (Yavor Yakow), независим разработчик. Продукти със системи зад тях: сайтове, онлайн магазини, уеб и настолен софтуер, админ панели, Discord ботове, игри и FiveM, API и AI. Избрано: Before I Deploy, TLR Police Portal, The Last Republic. Контакт: Fraisbg1@gmail.com · Discord Fraisbg · Instagram @y.yakowvw.sales." width="100%" />
</picture>

<p align="center"><b><a href="#проекти">Проекти</a> · <a href="#услуги">Услуги</a> · <a href="#технологии">Технологии</a> · <a href="#сертификати">Сертификати</a> · <a href="#активност">Активност</a> · <a href="#процес">Процес</a> · <a href="#контакт">Контакт</a></b></p>

## 👋 Здравейте, аз съм Явор

Създавам дигитални продукти, които свързват дизайн, код и реални работни процеси. Работя по уеб приложения, индивидуален софтуер, Discord ботове, игри, FiveM системи, автоматизации и инструменти за разработчици.

**Приемам платени поръчки** — от конкретна функционалност или нов сайт до цялостна платформа. Помагам с уточняването на обхвата, разработката, интеграциите и подготовката за публикуване.

<a name="проекти"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-01-bg-mobile.svg" />
<img src="assets/motion/divider-01-bg.svg" alt="" width="100%" />
</picture>

## 🚀 Избрани проекти

<a href="#before-i-deploy"><picture>
<source media="(max-width: 600px)" srcset="assets/motion/bento-bg-mobile.svg" />
<img src="assets/motion/bento-bg.svg" alt="Избрана работа накратко: Before I Deploy, нативно macOS приложение със 172 минаващи теста, 8 проверки и 3 платформи; TLR Police Portal, състав, звания и наръчник, свързани с Discord, с достъп по ID на роля; The Last Republic, сайт, правила и изпит с решения в Discord с 23 API маршрута; 42.6k реда код в Before I Deploy; 6 сертификата и 129 Google урока; 68 технологии, 12 в готови продукти; свободен за платени проекти на Fraisbg1@gmail.com." width="100%" />
</picture></a>

Голяма част от изходния код е частен. Тук представям конкретната работа, техническите решения и начина си на работа.

<a name="before-i-deploy"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/project-bid-bg-mobile.svg" />
<img src="assets/motion/project-bid-bg.svg" alt="01 · Нативно macOS приложение" width="100%" />
</picture>


**Ясна подготовка за публикуване — от първата проверка до следващото действие.**

Нативно приложение за macOS за преглед на локални уеб проекти, разбиране на предупрежденията и подготовка на тестова или продукционна версия. **Моят принос:** разработих SwiftUI интерфейса, командния Node.js модул и връзките между проверките, хостинга и облачните услуги.

<picture>
<source media="(max-width: 600px)" srcset="assets/screens/framed/before-i-deploy.jpg" />
<img src="assets/motion/scene-bid-bg.svg" alt="Работещ Before I Deploy на macOS: демонстрационен проект с предупреждения, проверки и списък със стъпки за публикуване." width="100%" />
</picture>

- **Общ процес за проверки:** Git, тайни ключове, зависимости, статичен анализ, типове, компилация, качество на сайта и готовност на хостинга. Резултатите стигат до приложението като NDJSON събития.
- **Защити при публикуване:** проверка дали файловете са променени след анализа и изрично потвърждение преди продукционно публикуване.
- **Център за управление:** състояние на проектите, наблюдение на сайтове, SSL информация и командна палитра.
- **AI помощ при поправки:** преглед и прилагане на предложени промени. Работата зависи от настройката на доставчика и достъпността на услугите.

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/arch-bid-bg-mobile.svg" />
<img src="assets/motion/arch-bid-bg.svg" alt="Илюстрация на архитектурата: SwiftUI приложението изпраща команди към Node.js модул и получава NDJSON събития. Една верига от проверки — Git, тайни, зависимости, lint, типове, build, хостинг — завършва с изрично потвърждение преди продукционно публикуване. Файловете и Keychain остават локално; Supabase, Postgres и Deno Edge Functions са облачни услуги по избор." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/under-hood-bg-mobile.svg" />
<img src="assets/motion/under-hood-bg.svg" alt="Before I Deploy под капака, измерено на 5 окт 2026: 42.6k реда код, 172 автоматични теста минават, 8 проверки в една верига, 54 команди в engine-а, 3 платформи, 5 Edge функции, 20 шаблона за сайтове, 2 езика на интерфейса; състав на кода JavaScript 17.8k, Swift 15.1k, TypeScript 5.4k, SQL 3.3k реда; и реалният формат на NDJSON събитията от engine-а към приложението." width="100%" />
</picture>

**Решения в кода**

- **Човек одобрява автоматичните проверки.** Наблюдението на файлове пуска скриптовете на проекта само докато отпечатъкът на проекта съвпада с одобрения от човек. След всяка промяна — от AI, git pull или някой друг — следващата проверка се пуска от човек.
- **Тайните остават в системния keychain:** macOS Keychain, Windows Credential Manager, Linux Secret Service.
- **Един engine, три нативни обвивки:** SwiftUI на macOS, Tauri с общ уеб интерфейс на Windows и Linux. Node.js модулът работи като отделен процес и говори NDJSON.
- **Тестван като продукт:** тестовете създават временни проекти с изолирани настройки и симулирани услуги и се пускат в CI.

<sub>Общите числа са измерени в главния клон на 5 окт 2026; кодът остава частен.</sub>

**Технологии:** Swift · SwiftUI · JavaScript · Node.js · Supabase · PostgreSQL · Deno Edge Functions

<details>
<summary><b>Разгледайте приложението — Mission Control и командна палитра</b></summary>

### Mission Control

<img src="assets/screens/framed/bid-mission-control.jpg" alt="Реален Mission Control с демонстрационен проект и HTTP 404 инцидент. Заснето състояние по време на разработка." width="100%" />

### Командна палитра

<img src="assets/screens/framed/bid-command-palette.jpg" alt="Командна палитра с достъп до Mission Control, домейни, разходи, настройки, AI и история." width="100%" />

</details>

<sub>Продукт в активно развитие. Снимките са от инсталираното приложение с демонстрационен проект и не означават публично издание или проверка на всяка външна интеграция. Кодът е частен.</sub>

[Обсъдете продукта или подобен инструмент →](mailto:Fraisbg1@gmail.com?subject=Before%20I%20Deploy)

<a name="tlr-police-portal"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/project-police-bg-mobile.svg" />
<img src="assets/motion/project-police-bg.svg" alt="02 · Операции за FiveM общност" width="100%" />
</picture>


**Структурата на екипа, превърната в работно пространство.**

Вътрешен портал за полицейския отдел на TLR. **Моят принос:** разработих табло, търсачка на служители, йерархия на званията, наръчник и управление на сертификати, наказания и позивни, със сървърни проверки на правата и журнал на действията.

<picture>
<source media="(max-width: 600px)" srcset="assets/screens/framed/police-dashboard.jpg" />
<img src="assets/motion/scene-police-bg.svg" alt="Заснето табло на TLR Police Portal с наръчник, радиокодове, райони и състав. Имената и аватарите са скрити." width="100%" />
</picture>

**Техническо решение:** събитията за членство в Discord изискват постоянна връзка. Отделен Node.js бот поддържа Gateway връзката и синхронизира данните за състава в Postgres. Next.js сайтът обработва разрешените административни действия. Двата компонента използват обща карта на ролите.

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/arch-tlr-bg-mobile.svg" />
<img src="assets/motion/arch-tlr-bg.svg" alt="Илюстрация на архитектурата: постоянен Discord Gateway бот синхронизира състава в Postgres; Next.js порталът чете данните и изпълнява разрешени действия след проверка на правата на сървъра, като записва журнал. Ботът и порталът използват обща карта на ролите; служителите влизат с Discord." width="100%" />
</picture>

**Технологии:** TypeScript · Next.js · React · PostgreSQL / Neon · Drizzle ORM · Node.js · discord.js

<details>
<summary><b>Отворете галерията — звания и интерактивен наръчник</b></summary>

### Йерархия на званията

<img src="assets/screens/framed/police-ranks.jpg" alt="Реална страница със званията на полицейските структури в TLR." width="100%" />

### Интерактивен наръчник

<img src="assets/screens/framed/police-handbook.jpg" alt="Реален наръчник с глави, управление на страниците и структурирани процедури." width="100%" />

</details>

<details>
<summary><b>Кратка демонстрация на навигацията в наръчника — GIF</b></summary>

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/screens/police-handbook.jpg" />
  <img src="assets/screens/handbook-navigation.gif" alt="Три реално заснети страници на наръчника при навигация. При поддръжка на намалено движение се показва статична снимка." width="100%" />
</picture>

<sub>Три състояния от реална навигация с паузи за четене. Интерфейсът и данните не са измислени.</sub>

</details>

<sub>Снимки от предишната проверка на портала. Достъпът изисква Discord вход и членство в отдела. Актуалната връзка се уточнява; кодът е частен.</sub>

<a name="the-last-republic"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/project-tlr-bg-mobile.svg" />
<img src="assets/motion/project-tlr-bg.svg" alt="03 · The Last Republic · общностна инфраструктура" width="100%" />
</picture>

**Официалният сайт и защитена платформа за whitelisted FiveM roleplay общност.**

**Моят принос:** една Next.js система за публичния сайт, правилата, изпит с таймер за whitelist с кандидатури, преглеждани в Discord, и защитения полицейски портал.

<picture>
<source media="(max-width: 600px)" srcset="assets/screens/framed/tlr-home.jpg" />
<img src="assets/motion/scene-tlr-bg.svg" alt="The Last Republic, актуален сайт: кинематографична начална страница с град от линии, път до кандидатстване, илюстрирани правила, правилник с търсене и терминалът за вход в полицейския портал." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/arch-whitelist-bg-mobile.svg" />
<img src="assets/motion/arch-whitelist-bg.svg" alt="Път на кандидатурата: вход с Discord, двучасов изпит с три опита, кандидатура в Postgres, постоянно свързан Discord бот с бутони за приемане и отказ, решение на екипа с причина, подписано с HMAC препращане към сайта и публикация плюс лично съобщение до кандидата. Достъпът до полицейския портал се проверява по ID на ролята при всяка заявка и се отказва при грешка." width="100%" />
</picture>

**Решения в кода**

- **Достъп по ID на ролята при всяка заявка.** Полицейският портал пита Discord за текущите роли на сървъра, сравнява само ID-та — никога имена — и отказва достъп при всяка грешка.
- **Всяко входящо действие е подписано.** Действията от Discord се проверяват с подписа на Discord; тъй като Discord позволява един канал за действия на приложение, постоянно свързаният бот препраща решенията към сайта с HMAC-SHA256 подпис и часови прозорец.
- **Постоянните връзки са извън serverless.** Сайтът работи в Netlify, а връзките с Discord Gateway — в постоянно работещ бот и Cloudflare Durable Object.
- **Решенията са документирани:** 4 архитектурни решения (ADR) и 21 проектни документа.

**Технологии:** TypeScript · Next.js 16 · React 19 · Tailwind CSS 4 · Drizzle ORM · Neon Postgres · Netlify · discord-interactions · discord.js · Cloudflare Workers

<sub>22 страници · 23 API маршрута · 4 миграции на базата · 11 автоматични теста минават. Заснето от актуалния код, стартиран локално на 5 окт 2026; входът с Discord не е настроен локално. Кодът е частен.</sub>

<a name="readme-studio"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/project-studio-bg-mobile.svg" />
<img src="assets/motion/project-studio-bg.svg" alt="04 · readme-studio · отворен код" width="100%" />
</picture>

**Двигателят с отворен код зад стила на този профил: анимиран двуезичен GitHub README от един JSON файл.**

<a href="https://github.com/yyakowvw/readme-studio">
<picture>
<source media="(max-width: 600px)" srcset="assets/studio/readme-studio-bg-mobile.svg" />
<img src="assets/studio/readme-studio-bg.svg" alt="readme-studio — вашият GitHub профил, в движение. Чист SVG, нула JavaScript, уважава намаленото движение." width="100%" />
</picture>
</a>

- **Девет анимирани компонента** с варианти от 1200 px и 600 px, четири теми, 174 вградени икони и заглавия с шрифта Unbounded, превърнати в SVG контури (латиница + кирилица).
- **Работи в защитения преглед на GitHub:** без скриптове и външни заявки, цялото движение е в `prefers-reduced-motion`. Проверка преглежда всеки файл преди публикуване.
- **Една команда, нула код:** `curl … | bash` (или двоен клик на macOS и Windows) задава няколко въпроса, изгражда профила, отваря преглед и го публикува в GitHub. GitHub Action го обновява при всяка промяна; 17 теста и CI пазят резултата възпроизводим.

<img src="assets/video/readme-studio-demo-bg.webp" alt="60-секундно демо: една команда в терминала, няколко отговора и готов анимиран GitHub профил." width="100%" />

<p align="center"><sub>🎬 <b>Вижте как работи</b>: истинско пускане — от една команда до готов профил за 60 секунди.</sub></p>

**Създадено с:** Python · fontTools · SVG + CSS анимация · GitHub Actions · **[⭐ github.com/yyakowvw/readme-studio](https://github.com/yyakowvw/readme-studio)**

<a name="услуги"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-02-bg-mobile.svg" />
<img src="assets/motion/divider-02-bg.svg" alt="" width="100%" />
</picture>

## 💼 За какво можете да ме наемете

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/services-bg-mobile.svg" />
<img src="assets/motion/services-bg.svg" alt="01 Сайтове и онлайн бизнес: Фирмени сайтове, целеви страници, портфолиа, онлайн магазини, интерфейси за резервации и обновяване на съществуващи сайтове. 02 Софтуер и платформи: Уеб и настолни приложения, табла, административни панели, клиентски портали и вътрешни бизнес инструменти. 03 Discord ботове и общности: Команди, тикети, модерация, роли, известия, дневници на събитията и свързани административни табла. 04 Игри и FiveM системи: Игри и прототипи, игрови механики, сървърни ресурси, NUI интерфейси, професии, инвентари и инструменти за екипа. 05 Автоматизации и AI: Скриптове за повтарящи се задачи, AI функционалности, асистенти, обработка на данни и свързване на услуги. 06 Поддръжка и развитие: Нови функции, поправка на грешки, преработка на код, оптимизация, миграции, подобрения на интерфейса и подготовка за публикуване." width="100%" />
</picture>

**Предлагам · доказано · проучвам.** Картите по-горе са услугите, които предлагам. Проектите показват вече реализирания опит. Панелите с технологии по-долу отделят използваното в тези продукти от по-широките интереси.

<details>
<summary><b>Разгледайте пълния каталог с услуги</b></summary>

| Област | Примерен обхват |
| :--- | :--- |
| 🌍 **Сайтове** | Фирмени и лични сайтове, портфолиа, кампании, каталози и съдържателни страници |
| 🛒 **Онлайн магазини** | Продукти, поръчки, клиентски профили и интеграции за плащане |
| 📅 **Резервации** | Записване на часове, наличности, напомняния и календари |
| 🧩 **Уеб приложения** | SaaS интерфейси, членски платформи, портали и интерактивни табла |
| 🖥️ **Настолен софтуер** | Помощни програми, инструменти за продуктивност и инсталатори |
| 📱 **Мобилни интерфейси** | Адаптивни сайтове, прогресивни уеб приложения и прототипи |
| 🎨 **UI/UX** | Компоненти, дизайн системи, анимация и достъпност |
| ⚙️ **Сървърна логика** | API услуги, фонови задачи, проверки и интеграции |
| 🗄️ **Бази данни** | Структура, миграции, импорт, експорт и справки |
| 🔐 **Профили и права** | Вход, роли, права на екипа и журнал на действията |
| 🔌 **Интеграции** | Външни услуги, webhooks, известия и свързани процеси |
| 💬 **Discord** | Ботове, команди, тикети, роли, дневници и връзка с игрови сървъри |
| 🎮 **Игри** | Прототипи, игрови функции, браузърни игри и помощни инструменти |
| 🚓 **FiveM** | Ресурси, NUI, професии, полицейски системи и администрация |
| 🏢 **Бизнес софтуер** | CRM инструменти, служители, наличности и оперативни панели |
| 🤖 **AI функции** | AI API, асистенти и работа със съдържание |
| 🔁 **Автоматизация** | Файлове, данни, известия и координация между услуги |
| 🧰 **Инструменти за разработчици** | CLI, проверки на проекти и помощни средства за публикуване |
| 🧪 **Качество** | Тестове, статичен анализ, типове, компилация и диагностика |
| 🚀 **Публикуване и поддръжка** | Среди, CI/CD, наблюдение и последващи подобрения |

**Обхватът се уточнява за всеки проект.** Функциите, платформите, срокът и цената зависят от договорените изисквания. Това са предлагани услуги; конкретният реализиран опит е показан в проектите по-горе.

</details>

> **Имате друга идея?** Разглеждам и разработка извън този списък. Опишете проблема, потребителите и какво трябва да прави решението.

<a name="технологии"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-03-bg-mobile.svg" />
<img src="assets/motion/divider-03-bg.svg" alt="" width="100%" />
</picture>

## 🌈 Езици и технологии

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-used-bg-mobile.svg" />
<img src="assets/motion/stack-used-bg.svg" alt="Използвано в представените проекти. Before I Deploy: Swift, SwiftUI, JavaScript, Node.js, Supabase, PostgreSQL, Deno Edge Functions. The Last Republic: TypeScript, Next.js, React, Tailwind CSS, Drizzle, Neon Postgres, Netlify. TLR Police Portal: TypeScript, Next.js, React, Tailwind CSS, Drizzle, Neon Postgres, discord.js." width="100%" />
</picture>

Колекцията от 68 технологии по-долу показва допълнителни интереси и възможни технологични избори. Тя не означава завършени продукти или еднакъв опит с всеки инструмент. **Ментовият кръг** отбелязва инструментите, проверени в проектите по-горе.

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-tools-bg-mobile.svg" />
<img src="assets/motion/stack-tools-bg.svg" alt="Допълнителни инструменти и интереси, 13: TypeScript (използвано в проектите), JavaScript (използвано), Python, Lua, HTML5 (използвано), CSS3, SQL, Node.js (използвано), Astro, MySQL, MariaDB, Git, GitHub." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-languages-bg-mobile.svg" />
<img src="assets/motion/stack-languages-bg.svg" alt="Други програмни езици, 27: C, C++, C#, Java, Kotlin, Swift (използвано в проектите), Go, Rust, PHP, Ruby, Dart, Scala, R, Bash, PowerShell, Elixir, Erlang, Haskell, Clojure, F#, Julia, Zig, Solidity, GDScript, Objective-C, Perl, OCaml." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-web-bg-mobile.svg" />
<img src="assets/motion/stack-web-bg.svg" alt="Уеб технологии и приложения, 10: React (използвано в проектите), Next.js (използвано), Vue.js, Svelte, Vite (използвано), Tailwind CSS (използвано), Express, Electron, Flutter, .NET." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-data-bg-mobile.svg" />
<img src="assets/motion/stack-data-bg.svg" alt="Данни, инфраструктура и публикуване, 10: PostgreSQL (използвано в проектите), SQLite, MongoDB, Redis, Docker, Linux, macOS (използвано), Netlify, GitHub Actions, NGINX." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/stack-games-bg-mobile.svg" />
<img src="assets/motion/stack-games-bg.svg" alt="Игри, общности и AI, 8: Discord (използвано в проектите), FiveM, Godot, Unity, Unreal Engine, OpenAI, Anthropic, Cursor." width="100%" />
</picture>

<sub>Подходящият избор зависи от продукта; панелите не означават еднаква специализация. Конкретните инструменти и обхват се уточняват за всеки проект. Логата са в оригиналните цветове на марките чрез <a href="https://simpleicons.org">Simple Icons</a> (CC0); SQL, C#, PowerShell, Objective-C и OpenAI са текстови плочки, както в оригиналните значки.</sub>

<a name="сертификати"></a>

## 🎓 Сертификати

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/certificates-bg-mobile.svg" />
<img src="assets/motion/certificates-bg.svg" alt="Сертификати: Gemini Certified Educator (Google for Education, валиден до 23 юли 2029); AI-Powered Performance Ads (Google Ads, валиден до 21 юли 2027); Digital Marketing Certified (HubSpot Academy, валиден до 23 авг 2027); Digital Marketing Specialist (Advance Academy, фев–апр 2026); Fundamentals of Digital Marketing (Google, 27 юли 2026); значка Intro to Gemini (Google AI Educator Series, Foundational)." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/lessons-bg-mobile.svg" />
<img src="assets/motion/lessons-bg.svg" alt="129 урока от Google Applied Digital Skills, завършени 23–27 юли 2026: творчество и проучване 47, Google Workspace 38, кариера и професия 21, данни и логика 13, AI и дигитална сигурност 10." width="100%" />
</picture>

<details>
<summary><b>Всички 129 урока от Google Applied Digital Skills</b></summary>

**Творчество и проучване · 47**<br>
Build a Logo to Express Who You Are · Create a Brochure · Create a Collaborative Study Guide · Create a Community My Map · Create a Crossword Puzzle · Create a Digital Picture Book · Create a Digital Postcard · Create a Flyer for a Juneteenth Celebration · Create a Guide to an Area · Create a Presentation "All About a Topic" · Create a Scrapbook · Create a Slogan for Earth Day · Create a Travel Brochure for an Exoplanet · Create a Vision Board · Create an Annotated Playlist · Design a Poster About You · Design a Website to Promote a Project · Design and Share a Digital Badge · Explore a Topic: Celebrate Black History · Explore a Topic: Celebrate Latinx History · Explore a Topic: Earth Day · Explore a Topic: Equal Access to Technology · Explore a Topic: Innovators · Explore a Topic: Technology at Work · Explore a Topic: Technology's Role in Current Events · Explore a Topic: Women's History · Explore the History of Humankind in Kenya · Go on a Scavenger Hunt Through Italy · Learn New Vocabulary with Flash cards · Make Art Inspired by Frida Kahlo and Mexico · Make Your Own Space Shuttle Adventure · Make a Promotional Flyer · Memorize Facts with a Visual Mnemonic · Organize Your Time with a Digital Agenda · Plan and Promote an Event · Present Your Ideas for Classroom Expectations · Quiz Your Classmates About the Palace of Versailles · Research and Develop a Topic · Respond to a Question in Google Classroom · Schedule Emails for Goal-Setting · Take Notes in a Table · Welcome New Students with a Presentation · Write Effectively for Your Audience · Write a Press Release · Write a Story Using Emojis · Write an If-Then Adventure Story · Write the Lyrics for a Song

**Google Workspace · 38**<br>
Annotate Text in Google Docs · Create Papel Picado in Google Slides · Create Quizzes in Google Forms · Create a Clickable Map in Google Slides · Create a Collage in Google Drawings · Create a Comic Strip in Google Drawings · Create a Meme with Google Drawings · Create a Mind Map in Google Drawings · Create a Personal Timeline in Google Drawings · Create a Photo Journal in Google Docs · Create a Schedule to Meet Your Goals · Create a Virtual Family Reunion in Google Slides · Create an Animation in Google Slides · Design an Infographic in Google Drawings · Gmail for Beginners · Google Calendar for Beginners · Google Docs for Beginners · Google Drive for Beginners · Google Meet for Beginners · Google Search for Beginners · Google Sheets for Beginners · Google Workspace: Docs - Part 1 · Google Workspace: Docs - Part 2 · Google Workspace: Drive · Google Workspace: Gmail · Google Workspace: Sheets - Part 1 · Google Workspace: Sheets - Part 2 · Google Workspace: Sheets - Part 3 · Google Workspace: Slides - Part 1 · Google Workspace: Slides - Part 2 · Google Workspace: Slides - Part 3 · Introduce Yourself in Google Slides · Make Art with Google Sheets · Make Pop Art in Google Drawings · Manage Your Time With Google Sheets · Show Appreciation with Google Slides · Track Due Dates and Tasks in Gmail · Use Drive to Organize Files

**Кариера и професия · 21**<br>
Ask Someone to Be a Reference · Ask for Feedback · Build Your Professional Brand · Build Your Professional Network · Build a Portfolio with Google Sites · Create a Resume in Google Docs · Draft an Application Essay · Explore Careers by Interviewing Professionals · Introduce Yourself to Potential Employers · Organize College Applications in Google Sheets · Organize College Information in Google Sheets · Prepare for Your First Day of Work · Prepare for a College Interview · Prepare for the FAFSA · Research Career Paths · Research and Interview a Person From History · Search for Colleges Online · Search for Scholarships · Search for a Part-Time or Summer Job · Track Graduation Requirements · Write a Cover Letter for Your First Job

**Данни и логика · 13**<br>
Analyze Data from Images in Google Earth Engine · Calculate Percentages in Google Sheets · Calculate Probability with Google Sheets · Code a Joke-Telling Talkbot · Create a Budget in Google Sheets · Create a Guessing Game · Find the Mean, Median, or Mode of a Data Set · Make a Flowchart · Make a Word Game · Pick the Next Box Office Hit · Program a Progress Bar · Wage a Sea Battle with Google Sheets · Work with Fractions In Google Sheets

**AI и дигитална сигурност · 10**<br>
Avoid Online Scams · Build Healthy Digital Habits · Create a Responsible Blog with Google Sites · Create and Safeguard Passwords · Discover AI in Daily Life · Evaluate Credibility of Online Sources · Explore a Topic: Generative AI · Explore a Topic: Technology, Ethics, and Security · Identify Cyberbullying · Understand Your Digital Footprint

</details>

<sub>Оригиналните файлове на сертификатите се пазят частно; номерата и данните за проверка са налични при запитване.</sub>

<a name="активност"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-04-bg-mobile.svg" />
<img src="assets/motion/divider-04-bg.svg" alt="" width="100%" />
</picture>

## 📊 Активност и езици

<picture>
<source media="(max-width: 600px)" srcset="assets/metrics/activity-bg-mobile.svg" />
<img src="assets/metrics/activity-bg.svg" alt="Приноси, активни дни, текуща и най-дълга поредица, последен принос и календар." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/metrics/languages-bg-mobile.svg" />
<img src="assets/metrics/languages-bg.svg" alt="Езици по обем код в проектите, включително частни хранилища, без имена и съдържание." width="100%" />
</picture>

<details>
<summary><b>Как се изчисляват показателите</b></summary>

Активността се обновява ежедневно от публичния календар на GitHub. Приносите не са само commit-и и не показват часове работа. „Последен принос“ е последният активен ден в календара, а не последно влизане в профила. GitHub може да обновява календара със закъснение.

Текущата поредица брои последователните активни дни до днес или вчера, ако днешният ден още няма принос. Най-дългата поредица, приносите и активните дни са в показания годишен период. Мобилният календар показва последните 26 седмици; общите показатели остават за годишния период.

Езиковите дялове са отделна снимка от 2026-10-05 на обема код според GitHub, включително частните проекти и без профилното хранилище. Това не измерва честота, време или умения. Езиковата снимка не се обновява автоматично: публичната задача няма достъп до частния код.

[GitHub contribution rules](https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference) · [Metrics source](scripts/update_metrics.py)

</details>

<a name="процес"></a>

## 🧭 От вашата идея до работещ продукт

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/process-bg-mobile.svg" />
<img src="assets/motion/process-bg.svg" alt="01 Проучване: цели, потребители и изисквания. 02 Дизайн: интерфейс, архитектура и обхват. 03 Разработка: функции и интеграции. 04 Проверка: поведение, грешки и готовност. 05 Публикуване: публикуване, документация и следващи подобрения." width="100%" />
</picture>

### Какво е важно в работата ми

**🎯 Дизайн с цел** — интерфейс според нуждите на хората.<br>
**🧱 Ясна архитектура** — разбираем код, който може да се развива.<br>
**🔐 Обмислени права** — проверки и контрол на достъпа.<br>
**🧪 Практически проверки** — тестове и диагностика преди публикуване.<br>
**🔁 Полезна автоматизация** — по-малко повтаряща се работа.<br>
**🤝 Ясен обхват** — договорени изисквания, резултати и очаквания.

<a name="контакт"></a>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/divider-05-bg-mobile.svg" />
<img src="assets/motion/divider-05-bg.svg" alt="" width="100%" />
</picture>

## 📬 Нека обсъдим вашия проект

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/finale-bg-mobile.svg" />
<img src="assets/motion/finale-bg.svg" alt="Приемам платени проекти. Какво да създадем следващо? Сайт, инструмент, бот или следващата ви идея." width="100%" />
</picture>

<p align="center">
<a href="mailto:Fraisbg1@gmail.com"><img src="assets/motion/contact-mail-bg.svg" alt="Имейл Fraisbg1@gmail.com" height="46" /></a>
<img src="assets/motion/contact-discord-bg.svg" alt="Discord: Fraisbg" height="46" />
<a href="https://www.instagram.com/y.yakowvw.sales/"><img src="assets/motion/contact-instagram-bg.svg" alt="Instagram @y.yakowvw.sales" height="46" /></a>
</p>

<p align="center"><b>Приемам платени поръчки за сайтове, софтуер, Discord ботове и игри.</b><br>
Изпратете идеята, основните функции, срока и бюджета — заедно ще уточним обхвата и цената.</p>

<picture>
<source media="(max-width: 600px)" srcset="assets/motion/footer-bg-mobile.svg" />
<img src="assets/motion/footer-bg.svg" alt="Сайтове · Софтуер · Ботове · Игри · Автоматизации. Вашата идея. Ясен план. Работещ софтуер. Създаване · Тестване · Проверка · Публикуване · Развитие." width="100%" />
</picture>
