#!/usr/bin/env python3
"""Render local SVGs from public GitHub activity and an aggregate language snapshot.
No private repository names, tokens, commit messages or account events are stored.
"""
import argparse
import json
import re
import urllib.request
from datetime import date, datetime, timedelta
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
USER = 'yavordfgggdag'

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

def txt(x,y,value,size=20,color='#edf3ff',weight=400,extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(str(value))}</text>'

def svg(w,h,title,content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(title)}. Source: GitHub. Motion is decorative, never simulated activity.</desc><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0c1023"/><stop offset=".6" stop-color="#17132e"/><stop offset="1" stop-color="#082f37"/></linearGradient><linearGradient id="accent"><stop stop-color="#aa91ff"/><stop offset=".5" stop-color="#6fb7ff"/><stop offset="1" stop-color="#51e4cb"/></linearGradient></defs><style>text{{font-family:Arial,Helvetica,sans-serif}}.signal{{stroke-dasharray:18 220;animation:signal 18s linear infinite}}.pulse{{animation:pulse 6s ease-in-out infinite}}@keyframes signal{{to{{stroke-dashoffset:-714}}}}@keyframes pulse{{50%{{opacity:.4}}}}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style><rect width="{w}" height="{h}" rx="20" fill="url(#bg)"/><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="19" stroke="#394761" fill="none"/>{content}</svg>'''

def activity(days, today, lang, mobile):
    bg = lang == 'bg'; s = stats(days,today); w = 520 if mobile else 1000
    title = 'Ритъмът на работата.' if bg else 'The rhythm behind the work.'
    b = txt(28,38,'GITHUB / ACTIVITY',13,'#91a5c8',700, 'letter-spacing="2"')
    b += txt(28,84,title,29 if mobile else 35,'#f3f5ff',700)
    labels = ['ПРИНОСИ','АКТИВНИ ДНИ','ТЕКУЩ STREAK','НАЙ-ДЪЛЪГ STREAK'] if bg else ['CONTRIBUTIONS','ACTIVE DAYS','CURRENT STREAK','LONGEST STREAK']
    vals = [s['total'],s['active'],s['current'],s['longest']]
    for i,(label,value) in enumerate(zip(labels,vals)):
        x=28+(i%2)*242 if mobile else 28+i*242
        y=112+(i//2)*132 if mobile else 115
        b += f'<rect x="{x}" y="{y}" width="222" height="116" rx="12" fill="#111c31" stroke="#3c4864"/>'
        b += txt(x+16,y+29,label,12,'#a8bad4',700)+txt(x+16,y+84,value,43,'#a9a3ff' if i<2 else '#66e4cf',700)
    y=414 if mobile else 285
    last=s['last'] or ('няма' if bg else 'none')
    b += txt(28,y,('Последен принос: ' if bg else 'Last contribution: ')+last,19,'#e1e9fa',700)
    b += txt(28,y+30,('Последни 30 дни: ' if bg else 'Last 30 days: ')+str(s['month']),17,'#a1b8d5')
    # Calendar remains factual and static; only the line below it moves.
    visible=days[-182:] if mobile else days
    start=date.fromisoformat(visible[0]['date']); start -= timedelta(days=(start.weekday()+1)%7)
    step=17 if mobile else 17; cell=13; ox=28; oy=y+70
    maxval=max(d['count'] for d in days) or 1
    for d in visible:
        dt=date.fromisoformat(d['date']); pos=(dt-start).days; c=d['count']
        level=0 if c==0 else min(4,1+int(c/maxval*3))
        fill=['#243149','#48427a','#6f60ab','#628ece','#5cdbc7'][level]
        x=ox+(pos//7)*step; yy=oy+(pos%7)*step
        b+=f'<rect x="{x}" y="{yy}" width="{cell}" height="{cell}" rx="3" fill="{fill}"><title>{d["date"]}: {c}</title></rect>'
    foot=oy+145
    b+=txt(28,foot,('Календар: ' if bg else 'Calendar: ')+visible[0]['date']+' → '+visible[-1]['date'],14,'#9aafca')
    b+=f'<path d="M28 {foot+25}H{w-28}" stroke="#354962"/><path class="signal" d="M28 {foot+25}H{w-28}" stroke="url(#accent)" stroke-width="2"/>'
    b+=txt(28,foot+53,('Публични GitHub приноси · обновено ' if bg else 'Public GitHub calendar · updated ')+today.isoformat(),13,'#a7b8cf')
    return svg(w,foot+80,title,b)

def languages(data,lang,mobile):
    bg=lang=='bg';w=520 if mobile else 1000
    items=data['languages'];total=sum(d['bytes'] for d in items)
    if total<=0:raise ValueError('Empty language snapshot')
    top=items[:6]
    other=sum(i['bytes'] for i in items[6:])
    if other:top=top+[{'name':'Други' if bg else 'Other','bytes':other}]
    b=txt(28,38,'CODE / LANGUAGE MIX',13,'#91a5c8',700,'letter-spacing="2"')
    b+=txt(28,83,'Езиците зад проектите.' if bg else 'The languages behind the products.',28 if mobile else 34,'#f3f5ff',700)
    b+=txt(28,116,'Дял от обема код · без профилното хранилище' if bg else 'Share of code bytes · profile repository excluded',16,'#a7b8d5')
    colors=['#a895ff','#61c7f2','#65deca','#e6b97c','#f497b2','#80a7ec','#69778f']
    for i,(row,color) in enumerate(zip(top,colors)):
        y=163+i*65; pct=row['bytes']/total*100
        b+=txt(28,y,row['name'],21,'#edf2ff',700)+txt(w-30,y,f'{pct:.1f}%',20,color,700,'text-anchor="end"')
        b+=f'<rect x="28" y="{y+13}" width="{w-56}" height="9" rx="4.5" fill="#28334a"/><rect x="28" y="{y+13}" width="{(w-56)*pct/100:.2f}" height="9" rx="4.5" fill="{color}"/>'
    y=163+len(top)*65
    b+=txt(28,y,('Измерено: ' if bg else 'Measured: ')+data['snapshot_date'],15,'#adbed6')
    b+=txt(28,y+27,'Обем код, не време или ниво на умения.' if bg else 'Code volume, not time spent or proficiency.',15,'#a1b3ce')
    return svg(w,y+55,'Езици по обем код' if bg else 'Languages by code volume',b)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--calendar-file',type=Path);ap.add_argument('--today',type=date.fromisoformat);a=ap.parse_args()
    today=a.today or datetime.now(ZoneInfo('Europe/Sofia')).date()
    if a.calendar_file:html=a.calendar_file.read_text()
    else:
        req=urllib.request.Request(f'https://github.com/users/{USER}/contributions',headers={'User-Agent':'Yavor-Profile-Metrics/1.0'})
        with urllib.request.urlopen(req,timeout=40) as response:html=response.read().decode()
    parser=CalendarParser();parser.feed(html);days=parser.days()
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
