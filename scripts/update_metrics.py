#!/usr/bin/env python3
"""Render local SVGs from public GitHub activity and an aggregate language snapshot.
No private repository names, tokens, commit messages or account events are stored.
"""
import argparse
import json
import re
import urllib.request
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
USER = 'yyakowvw'

class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.cells = {}; self.tips = {}; self.tip = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'td' and a.get('data-date') and a.get('id'):
            self.cells[a['id']] = a['data-date']
        if tag == 'tool-tip' and a.get('for'):
            self.tip = a['for']; self.tips[self.tip] = ''
    def handle_data(self, value):
        if self.tip: self.tips[self.tip] += value
    def handle_endtag(self, tag):
        if tag == 'tool-tip': self.tip = None
    def days(self):
        result = []
        for key, day in self.cells.items():
            label = self.tips.get(key, '').strip()
            match = re.match(r'([\d,]+) contributions? on ', label)
            if label.startswith('No contributions on '): count = 0
            elif match: count = int(match[1].replace(',', ''))
            else: raise ValueError(f'Unrecognized contribution label for {day}')
            result.append({'date': day, 'count': count})
        result.sort(key=lambda d: d['date'])
        if len(result) < 300: raise ValueError('Incomplete public contribution calendar')
        for a, b in zip(result, result[1:]):
            if date.fromisoformat(b['date']) - date.fromisoformat(a['date']) != timedelta(days=1):
                raise ValueError('Non-contiguous calendar')
        return result

def stats(days, today):
    days = [d for d in days if date.fromisoformat(d['date']) <= today]
    counts = {date.fromisoformat(d['date']): d['count'] for d in days}
    active = [d for d in days if d['count'] > 0]
    longest = run = 0
    for d in days:
        run = run + 1 if d['count'] else 0
        longest = max(longest, run)
    cursor = today if counts.get(today, 0) else today - timedelta(days=1)
    current = 0
    while counts.get(cursor, 0):
        current += 1; cursor -= timedelta(days=1)
    return dict(total=sum(d['count'] for d in days), active=len(active), longest=longest,
                current=current, last=active[-1]['date'] if active else None,
                month=sum(d['count'] for d in days if date.fromisoformat(d['date']) >= today-timedelta(days=29)))

from profile_style import C, document, linear, radial, text as txt, wrap

HEAT = ['#2B2463', '#4C2F9E', '#8B5CF6', '#EC4899', '#FBBF24']
MONTHS = {'en': 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(),
          'bg': 'яну фев мар апр май юни юли авг сеп окт ное дек'.split()}


def panel(w, h, title, desc, body, extra_defs='', motion=''):
    """Shared studio frame; motion is decorative and never simulates activity."""
    defs = (linear('bg', [(0, C['night']), (.55, '#161045'), (1, C['deep'])], x2=1, y2=1)
            + linear('accent', [(0, C['violet']), (.5, C['cyan']), (1, C['mint'])])
            + radial('au1', C['violet'], .38) + radial('au2', C['cyan'], .26) + extra_defs)
    motion = ('.aur{animation:aur 28s ease-in-out infinite}@keyframes aur{50%{transform:translate(-70px,30px)}}'
              f'.signal{{animation:signal 12s cubic-bezier(.6,0,.3,1) infinite}}@keyframes signal{{0%{{transform:translateX(0);opacity:0}}10%{{opacity:1}}85%{{opacity:1}}100%{{transform:translateX({w - 200}px);opacity:0}}}}' + motion)
    b = (f'<clipPath id="frame"><rect width="{w}" height="{h}" rx="28"/></clipPath><rect width="{w}" height="{h}" rx="28" fill="url(#bg)"/>'
         f'<g clip-path="url(#frame)"><g class="aur"><circle cx="{w * .85:.0f}" cy="{h * .1:.0f}" r="{w * .45:.0f}" fill="url(#au1)"/></g>'
         f'<circle cx="{w * .05:.0f}" cy="{h:.0f}" r="{w * .4:.0f}" fill="url(#au2)"/>'
         f'<rect width="{w}" height="4" fill="url(#accent)"/>{body}</g>')
    return document(w, h, title, desc + ' Source: GitHub. Motion is decorative, never simulated activity.', b, defs, motion)


