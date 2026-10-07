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


<a name="talk-to-mac"></a>

**Talk to Mac — превърнете вашия MacBook в личен интерком, който управлявате от телефона, отвсякъде.**

Задържате бутон и гласът ви излиза от говорителите на Mac-а; с едно докосване слушате стаята или гледате камерата. Звукът и видеото вървят от край до край по WebRTC — безплатен Cloudflare Worker само запознава двете устройства. **Изцяло отворен код, с живо демо.**

<a href="https://github.com/yyakowvw/talk-to-mac">
<img src="assets/video/talk-to-mac-demo-en.webp" alt="Демо на Talk to Mac: iPhone (вдясно) задържа за говорене, слуша стаята и гледа камерата на Mac-а; приемникът на MacBook (вляво) отговаря на живо." width="100%" />
</a>

<p align="center"><sub>🎬 <b>Вижте на живо</b>: задържане за говорене, звук от стаята и камерата на Mac-а — телефонът управлява Mac-а.</sub></p>

- **Правилно задържане за говорене:** микрофонът е закачен само докато бутонът е натиснат, затова иначе от телефона не излиза нищо, дори тишина.
- **Работи през всяка мрежа:** свързването чрез long polling минава през тунели и прокси; безплатен Cloudflare TURN пренася звука и видеото, когато директен път е блокиран.
- **Приложение за Mac, което не заспива:** приемникът върви в скрит WKWebView, поддържан жив, за да не го „приспива“ macOS и да къса връзката.
- **При поискване и поверително:** микрофонът и камерата се включват само при поискване и спират веднага щом телефонът затвори, а индикаторът за запис на macOS винаги свети. Нищо не се записва.

