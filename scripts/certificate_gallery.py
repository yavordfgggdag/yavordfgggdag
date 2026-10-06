#!/usr/bin/env python3
"""Write the "All 135 certificates" section of README.md and README.bg.md.

Each certificate sits in its own <details> block, ordered by importance: the six
featured certificates first, then the 129 Google lessons grouped by topic.
Images live in assets/certificates/ (numbers and QR codes covered).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = json.loads((ROOT / 'data/certificates.json').read_text())['collections'][0]['lessons']
MON = {'en': 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(), 'bg': 'яну фев мар апр май юни юли авг сеп окт ное дек'.split()}
FEATURED = [
    ('1-gemini-certified-educator', 'Gemini Certified Educator', 'Google for Education',
     {'en': 'issued 23 Jul 2026 · valid until 23 Jul 2029', 'bg': 'издаден 23 юли 2026 · валиден до 23 юли 2029'}),
    ('2-google-ads-ai-powered-performance-ads', 'AI-Powered Performance Ads', 'Google Ads',
     {'en': 'issued 21 Jul 2026 · valid until 21 Jul 2027', 'bg': 'издаден 21 юли 2026 · валиден до 21 юли 2027'}),
    ('3-hubspot-digital-marketing', 'Digital Marketing Certified', 'HubSpot Academy',
     {'en': 'issued 24 Jul 2026 · valid until 23 Aug 2027', 'bg': 'издаден 24 юли 2026 · валиден до 23 авг 2027'}),
    ('4-advance-academy-digital-marketing-specialist', 'Digital Marketing Specialist', 'Advance Academy',
     {'en': 'program Feb–Apr 2026 · issued 30 Apr 2026', 'bg': 'програма февр.–апр. 2026 · издаден 30 апр 2026'}),
    ('5-google-fundamentals-of-digital-marketing', 'Fundamentals of Digital Marketing', 'Google',
     {'en': 'completed 27 Jul 2026', 'bg': 'завършен 27 юли 2026'}),
    ('6-google-intro-to-gemini', 'Intro to Gemini', 'Google AI Educator Series', {'en': 'foundational badge', 'bg': 'базова значка'}),
]
TOPICS = [('creative', {'en': 'Creative & research', 'bg': 'Творчество и проучване'}),
          ('workspace', {'en': 'Google Workspace', 'bg': 'Google Workspace'}),
          ('career', {'en': 'Career & professional', 'bg': 'Кариера и професия'}),
          ('data_logic', {'en': 'Data & logic', 'bg': 'Данни и логика'}),
          ('ai_safety', {'en': 'AI & digital safety', 'bg': 'AI и дигитална сигурност'})]
T = {'en': {'head': '### 🏅 All 135 certificates', 'hint': 'Sorted by importance. Click a title to open the certificate.',
            'lessons': '7–135 · 129 Google Applied Digital Skills lessons', 'sub': 'completed 23–27 Jul 2026 · click a topic, then a lesson',
            'alt': 'Certificate', 'note': 'Certificate numbers and QR codes are hidden; verification details are available on request.',
            'end': '<a name="activity"></a>'},
     'bg': {'head': '### 🏅 Всички 135 сертификата', 'hint': 'Подредени по важност. Натиснете заглавие, за да отворите сертификата.',
            'lessons': '7–135 · 129 урока от Google Applied Digital Skills', 'sub': 'завършени 23–27 юли 2026 · натиснете тема, после урок',
            'alt': 'Сертификат', 'note': 'Номерата на сертификатите и QR кодовете са скрити; данни за проверка се предоставят при запитване.',
            'end': '<a name="активност"></a>'}}


def slug(value):
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')


def date(value, lang):
    return f'{int(value[8:])} {MON[lang][int(value[5:7]) - 1]} {value[:4]}'


def section(lang):
    t = T[lang]
    out = [t['head'], '', t['hint'], '']
    for i, (name, title, issuer, when) in enumerate(FEATURED):
        out += ['<details>', f'<summary><b>{i + 1} · {title}</b> — {issuer} · {when[lang]}</summary>', '',
                f'<img src="assets/certificates/featured/{name}.jpg" width="100%" alt="{t["alt"]}: {title}, {issuer}" />', '', '</details>', '']
    out += ['<details>', f'<summary><b>{t["lessons"]}</b> — {t["sub"]}</summary>', '']
    for key, names in TOPICS:
        items = sorted((l for l in LESSONS if l['topic'] == key), key=lambda l: l['title'])
        out += ['<details>', f'<summary><b>{names[lang]} · {len(items)}</b></summary>', '']
        for lesson in items:
            out += ['<details>', f'<summary>{lesson["title"]} · {date(lesson["date"], lang)}</summary>', '',
                    f'<img src="assets/certificates/lessons/{slug(lesson["title"])}.jpg" width="420" '
                    f'alt="{t["alt"]}: {lesson["title"]}, Google Applied Digital Skills" />', '', '</details>', '']
        out += ['</details>', '']
    out += ['</details>', '', f'<sub>{t["note"]}</sub>', '', '']
    return '\n'.join(out)


if __name__ == '__main__':
    for name, lang in (('README.md', 'en'), ('README.bg.md', 'bg')):
        path = ROOT / name
        text = path.read_text()
        start, end = text.index(T[lang]['head']), text.index(T[lang]['end'])
        path.write_text(text[:start] + section(lang) + text[end:])
    print('certificate gallery written')
