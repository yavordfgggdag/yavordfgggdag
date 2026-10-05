<p align="right"><a href="https://github.com/yavordfgggdag">EN · English</a> &nbsp; / &nbsp; <b>BG · Български</b></p>

<img src="assets/banner.svg" alt="Yavor — Websites. Software. Games. Available for paid projects." width="100%" />

**Аз съм Явор.** Разработвам уеб и настолен софтуер, сайтове и инструменти за бизнеси и общности.

**Приемам платени проекти.** [Нека обсъдим вашия →](mailto:Fraisbg1@gmail.com)

[Работа](#work) · [Езици и инструменти](#toolkit) · [Услуги](#services) · [Активност](#activity) · [Контакт](#contact)

<a name="work"></a><a name="before-i-deploy"></a>

## Before I Deploy

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/screens/bid-mobile.svg" />
<img src="assets/journal/screens/bid.svg" alt="Реален Before I Deploy с демонстрационен проект; на тесен екран се показва детайл от същия desktop кадър." width="100%" />
</picture>

Нативно macOS приложение за проверки и подготовка на уеб проекти за публикуване.

<sub>Реален кадър от разработката. При тесен екран: увеличен детайл от desktop интерфейса. [Целият кадър](assets/screens/before-i-deploy.jpg).</sub>

**Нативен интерфейс. Отделен модул за проверки.** Разработих SwiftUI интерфейса, командния Node.js модул и връзките между проверките, хостинга и облачните услуги. Резултатите достигат до приложението като NDJSON събития.

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/native-bg-mobile.svg" />
<img src="assets/journal/native-bg.svg" alt="Обяснителна схема: SwiftUI изпраща команди към Node.js и получава NDJSON събития; модулът проверява локалния проект. Движението не показва жив статус." width="100%" />
</picture>

**Техническите решения:** Git състояние, тайни ключове, зависимости, статичен анализ, типове, компилация и готовност на хостинга в общ процес; проверка за променени файлове след анализа; изрично потвърждение преди продукционно публикуване.

**Технологии:** Swift · SwiftUI · JavaScript · Node.js · Supabase · PostgreSQL · Deno Edge Functions

<details>
<summary><b>Галерия и още функционалности</b></summary>

Mission Control обединява състоянието на проектите, наблюдението на сайтове и SSL информацията. Командната палитра предоставя бърза навигация.

<img src="assets/screens/bid-mission-control.jpg" alt="Mission Control с демонстрационен проект и HTTP 404 инцидент; заснето състояние, не показател за резултат." width="100%" />

<img src="assets/screens/bid-command-palette.jpg" alt="Реалната командна палитра на Before I Deploy." width="100%" />

**AI помощ:** преглед и прилагане на предложени промени. Достъпността зависи от настройките на доставчика и външните услуги.

</details>

<sub>Продукт в активно развитие, с частен код. Снимките не означават публично издание или проверка на всяка външна интеграция.</sub>

---

<a name="tlr-police-portal"></a>

## TLR Police Portal

Вътрешен портал за полицейския отдел на FiveM roleplay общността The Last Republic. Разработих таблото, търсачката на служители, йерархията на званията, наръчника и управлението на сертификати, наказания и позивни.

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/screens/police-mobile.svg" />
<img src="assets/journal/screens/police.svg" alt="Реално табло на TLR Police Portal със скрити лични данни. Мобилният вариант е детайл с радиокодовете от desktop кадъра." width="100%" />
</picture>

<sub>На тесен екран: детайл с радиокодовете от същия кадър. [Цялото табло](assets/screens/police-dashboard.jpg).</sub>

**Постоянната връзка има собствен процес.** Отделен Node.js бот поддържа Discord Gateway връзката и синхронизира данните за състава в Postgres. Next.js порталът извършва административните действия със сървърни проверки на правата и журнал. Двата компонента използват обща карта на ролите.

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/sync-bg-mobile.svg" />
<img src="assets/journal/sync-bg.svg" alt="Архитектура: Discord бот, Postgres и Next.js портал. Схематична синхронизация, не жива активност." width="100%" />
</picture>

**Технологии:** TypeScript · Next.js · React · Tailwind CSS · PostgreSQL / Neon · Drizzle ORM · Node.js · discord.js

<details>
<summary><b>Галерия — състав, звания и наръчник</b></summary>

<img src="assets/screens/police-employees.jpg" alt="Управление на състава; личните записи са скрити." width="100%" />

<img src="assets/screens/police-ranks.jpg" alt="Реална йерархия на званията." width="100%" />

<img src="assets/screens/police-handbook.jpg" alt="Реален интерактивен наръчник." width="100%" />

</details>

<details>
<summary><b>Реална навигация в наръчника — кратък GIF</b></summary>

<picture>
<source media="(prefers-reduced-motion: reduce)" srcset="assets/screens/police-handbook.jpg" />
<img src="assets/screens/handbook-navigation.gif" alt="Три реално заснети страници от навигацията в наръчника." width="100%" />
</picture>

[Статичен кадър](assets/screens/police-handbook.jpg).

</details>

<sub>Кадри от предишната проверка. Достъпът изисква Discord вход и членство в отдела. Актуалният вход се уточнява; кодът е частен.</sub>

---

<a name="client-websites"></a>

## Клиентска работа

### Помощ от приятел · Образователен център

Сайт, който помага на родителите да разгледат уроците по БЕЛ и математика и да изпратят запитване. Включва формати на обучение, често задавани въпроси и форма за контакт.

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/screens/education-mobile.svg" />
<img src="assets/journal/screens/education.svg" alt="Реален кадър от Помощ от приятел; тесният вариант е детайл от същата снимка." width="680" />
</picture>

**Компоненти, документирани при предишния преглед:** WordPress · WPForms. Формата е разгледана без изпращане на лични данни.

[Посетете сайта →](https://pomoshtotpriyatel.com/) · [Целият кадър](assets/screens/client-education.jpg)

<details>
<summary><b>Въпроси и отговори — реален кадър</b></summary>

<img src="assets/screens/client-education-faq.jpg" alt="Често задавани въпроси с разгънат отговор." width="100%" />

</details>

### Автоинструктор Господинов

Клиентски сайт за онлайн представяне на автоинструктор. **Очаква потвърждение:** точен адрес, актуални снимки, обхват и технологии.

<a name="the-last-republic"></a>

### The Last Republic

Основен сайт за FiveM общността. Работата включва публичен интерфейс, правила и кандидатстване, свързано с Discord. **Актуалният адрес и версия предстои да се потвърдят.** Старите начални страници и Minecraft интерфейсът не се представят като текущия основен сайт.

<details>
<summary><b>Допълнителна работа и експерименти</b></summary>

**Общностна платформа.** Отделна React реализация с Minecraft SMP и Factions интерфейс. Техническите решения включват React Router, зареждане на страници при нужда, TanStack Query и Supabase интеграции. Снимките са от локален преглед без продукционните услуги; не доказват работещ сървър, плащане или публичен вход.

<img src="assets/screens/community-platform.jpg" alt="Локален Minecraft интерфейс; не е актуалният основен сайт на The Last Republic." width="100%" />

<img src="assets/screens/community-rules.jpg" alt="Локален център с правила на общностната платформа." width="100%" />

**Технологии:** TypeScript · React · Vite · Tailwind CSS · shadcn/ui · React Router · TanStack Query · Supabase.

**Space Control.** Експеримент с HTML, JavaScript и Canvas API. В предишния преглед липсват посочени файлове за оформление и скриптове; не е представен като завършен продукт. Кодът на тези проекти е частен.

</details>

---

<a name="toolkit"></a>

## Езици, инструменти и среда за разработка

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/toolkit-bg-mobile.svg" />
<img src="assets/journal/toolkit-bg.svg" alt="Технологии от представените проекти: Swift и SwiftUI; TypeScript, React и Next.js; Postgres, Drizzle, Supabase и discord.js." width="100%" />
</picture>

### Реализиран опит — свързан с конкретна работа

| Контекст | Инструменти и роля |
| :--- | :--- |
| Нативно приложение | Swift / SwiftUI — macOS интерфейс; Node.js / JavaScript — проверки; NDJSON — събития |
| Портал и интеграции | TypeScript / React / Next.js — интерфейс и сървърна логика; Tailwind CSS — оформление; discord.js — бот |
| Данни и облачни услуги | PostgreSQL / Neon / Drizzle; Supabase / Deno Edge Functions — според проекта |
| Клиентски сайт | WordPress / WPForms — документираните компоненти на „Помощ от приятел“ |

### Пълна колекция — допълнителни технологии и интереси

Запазен е целият набор от езици и инструменти от профила. Тази колекция включва допълнителни интереси и възможни технологични избори; не означава еднакъв опит или завършени продукти с всеки инструмент. Реализираният опит е посочен по-горе.

**Допълнителни инструменти и интереси**  
TypeScript · JavaScript · Python · Lua · HTML5 · CSS3 · SQL · Node.js · Astro · MySQL · MariaDB · Git · GitHub

**Други програмни езици**  
C · C++ · C# · Java · Kotlin · Swift · Go · Rust · PHP · Ruby · Dart · Scala · R · Bash · PowerShell · Elixir · Erlang · Haskell · Clojure · F# · Julia · Zig · Solidity · GDScript · Objective-C · Perl · OCaml

**Уеб технологии и приложения**  
React · Next.js · Vue.js · Svelte · Vite · Tailwind CSS · Express · Electron · Flutter · .NET

**Данни, инфраструктура и публикуване**  
PostgreSQL · SQLite · MongoDB · Redis · Docker · Linux · macOS · Netlify · GitHub Actions · NGINX

**Игри, общности и AI**  
Discord · FiveM · Godot · Unity · Unreal Engine · OpenAI · Claude · Cursor

---

<a name="services"></a>

## За какво можете да ме наемете

- **Сайтове и онлайн магазини:** фирмено представяне, каталози, поръчки и резервации.
- **Уеб и настолен софтуер:** административни панели, портали и вътрешни инструменти.
- **Discord, игри и FiveM:** ботове, игрови системи и инструменти за общности.
- **API, автоматизации и AI:** свързване на услуги, обработка на данни и AI функционалности.
- **Поддръжка и развитие:** нови функции, поправки, оптимизация и подготовка за публикуване.

Това са **предлагани услуги**. Обхватът, срокът и цената се уточняват за конкретния проект.

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

**Обхватът се уточнява за всеки проект.** Функциите, платформите, срокът и цената зависят от договорените изисквания. Това са предлагани услуги; конкретният реализиран опит е показан в проектите по-долу.

</details>

---

<a name="activity"></a>

## Активност и обем код

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/metrics/activity-bg-mobile.svg" />
<img src="assets/journal/metrics/activity-bg.svg" alt="GitHub приноси: текущ и най-дълъг streak, активни дни, последен принос, 30-дневна активност и календар." width="100%" />
</picture>

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/metrics/languages-bg-mobile.svg" />
<img src="assets/journal/metrics/languages-bg.svg" alt="Датирана снимка на езиците по обем код, не по време или умения." width="100%" />
</picture>

<details>
<summary><b>Как се изчисляват показателите</b></summary>

Активността се обновява ежедневно от публичния календар на GitHub. Приносите не са само commit-и и не показват часове работа. „Последен принос“ е последният активен ден в календара, а не последно влизане в профила. GitHub може да обновява календара със закъснение.

Текущата поредица брои последователните активни дни до днес или вчера, ако днешният ден още няма принос. Най-дългата поредица, приносите и активните дни са в показания годишен период. Мобилният календар показва последните 26 седмици; общите показатели остават за годишния период.

Езиковите дялове са отделна снимка от 2026-10-05 на обема код според GitHub, включително частните проекти и без профилното хранилище. Това не измерва честота, време или умения. Езиковата снимка не се обновява автоматично: публичната задача няма достъп до частния код.

[GitHub contribution rules](https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference) · [Metrics source](scripts/update_metrics.py)

</details>

---

<a name="process"></a>

## Как работим заедно

<picture>
<source media="(max-width: 600px)" srcset="assets/journal/process-bg-mobile.svg" />
<img src="assets/journal/process-bg.svg" alt="Обхват, дизайн, разработка, проверка и публикуване. Декоративно движение, не отчет за напредък." width="100%" />
</picture>

Започваме с целите, потребителите и изискванията. Уточняваме интерфейса, архитектурата и обхвата; разработваме функциите и интеграциите; проверяваме поведението и подготовката за публикуване. Следват документация и договорените подобрения.

<details>
<summary><b>Принципи на работа</b></summary>

Дизайн според нуждите на хората · Ясна архитектура · Обмислени права и контрол на достъпа · Практически проверки · Полезна автоматизация · Договорени изисквания и очаквания.

</details>

---

<a name="contact"></a>

## Нека обсъдим вашия проект.

Изпратете **идеята, основните функции, желания срок и ориентировъчния бюджет**. Ще уточним обхвата и индивидуална оферта.

**[Fraisbg1@gmail.com](mailto:Fraisbg1@gmail.com)**  
Телефон: **+359898634678**  
Discord: **Fraisbg**  
Instagram: **[@y.yakowvw.sales](https://www.instagram.com/y.yakowvw.sales/)**

[EN · English](https://github.com/yavordfgggdag) · **BG · Български**

<sub>Изходният код на проектите е частен. [Произход на кадрите и бележки за достъпност](assets/README.md). Оригиналният банер и оригиналните изображения са запазени.</sub>