def activity(days, today, lang, mobile):
    bg = lang == 'bg'; s = stats(days, today); w = 600 if mobile else 1200; x0 = 32 if mobile else 48
    title = 'Ритъмът на работата.' if bg else 'The rhythm behind the work.'
    b = txt(x0, 52, 'GITHUB · ПУБЛИЧНА АКТИВНОСТ' if bg else 'GITHUB · PUBLIC ACTIVITY', 17 if mobile else 13, C['cyan'], 800, spacing=2.4)
    b += txt(x0, 98, title, 32 if mobile else 38, C['text'], 800)
    labels = ['ПРИНОСИ', 'АКТИВНИ ДНИ', 'ТЕКУЩ STREAK', 'НАЙ-ДЪЛЪГ STREAK'] if bg else ['CONTRIBUTIONS', 'ACTIVE DAYS', 'CURRENT STREAK', 'LONGEST STREAK']
    vals = [s['total'], s['active'], s['current'], s['longest']]
    accents = [C['lilac'], C['pink'], C['mint'], C['amber']]
    if mobile:
        boxes = [(x0, 126, 260, 128), (x0 + 276, 126, 260, 128), (x0, 268, 260, 128), (x0 + 276, 268, 260, 128)]
    else:
        boxes = [(x0, 132, 330, 150), (x0 + 350, 132, 240, 150), (x0 + 610, 132, 240, 150), (x0 + 870, 132, 234, 150)]
    for i, ((x, y, bw, bh), label, value, col) in enumerate(zip(boxes, labels, vals, accents)):
        b += (f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="{26 if i == 0 else 20}" fill="#0E0B2C" fill-opacity=".78" stroke="{col}" stroke-opacity=".55"/>'
              f'<rect x="{x + 18}" y="{y}" width="{bw - 36}" height="3" rx="1.5" fill="{col}"/>')
        b += txt(x + 20, y + 36, label, 16 if mobile else 13, C['soft'], 800, spacing=1.2)
        b += txt(x + 20, y + bh - 26, value, (54 if mobile else (74 if i == 0 else 60)), col, 800)
    y = 438 if mobile else 330
    last = s['last'] or ('няма' if bg else 'none')
    b += f'<circle cx="{x0 + 7}" cy="{y - 6}" r="6" fill="{C["mint"]}"/>'
    b += txt(x0 + 22, y, ('Последен принос: ' if bg else 'Last contribution: ') + last, 22 if mobile else 19, C['text'], 700)
    b += txt(x0 + 22, y + 30, ('Последни 30 дни: ' if bg else 'Last 30 days: ') + str(s['month']), 19 if mobile else 16, C['muted'])
    # Calendar remains factual and static; only the line under it moves.
    visible = days[-182:] if mobile else days
    start = date.fromisoformat(visible[0]['date']); start -= timedelta(days=(start.weekday() + 1) % 7)
    step, cell = (19, 15) if mobile else (19, 15)
    ox, oy = x0 + (6 if mobile else 0), y + 76
    maxval = max(d['count'] for d in days) or 1
    seen = set()
    for d in visible:
        dt = date.fromisoformat(d['date']); pos = (dt - start).days; c = d['count']
        level = 0 if c == 0 else min(4, 1 + int(c / maxval * 3))
        x = ox + (pos // 7) * step; yy = oy + (pos % 7) * step
        if dt.day <= 7 and (dt.year, dt.month) not in seen and pos % 7 == 0:
            seen.add((dt.year, dt.month))
            b += txt(x, oy - 10, MONTHS[lang][dt.month - 1], 16 if mobile else 12, C['muted'])
        b += f'<rect x="{x}" y="{yy}" width="{cell}" height="{cell}" rx="4" fill="{HEAT[level]}"><title>{d["date"]}: {c}</title></rect>'
    foot = oy + 7 * step + 30
    lx = x0
    b += txt(lx, foot, ('Календар: ' if bg else 'Calendar: ') + visible[0]['date'] + ' → ' + visible[-1]['date'], 18 if mobile else 14, C['muted'])
    if not mobile:
        b += txt(w - 48 - 5 * 22 - 60, foot, 'по-малко' if bg else 'less', 12, C['muted'], anchor='end')
        for i, col in enumerate(HEAT):
            b += f'<rect x="{w - 48 - 5 * 22 - 50 + i * 22}" y="{foot - 12}" width="15" height="15" rx="4" fill="{col}"/>'
        b += txt(w - 48, foot, 'повече' if bg else 'more', 12, C['muted'], anchor='end')
    b += f'<path d="M{x0} {foot + 24}H{w - x0}" stroke="#3B3378"/><rect class="live signal" x="{x0}" y="{foot + 22}" width="140" height="4" rx="2" fill="#E0FBFF"/>'
    b += txt(x0, foot + 56, ('Публични GitHub приноси · обновено ' if bg else 'Public GitHub calendar · updated ') + today.isoformat(), 17 if mobile else 13, C['muted'])
    return panel(w, foot + 80, title, title, b)


def languages(data, lang, mobile):
    bg = lang == 'bg'; w = 600 if mobile else 1200; x0 = 32 if mobile else 48
    items = data['languages']; total = sum(d['bytes'] for d in items)
    if total <= 0: raise ValueError('Empty language snapshot')
    top = [dict(i) for i in items[:6]]
    other = sum(i['bytes'] for i in items[6:])
    if other: top.append({'name': 'Други' if bg else 'Other', 'bytes': other, 'color': '#8B8FB0'})
    title = 'Езиците зад проектите.' if bg else 'The languages behind the products.'
    b = txt(x0, 52, 'КОД · ЕЗИКОВ МИКС' if bg else 'CODE · LANGUAGE MIX', 17 if mobile else 13, C['pink'], 800, spacing=2.4)
    b += txt(x0, 98, title, 30 if mobile else 38, C['text'], 800)
    sub = 'Дял от обема код · без профилното хранилище' if bg else 'Share of code bytes · profile repository excluded'
    b += txt(x0, 130, sub, 16, C['muted']) if not mobile else ''.join(txt(x0, 130 + i * 22, line, 18, C['muted']) for i, line in enumerate(wrap(sub, 40)))
    # one stacked bar in the original GitHub language colours
    bx, bw, x = x0, w - 2 * x0, x0
    top_y = 158 if not mobile else 172
    b += f'<clipPath id="bar"><rect x="{bx}" y="{top_y}" width="{bw}" height="22" rx="11"/></clipPath><g clip-path="url(#bar)">'
    for row in top:
        seg = bw * row['bytes'] / total
        b += f'<rect x="{x:.2f}" y="{top_y}" width="{seg + .5:.2f}" height="22" fill="{row["color"]}"/>'
        x += seg
    b += f'<rect class="live sweep" x="{bx - 120}" y="{top_y}" width="120" height="22" fill="url(#sweep)"/></g>'
    for i, row in enumerate(top):
        y = top_y + 78 + i * 58; pct = row['bytes'] / total * 100
        b += f'<circle cx="{x0 + 8}" cy="{y - 7}" r="8" fill="{row["color"]}" stroke="#fff" stroke-opacity=".35"/>'
        b += txt(x0 + 26, y, row['name'], 21, C['text'], 700) + txt(w - x0, y, f'{pct:.1f}%', 20, C['soft'], 700, anchor='end')
        b += (f'<rect x="{x0}" y="{y + 13}" width="{bw}" height="8" rx="4" fill="#2A2457"/>'
              f'<rect x="{x0}" y="{y + 13}" width="{max(bw * pct / 100, 8):.2f}" height="8" rx="4" fill="{row["color"]}"/>')
    y = top_y + 78 + len(top) * 58 + 8
    fs = 18 if mobile else 15
    b += txt(x0, y, ('Измерено: ' if bg else 'Measured: ') + data['snapshot_date'], fs, C['soft'])
    b += txt(x0, y + 28, 'Обем код, не време или ниво на умения.' if bg else 'Code volume, not time spent or proficiency.', fs, C['muted'])
    defs = linear('sweep', [(0, '#fff', 0), (.5, '#fff', .5), (1, '#fff', 0)])
    motion = f'.sweep{{animation:sweep 9s ease-in-out infinite}}@keyframes sweep{{0%,15%{{transform:translateX(0)}}60%,100%{{transform:translateX({bw + 240}px)}}}}'
    return panel(w, y + 56, 'Езици по обем код' if bg else 'Languages by code volume',
                 'Езици по обем код' if bg else 'Languages by code volume', b, defs, motion)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--calendar-file',type=Path);ap.add_argument('--today',type=date.fromisoformat)
    ap.add_argument('--from-saved',action='store_true',help='re-render visuals from data/activity.json without fetching');a=ap.parse_args()
    today=a.today or datetime.now(ZoneInfo('Europe/Sofia')).date()
    if a.from_saved:
        saved=json.loads((ROOT/'data/activity.json').read_text());days=saved['days'];today=a.today or date.fromisoformat(saved['updated'])
    elif a.calendar_file:html=a.calendar_file.read_text()
    else:
        req=urllib.request.Request(f'https://github.com/users/{USER}/contributions',headers={'User-Agent':'Yavor-Profile-Metrics/1.0'})
        with urllib.request.urlopen(req,timeout=40) as response:html=response.read().decode()
    if not a.from_saved:parser=CalendarParser();parser.feed(html);days=parser.days()
    days=[d for d in days if date.fromisoformat(d['date'])<=today]
    if (today-date.fromisoformat(days[-1]['date'])).days>2:raise ValueError('Stale calendar; preserving previous output')
    language=json.loads((ROOT/'data/languages.json').read_text())
    outputs={}
    for lang in ['en','bg']:
        for mobile in [False,True]:
            suffix=f'{lang}{"-mobile" if mobile else ""}.svg'
            outputs['activity-'+suffix]=activity(days,today,lang,mobile)
            outputs['languages-'+suffix]=languages(language,lang,mobile)
    # Validate all sources before replacing any successful output.
    folder=ROOT/'assets/metrics';folder.mkdir(exist_ok=True)
    for name,value in outputs.items():(folder/name).write_text(value)
    (ROOT/'data/activity.json').write_text(json.dumps({'source':f'https://github.com/users/{USER}/contributions','updated':today.isoformat(),'days':days,'summary':stats(days,today)},indent=2)+'\n')
    print(json.dumps(stats(days,today)))

if __name__=='__main__':main()