**Създадено с:** WebRTC · Cloudflare Workers · Durable Objects · Cloudflare TURN · Swift · SwiftUI · Node.js · **[⭐ github.com/yyakowvw/talk-to-mac](https://github.com/yyakowvw/talk-to-mac)**

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

Колекцията от 69 технологии по-долу показва допълнителни интереси и възможни технологични избори. Тя не означава завършени продукти или еднакъв опит с всеки инструмент. **Ментовият кръг** отбелязва инструментите, проверени в проектите по-горе.

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
<img src="assets/motion/stack-games-bg.svg" alt="Игри, общности и AI, 9: Discord (използвано в проектите), FiveM, Godot, Unity, Unreal Engine, OpenAI, Anthropic, Cursor, Higgsfield." width="100%" />
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

### 🏅 Всички 135 сертификата

Подредени по важност. Натиснете заглавие, за да отворите сертификата.

<details>
<summary><b>1 · Gemini Certified Educator</b> — Google for Education · издаден 23 юли 2026 · валиден до 23 юли 2029</summary>

<img src="assets/certificates/featured/1-gemini-certified-educator.jpg" width="100%" alt="Сертификат: Gemini Certified Educator, Google for Education" />

</details>

<details>
<summary><b>2 · AI-Powered Performance Ads</b> — Google Ads · издаден 21 юли 2026 · валиден до 21 юли 2027</summary>

<img src="assets/certificates/featured/2-google-ads-ai-powered-performance-ads.jpg" width="100%" alt="Сертификат: AI-Powered Performance Ads, Google Ads" />

</details>

<details>
<summary><b>3 · Digital Marketing Certified</b> — HubSpot Academy · издаден 24 юли 2026 · валиден до 23 авг 2027</summary>

<img src="assets/certificates/featured/3-hubspot-digital-marketing.jpg" width="100%" alt="Сертификат: Digital Marketing Certified, HubSpot Academy" />

</details>

<details>
<summary><b>4 · Digital Marketing Specialist</b> — Advance Academy · програма февр.–апр. 2026 · издаден 30 апр 2026</summary>

<img src="assets/certificates/featured/4-advance-academy-digital-marketing-specialist.jpg" width="100%" alt="Сертификат: Digital Marketing Specialist, Advance Academy" />

</details>

<details>
<summary><b>5 · Fundamentals of Digital Marketing</b> — Google · завършен 27 юли 2026</summary>

<img src="assets/certificates/featured/5-google-fundamentals-of-digital-marketing.jpg" width="100%" alt="Сертификат: Fundamentals of Digital Marketing, Google" />

</details>

<details>
<summary><b>6 · Intro to Gemini</b> — Google AI Educator Series · базова значка</summary>

<img src="assets/certificates/featured/6-google-intro-to-gemini.jpg" width="100%" alt="Сертификат: Intro to Gemini, Google AI Educator Series" />

</details>

<details>
<summary><b>7–135 · 129 урока от Google Applied Digital Skills</b> — завършени 23–27 юли 2026 · натиснете тема, после урок</summary>

<details>
<summary><b>Творчество и проучване · 47</b></summary>

<details>
<summary>Build a Logo to Express Who You Are · 24 юли 2026</summary>

<img src="assets/certificates/lessons/build-a-logo-to-express-who-you-are.jpg" width="420" alt="Сертификат: Build a Logo to Express Who You Are, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Brochure · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-brochure.jpg" width="420" alt="Сертификат: Create a Brochure, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Collaborative Study Guide · 24 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-collaborative-study-guide.jpg" width="420" alt="Сертификат: Create a Collaborative Study Guide, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Community My Map · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-community-my-map.jpg" width="420" alt="Сертификат: Create a Community My Map, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Crossword Puzzle · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-crossword-puzzle.jpg" width="420" alt="Сертификат: Create a Crossword Puzzle, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Digital Picture Book · 24 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-digital-picture-book.jpg" width="420" alt="Сертификат: Create a Digital Picture Book, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Digital Postcard · 24 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-digital-postcard.jpg" width="420" alt="Сертификат: Create a Digital Postcard, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Flyer for a Juneteenth Celebration · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-flyer-for-a-juneteenth-celebration.jpg" width="420" alt="Сертификат: Create a Flyer for a Juneteenth Celebration, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Guide to an Area · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-guide-to-an-area.jpg" width="420" alt="Сертификат: Create a Guide to an Area, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Presentation "All About a Topic" · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-presentation-all-about-a-topic.jpg" width="420" alt="Сертификат: Create a Presentation "All About a Topic", Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Scrapbook · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-scrapbook.jpg" width="420" alt="Сертификат: Create a Scrapbook, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Slogan for Earth Day · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-slogan-for-earth-day.jpg" width="420" alt="Сертификат: Create a Slogan for Earth Day, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Travel Brochure for an Exoplanet · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-travel-brochure-for-an-exoplanet.jpg" width="420" alt="Сертификат: Create a Travel Brochure for an Exoplanet, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Vision Board · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-vision-board.jpg" width="420" alt="Сертификат: Create a Vision Board, Google Applied Digital Skills" />

</details>

<details>
<summary>Create an Annotated Playlist · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-an-annotated-playlist.jpg" width="420" alt="Сертификат: Create an Annotated Playlist, Google Applied Digital Skills" />

</details>

<details>
<summary>Design a Poster About You · 27 юли 2026</summary>

<img src="assets/certificates/lessons/design-a-poster-about-you.jpg" width="420" alt="Сертификат: Design a Poster About You, Google Applied Digital Skills" />

</details>

<details>
<summary>Design a Website to Promote a Project · 27 юли 2026</summary>

<img src="assets/certificates/lessons/design-a-website-to-promote-a-project.jpg" width="420" alt="Сертификат: Design a Website to Promote a Project, Google Applied Digital Skills" />

</details>

<details>
<summary>Design and Share a Digital Badge · 27 юли 2026</summary>

<img src="assets/certificates/lessons/design-and-share-a-digital-badge.jpg" width="420" alt="Сертификат: Design and Share a Digital Badge, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Celebrate Black History · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-celebrate-black-history.jpg" width="420" alt="Сертификат: Explore a Topic: Celebrate Black History, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Celebrate Latinx History · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-celebrate-latinx-history.jpg" width="420" alt="Сертификат: Explore a Topic: Celebrate Latinx History, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Earth Day · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-earth-day.jpg" width="420" alt="Сертификат: Explore a Topic: Earth Day, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Equal Access to Technology · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-equal-access-to-technology.jpg" width="420" alt="Сертификат: Explore a Topic: Equal Access to Technology, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Innovators · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-innovators.jpg" width="420" alt="Сертификат: Explore a Topic: Innovators, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Technology at Work · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-technology-at-work.jpg" width="420" alt="Сертификат: Explore a Topic: Technology at Work, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Technology's Role in Current Events · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-technology-s-role-in-current-events.jpg" width="420" alt="Сертификат: Explore a Topic: Technology's Role in Current Events, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Women's History · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-women-s-history.jpg" width="420" alt="Сертификат: Explore a Topic: Women's History, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore the History of Humankind in Kenya · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-the-history-of-humankind-in-kenya.jpg" width="420" alt="Сертификат: Explore the History of Humankind in Kenya, Google Applied Digital Skills" />

</details>

<details>
<summary>Go on a Scavenger Hunt Through Italy · 25 юли 2026</summary>

<img src="assets/certificates/lessons/go-on-a-scavenger-hunt-through-italy.jpg" width="420" alt="Сертификат: Go on a Scavenger Hunt Through Italy, Google Applied Digital Skills" />

</details>

<details>
<summary>Learn New Vocabulary with Flash cards · 27 юли 2026</summary>

<img src="assets/certificates/lessons/learn-new-vocabulary-with-flash-cards.jpg" width="420" alt="Сертификат: Learn New Vocabulary with Flash cards, Google Applied Digital Skills" />

</details>

<details>
<summary>Make Art Inspired by Frida Kahlo and Mexico · 25 юли 2026</summary>

<img src="assets/certificates/lessons/make-art-inspired-by-frida-kahlo-and-mexico.jpg" width="420" alt="Сертификат: Make Art Inspired by Frida Kahlo and Mexico, Google Applied Digital Skills" />

</details>

<details>
<summary>Make Your Own Space Shuttle Adventure · 25 юли 2026</summary>

<img src="assets/certificates/lessons/make-your-own-space-shuttle-adventure.jpg" width="420" alt="Сертификат: Make Your Own Space Shuttle Adventure, Google Applied Digital Skills" />

</details>

<details>
<summary>Make a Promotional Flyer · 27 юли 2026</summary>

<img src="assets/certificates/lessons/make-a-promotional-flyer.jpg" width="420" alt="Сертификат: Make a Promotional Flyer, Google Applied Digital Skills" />

</details>

<details>
<summary>Memorize Facts with a Visual Mnemonic · 27 юли 2026</summary>

<img src="assets/certificates/lessons/memorize-facts-with-a-visual-mnemonic.jpg" width="420" alt="Сертификат: Memorize Facts with a Visual Mnemonic, Google Applied Digital Skills" />

</details>

<details>
<summary>Organize Your Time with a Digital Agenda · 24 юли 2026</summary>

<img src="assets/certificates/lessons/organize-your-time-with-a-digital-agenda.jpg" width="420" alt="Сертификат: Organize Your Time with a Digital Agenda, Google Applied Digital Skills" />

</details>

<details>
<summary>Plan and Promote an Event · 24 юли 2026</summary>

<img src="assets/certificates/lessons/plan-and-promote-an-event.jpg" width="420" alt="Сертификат: Plan and Promote an Event, Google Applied Digital Skills" />

</details>

<details>
<summary>Present Your Ideas for Classroom Expectations · 24 юли 2026</summary>

<img src="assets/certificates/lessons/present-your-ideas-for-classroom-expectations.jpg" width="420" alt="Сертификат: Present Your Ideas for Classroom Expectations, Google Applied Digital Skills" />

</details>

<details>
<summary>Quiz Your Classmates About the Palace of Versailles · 25 юли 2026</summary>

<img src="assets/certificates/lessons/quiz-your-classmates-about-the-palace-of-versailles.jpg" width="420" alt="Сертификат: Quiz Your Classmates About the Palace of Versailles, Google Applied Digital Skills" />

</details>

<details>
<summary>Research and Develop a Topic · 25 юли 2026</summary>

<img src="assets/certificates/lessons/research-and-develop-a-topic.jpg" width="420" alt="Сертификат: Research and Develop a Topic, Google Applied Digital Skills" />

</details>

<details>
<summary>Respond to a Question in Google Classroom · 26 юли 2026</summary>

<img src="assets/certificates/lessons/respond-to-a-question-in-google-classroom.jpg" width="420" alt="Сертификат: Respond to a Question in Google Classroom, Google Applied Digital Skills" />

</details>

<details>
<summary>Schedule Emails for Goal-Setting · 24 юли 2026</summary>

<img src="assets/certificates/lessons/schedule-emails-for-goal-setting.jpg" width="420" alt="Сертификат: Schedule Emails for Goal-Setting, Google Applied Digital Skills" />

</details>

<details>
<summary>Take Notes in a Table · 25 юли 2026</summary>

<img src="assets/certificates/lessons/take-notes-in-a-table.jpg" width="420" alt="Сертификат: Take Notes in a Table, Google Applied Digital Skills" />

</details>

<details>
<summary>Welcome New Students with a Presentation · 24 юли 2026</summary>

<img src="assets/certificates/lessons/welcome-new-students-with-a-presentation.jpg" width="420" alt="Сертификат: Welcome New Students with a Presentation, Google Applied Digital Skills" />

</details>

<details>
<summary>Write Effectively for Your Audience · 24 юли 2026</summary>

<img src="assets/certificates/lessons/write-effectively-for-your-audience.jpg" width="420" alt="Сертификат: Write Effectively for Your Audience, Google Applied Digital Skills" />

</details>

<details>
<summary>Write a Press Release · 24 юли 2026</summary>

<img src="assets/certificates/lessons/write-a-press-release.jpg" width="420" alt="Сертификат: Write a Press Release, Google Applied Digital Skills" />

</details>

<details>
<summary>Write a Story Using Emojis · 24 юли 2026</summary>

<img src="assets/certificates/lessons/write-a-story-using-emojis.jpg" width="420" alt="Сертификат: Write a Story Using Emojis, Google Applied Digital Skills" />

</details>

<details>
<summary>Write an If-Then Adventure Story · 24 юли 2026</summary>

<img src="assets/certificates/lessons/write-an-if-then-adventure-story.jpg" width="420" alt="Сертификат: Write an If-Then Adventure Story, Google Applied Digital Skills" />

</details>

<details>
<summary>Write the Lyrics for a Song · 24 юли 2026</summary>

<img src="assets/certificates/lessons/write-the-lyrics-for-a-song.jpg" width="420" alt="Сертификат: Write the Lyrics for a Song, Google Applied Digital Skills" />

</details>

</details>

<details>
<summary><b>Google Workspace · 38</b></summary>

<details>
<summary>Annotate Text in Google Docs · 24 юли 2026</summary>

<img src="assets/certificates/lessons/annotate-text-in-google-docs.jpg" width="420" alt="Сертификат: Annotate Text in Google Docs, Google Applied Digital Skills" />

</details>

<details>
<summary>Create Papel Picado in Google Slides · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-papel-picado-in-google-slides.jpg" width="420" alt="Сертификат: Create Papel Picado in Google Slides, Google Applied Digital Skills" />

</details>

<details>
<summary>Create Quizzes in Google Forms · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-quizzes-in-google-forms.jpg" width="420" alt="Сертификат: Create Quizzes in Google Forms, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Clickable Map in Google Slides · 24 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-clickable-map-in-google-slides.jpg" width="420" alt="Сертификат: Create a Clickable Map in Google Slides, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Collage in Google Drawings · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-collage-in-google-drawings.jpg" width="420" alt="Сертификат: Create a Collage in Google Drawings, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Comic Strip in Google Drawings · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-comic-strip-in-google-drawings.jpg" width="420" alt="Сертификат: Create a Comic Strip in Google Drawings, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Meme with Google Drawings · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-meme-with-google-drawings.jpg" width="420" alt="Сертификат: Create a Meme with Google Drawings, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Mind Map in Google Drawings · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-mind-map-in-google-drawings.jpg" width="420" alt="Сертификат: Create a Mind Map in Google Drawings, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Personal Timeline in Google Drawings · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-personal-timeline-in-google-drawings.jpg" width="420" alt="Сертификат: Create a Personal Timeline in Google Drawings, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Photo Journal in Google Docs · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-photo-journal-in-google-docs.jpg" width="420" alt="Сертификат: Create a Photo Journal in Google Docs, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Schedule to Meet Your Goals · 24 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-schedule-to-meet-your-goals.jpg" width="420" alt="Сертификат: Create a Schedule to Meet Your Goals, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Virtual Family Reunion in Google Slides · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-virtual-family-reunion-in-google-slides.jpg" width="420" alt="Сертификат: Create a Virtual Family Reunion in Google Slides, Google Applied Digital Skills" />

</details>

<details>
<summary>Create an Animation in Google Slides · 27 юли 2026</summary>

<img src="assets/certificates/lessons/create-an-animation-in-google-slides.jpg" width="420" alt="Сертификат: Create an Animation in Google Slides, Google Applied Digital Skills" />

</details>

<details>
<summary>Design an Infographic in Google Drawings · 27 юли 2026</summary>

<img src="assets/certificates/lessons/design-an-infographic-in-google-drawings.jpg" width="420" alt="Сертификат: Design an Infographic in Google Drawings, Google Applied Digital Skills" />

</details>

<details>
<summary>Gmail for Beginners · 25 юли 2026</summary>

<img src="assets/certificates/lessons/gmail-for-beginners.jpg" width="420" alt="Сертификат: Gmail for Beginners, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Calendar for Beginners · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-calendar-for-beginners.jpg" width="420" alt="Сертификат: Google Calendar for Beginners, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Docs for Beginners · 25 юли 2026</summary>

<img src="assets/certificates/lessons/google-docs-for-beginners.jpg" width="420" alt="Сертификат: Google Docs for Beginners, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Drive for Beginners · 25 юли 2026</summary>

<img src="assets/certificates/lessons/google-drive-for-beginners.jpg" width="420" alt="Сертификат: Google Drive for Beginners, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Meet for Beginners · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-meet-for-beginners.jpg" width="420" alt="Сертификат: Google Meet for Beginners, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Search for Beginners · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-search-for-beginners.jpg" width="420" alt="Сертификат: Google Search for Beginners, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Sheets for Beginners · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-sheets-for-beginners.jpg" width="420" alt="Сертификат: Google Sheets for Beginners, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Docs - Part 1 · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-docs-part-1.jpg" width="420" alt="Сертификат: Google Workspace: Docs - Part 1, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Docs - Part 2 · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-docs-part-2.jpg" width="420" alt="Сертификат: Google Workspace: Docs - Part 2, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Drive · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-drive.jpg" width="420" alt="Сертификат: Google Workspace: Drive, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Gmail · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-gmail.jpg" width="420" alt="Сертификат: Google Workspace: Gmail, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Sheets - Part 1 · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-sheets-part-1.jpg" width="420" alt="Сертификат: Google Workspace: Sheets - Part 1, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Sheets - Part 2 · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-sheets-part-2.jpg" width="420" alt="Сертификат: Google Workspace: Sheets - Part 2, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Sheets - Part 3 · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-sheets-part-3.jpg" width="420" alt="Сертификат: Google Workspace: Sheets - Part 3, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Slides - Part 1 · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-slides-part-1.jpg" width="420" alt="Сертификат: Google Workspace: Slides - Part 1, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Slides - Part 2 · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-slides-part-2.jpg" width="420" alt="Сертификат: Google Workspace: Slides - Part 2, Google Applied Digital Skills" />

</details>

<details>
<summary>Google Workspace: Slides - Part 3 · 23 юли 2026</summary>

<img src="assets/certificates/lessons/google-workspace-slides-part-3.jpg" width="420" alt="Сертификат: Google Workspace: Slides - Part 3, Google Applied Digital Skills" />

</details>

<details>
<summary>Introduce Yourself in Google Slides · 27 юли 2026</summary>

<img src="assets/certificates/lessons/introduce-yourself-in-google-slides.jpg" width="420" alt="Сертификат: Introduce Yourself in Google Slides, Google Applied Digital Skills" />

</details>

<details>
<summary>Make Art with Google Sheets · 27 юли 2026</summary>

<img src="assets/certificates/lessons/make-art-with-google-sheets.jpg" width="420" alt="Сертификат: Make Art with Google Sheets, Google Applied Digital Skills" />

</details>

<details>
<summary>Make Pop Art in Google Drawings · 27 юли 2026</summary>

<img src="assets/certificates/lessons/make-pop-art-in-google-drawings.jpg" width="420" alt="Сертификат: Make Pop Art in Google Drawings, Google Applied Digital Skills" />

</details>

<details>
<summary>Manage Your Time With Google Sheets · 24 юли 2026</summary>

<img src="assets/certificates/lessons/manage-your-time-with-google-sheets.jpg" width="420" alt="Сертификат: Manage Your Time With Google Sheets, Google Applied Digital Skills" />

</details>

<details>
<summary>Show Appreciation with Google Slides · 25 юли 2026</summary>

<img src="assets/certificates/lessons/show-appreciation-with-google-slides.jpg" width="420" alt="Сертификат: Show Appreciation with Google Slides, Google Applied Digital Skills" />

</details>

<details>
<summary>Track Due Dates and Tasks in Gmail · 25 юли 2026</summary>

<img src="assets/certificates/lessons/track-due-dates-and-tasks-in-gmail.jpg" width="420" alt="Сертификат: Track Due Dates and Tasks in Gmail, Google Applied Digital Skills" />

</details>

<details>
<summary>Use Drive to Organize Files · 24 юли 2026</summary>

<img src="assets/certificates/lessons/use-drive-to-organize-files.jpg" width="420" alt="Сертификат: Use Drive to Organize Files, Google Applied Digital Skills" />

</details>

</details>

<details>
<summary><b>Кариера и професия · 21</b></summary>

<details>
<summary>Ask Someone to Be a Reference · 24 юли 2026</summary>

<img src="assets/certificates/lessons/ask-someone-to-be-a-reference.jpg" width="420" alt="Сертификат: Ask Someone to Be a Reference, Google Applied Digital Skills" />

</details>

<details>
<summary>Ask for Feedback · 24 юли 2026</summary>

<img src="assets/certificates/lessons/ask-for-feedback.jpg" width="420" alt="Сертификат: Ask for Feedback, Google Applied Digital Skills" />

</details>

<details>
<summary>Build Your Professional Brand · 24 юли 2026</summary>

<img src="assets/certificates/lessons/build-your-professional-brand.jpg" width="420" alt="Сертификат: Build Your Professional Brand, Google Applied Digital Skills" />

</details>

<details>
<summary>Build Your Professional Network · 24 юли 2026</summary>

<img src="assets/certificates/lessons/build-your-professional-network.jpg" width="420" alt="Сертификат: Build Your Professional Network, Google Applied Digital Skills" />

</details>

<details>
<summary>Build a Portfolio with Google Sites · 23 юли 2026</summary>

<img src="assets/certificates/lessons/build-a-portfolio-with-google-sites.jpg" width="420" alt="Сертификат: Build a Portfolio with Google Sites, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Resume in Google Docs · 23 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-resume-in-google-docs.jpg" width="420" alt="Сертификат: Create a Resume in Google Docs, Google Applied Digital Skills" />

</details>

<details>
<summary>Draft an Application Essay · 25 юли 2026</summary>

<img src="assets/certificates/lessons/draft-an-application-essay.jpg" width="420" alt="Сертификат: Draft an Application Essay, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore Careers by Interviewing Professionals · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-careers-by-interviewing-professionals.jpg" width="420" alt="Сертификат: Explore Careers by Interviewing Professionals, Google Applied Digital Skills" />

</details>

<details>
<summary>Introduce Yourself to Potential Employers · 27 юли 2026</summary>

<img src="assets/certificates/lessons/introduce-yourself-to-potential-employers.jpg" width="420" alt="Сертификат: Introduce Yourself to Potential Employers, Google Applied Digital Skills" />

</details>

<details>
<summary>Organize College Applications in Google Sheets · 27 юли 2026</summary>

<img src="assets/certificates/lessons/organize-college-applications-in-google-sheets.jpg" width="420" alt="Сертификат: Organize College Applications in Google Sheets, Google Applied Digital Skills" />

</details>

<details>
<summary>Organize College Information in Google Sheets · 27 юли 2026</summary>

<img src="assets/certificates/lessons/organize-college-information-in-google-sheets.jpg" width="420" alt="Сертификат: Organize College Information in Google Sheets, Google Applied Digital Skills" />

</details>

<details>
<summary>Prepare for Your First Day of Work · 24 юли 2026</summary>

<img src="assets/certificates/lessons/prepare-for-your-first-day-of-work.jpg" width="420" alt="Сертификат: Prepare for Your First Day of Work, Google Applied Digital Skills" />

</details>

<details>
<summary>Prepare for a College Interview · 24 юли 2026</summary>

<img src="assets/certificates/lessons/prepare-for-a-college-interview.jpg" width="420" alt="Сертификат: Prepare for a College Interview, Google Applied Digital Skills" />

</details>

<details>
<summary>Prepare for the FAFSA · 24 юли 2026</summary>

<img src="assets/certificates/lessons/prepare-for-the-fafsa.jpg" width="420" alt="Сертификат: Prepare for the FAFSA, Google Applied Digital Skills" />

</details>

<details>
<summary>Research Career Paths · 26 юли 2026</summary>

<img src="assets/certificates/lessons/research-career-paths.jpg" width="420" alt="Сертификат: Research Career Paths, Google Applied Digital Skills" />

</details>

<details>
<summary>Research and Interview a Person From History · 27 юли 2026</summary>

<img src="assets/certificates/lessons/research-and-interview-a-person-from-history.jpg" width="420" alt="Сертификат: Research and Interview a Person From History, Google Applied Digital Skills" />

</details>

<details>
<summary>Search for Colleges Online · 26 юли 2026</summary>

<img src="assets/certificates/lessons/search-for-colleges-online.jpg" width="420" alt="Сертификат: Search for Colleges Online, Google Applied Digital Skills" />

</details>

<details>
<summary>Search for Scholarships · 26 юли 2026</summary>

<img src="assets/certificates/lessons/search-for-scholarships.jpg" width="420" alt="Сертификат: Search for Scholarships, Google Applied Digital Skills" />

</details>

<details>
<summary>Search for a Part-Time or Summer Job · 24 юли 2026</summary>

<img src="assets/certificates/lessons/search-for-a-part-time-or-summer-job.jpg" width="420" alt="Сертификат: Search for a Part-Time or Summer Job, Google Applied Digital Skills" />

</details>

<details>
<summary>Track Graduation Requirements · 24 юли 2026</summary>

<img src="assets/certificates/lessons/track-graduation-requirements.jpg" width="420" alt="Сертификат: Track Graduation Requirements, Google Applied Digital Skills" />

</details>

<details>
<summary>Write a Cover Letter for Your First Job · 24 юли 2026</summary>

<img src="assets/certificates/lessons/write-a-cover-letter-for-your-first-job.jpg" width="420" alt="Сертификат: Write a Cover Letter for Your First Job, Google Applied Digital Skills" />

</details>

</details>

<details>
<summary><b>Данни и логика · 13</b></summary>

<details>
<summary>Analyze Data from Images in Google Earth Engine · 24 юли 2026</summary>

<img src="assets/certificates/lessons/analyze-data-from-images-in-google-earth-engine.jpg" width="420" alt="Сертификат: Analyze Data from Images in Google Earth Engine, Google Applied Digital Skills" />

</details>

<details>
<summary>Calculate Percentages in Google Sheets · 24 юли 2026</summary>

<img src="assets/certificates/lessons/calculate-percentages-in-google-sheets.jpg" width="420" alt="Сертификат: Calculate Percentages in Google Sheets, Google Applied Digital Skills" />

</details>

<details>
<summary>Calculate Probability with Google Sheets · 24 юли 2026</summary>

<img src="assets/certificates/lessons/calculate-probability-with-google-sheets.jpg" width="420" alt="Сертификат: Calculate Probability with Google Sheets, Google Applied Digital Skills" />

</details>

<details>
<summary>Code a Joke-Telling Talkbot · 24 юли 2026</summary>

<img src="assets/certificates/lessons/code-a-joke-telling-talkbot.jpg" width="420" alt="Сертификат: Code a Joke-Telling Talkbot, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Budget in Google Sheets · 24 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-budget-in-google-sheets.jpg" width="420" alt="Сертификат: Create a Budget in Google Sheets, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Guessing Game · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-guessing-game.jpg" width="420" alt="Сертификат: Create a Guessing Game, Google Applied Digital Skills" />

</details>

<details>
<summary>Find the Mean, Median, or Mode of a Data Set · 27 юли 2026</summary>

<img src="assets/certificates/lessons/find-the-mean-median-or-mode-of-a-data-set.jpg" width="420" alt="Сертификат: Find the Mean, Median, or Mode of a Data Set, Google Applied Digital Skills" />

</details>

<details>
<summary>Make a Flowchart · 25 юли 2026</summary>

<img src="assets/certificates/lessons/make-a-flowchart.jpg" width="420" alt="Сертификат: Make a Flowchart, Google Applied Digital Skills" />

</details>

<details>
<summary>Make a Word Game · 27 юли 2026</summary>

<img src="assets/certificates/lessons/make-a-word-game.jpg" width="420" alt="Сертификат: Make a Word Game, Google Applied Digital Skills" />

</details>

<details>
<summary>Pick the Next Box Office Hit · 24 юли 2026</summary>

<img src="assets/certificates/lessons/pick-the-next-box-office-hit.jpg" width="420" alt="Сертификат: Pick the Next Box Office Hit, Google Applied Digital Skills" />

</details>

<details>
<summary>Program a Progress Bar · 24 юли 2026</summary>

<img src="assets/certificates/lessons/program-a-progress-bar.jpg" width="420" alt="Сертификат: Program a Progress Bar, Google Applied Digital Skills" />

</details>

<details>
<summary>Wage a Sea Battle with Google Sheets · 24 юли 2026</summary>

<img src="assets/certificates/lessons/wage-a-sea-battle-with-google-sheets.jpg" width="420" alt="Сертификат: Wage a Sea Battle with Google Sheets, Google Applied Digital Skills" />

</details>

<details>
<summary>Work with Fractions In Google Sheets · 24 юли 2026</summary>

<img src="assets/certificates/lessons/work-with-fractions-in-google-sheets.jpg" width="420" alt="Сертификат: Work with Fractions In Google Sheets, Google Applied Digital Skills" />

</details>

</details>

<details>
<summary><b>AI и дигитална сигурност · 10</b></summary>

<details>
<summary>Avoid Online Scams · 24 юли 2026</summary>

<img src="assets/certificates/lessons/avoid-online-scams.jpg" width="420" alt="Сертификат: Avoid Online Scams, Google Applied Digital Skills" />

</details>

<details>
<summary>Build Healthy Digital Habits · 24 юли 2026</summary>

<img src="assets/certificates/lessons/build-healthy-digital-habits.jpg" width="420" alt="Сертификат: Build Healthy Digital Habits, Google Applied Digital Skills" />

</details>

<details>
<summary>Create a Responsible Blog with Google Sites · 25 юли 2026</summary>

<img src="assets/certificates/lessons/create-a-responsible-blog-with-google-sites.jpg" width="420" alt="Сертификат: Create a Responsible Blog with Google Sites, Google Applied Digital Skills" />

</details>

<details>
<summary>Create and Safeguard Passwords · 23 юли 2026</summary>

<img src="assets/certificates/lessons/create-and-safeguard-passwords.jpg" width="420" alt="Сертификат: Create and Safeguard Passwords, Google Applied Digital Skills" />

</details>

<details>
<summary>Discover AI in Daily Life · 23 юли 2026</summary>

<img src="assets/certificates/lessons/discover-ai-in-daily-life.jpg" width="420" alt="Сертификат: Discover AI in Daily Life, Google Applied Digital Skills" />

</details>

<details>
<summary>Evaluate Credibility of Online Sources · 25 юли 2026</summary>

<img src="assets/certificates/lessons/evaluate-credibility-of-online-sources.jpg" width="420" alt="Сертификат: Evaluate Credibility of Online Sources, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Generative AI · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-generative-ai.jpg" width="420" alt="Сертификат: Explore a Topic: Generative AI, Google Applied Digital Skills" />

</details>

<details>
<summary>Explore a Topic: Technology, Ethics, and Security · 25 юли 2026</summary>

<img src="assets/certificates/lessons/explore-a-topic-technology-ethics-and-security.jpg" width="420" alt="Сертификат: Explore a Topic: Technology, Ethics, and Security, Google Applied Digital Skills" />

</details>

<details>
<summary>Identify Cyberbullying · 25 юли 2026</summary>

<img src="assets/certificates/lessons/identify-cyberbullying.jpg" width="420" alt="Сертификат: Identify Cyberbullying, Google Applied Digital Skills" />

</details>

<details>
<summary>Understand Your Digital Footprint · 24 юли 2026</summary>

<img src="assets/certificates/lessons/understand-your-digital-footprint.jpg" width="420" alt="Сертификат: Understand Your Digital Footprint, Google Applied Digital Skills" />

</details>

</details>

</details>

<sub>Номерата на сертификатите и QR кодовете са скрити; данни за проверка се предоставят при запитване.</sub>

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
