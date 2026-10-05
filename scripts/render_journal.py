#!/usr/bin/env python3
"""Render the profile's local, bilingual artwork. Standard library only.

Presentation consumes the existing public activity data and fixed language snapshot.
No network, credentials, private repository names, or new metric definitions.
"""
import argparse
import base64
import json
from datetime import date, timedelta
from html import escape
from pathlib import Path
from update_metrics import stats

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/journal'
INK = '#0B1020'
TEXT = '#EEF2FF'
MUTED = '#B2BED5'
LINE = '#354560'
VIOLET = '#B8A1FF'
BLUE = '#83C9F4'
MINT = '#73DFCA'


def text(x, y, value, size=22, color=TEXT, weight=400, anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>'


def line(x1, y1, x2, y2, color=LINE, width=1, extra=''):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}" {extra}/>'


def svg(w, h, title, desc, body, animation=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><linearGradient id="wash" x2="1" y2="1"><stop stop-color="#151632"/><stop offset="1" stop-color="{INK}"/></linearGradient><linearGradient id="spectrum"><stop stop-color="{VIOLET}"/><stop offset=".52" stop-color="{BLUE}"/><stop offset="1" stop-color="{MINT}"/></linearGradient></defs>
<style>text{{font-family:Arial,Helvetica,sans-serif}}{animation}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}.travel,.return,.sweep{{display:none}}}}</style>
<rect width="{w}" height="{h}" fill="url(#wash)"/>
{body}
</svg>'''


def architecture(lang, mobile, kind):
    bg = lang == 'bg'
    w = 390 if mobile else 1000
    if kind == 'native':
        names = ['SwiftUI', 'Node.js', 'Local checks']
        labels = ['Нативен интерфейс', 'Модул за проверки', 'Локален проект'] if bg else ['Native interface', 'Check engine', 'Local project']
        names[2] = 'Проверки' if bg else 'Checks'
        kicker = '01 / КОМАНДИ И СЪБИТИЯ' if bg else '01 / COMMANDS & EVENTS'
        foot = 'Схема на архитектурата · не е жив статус' if bg else 'Architecture diagram · not live status'
        desc = 'SwiftUI sends commands to Node.js and receives NDJSON events. The engine checks local project files. Optional hosting and cloud integrations depend on setup.'
        bridge = ['команда →', '← NDJSON'] if bg else ['command →', '← NDJSON']
    else:
        names = ['Discord bot', 'Postgres', 'Next.js']
        labels = ['Постоянна връзка', 'Състав и журнал', 'Права и операции'] if bg else ['Persistent connection', 'Roster & audit data', 'Access & operations']
        kicker = '02 / СИНХРОНИЗАЦИЯ И ДОСТЪП' if bg else '02 / SYNC & ACCESS'
        foot = 'Схема на архитектурата · не е жив статус' if bg else 'Architecture diagram · not live status'
        desc = 'A separate Discord Gateway bot synchronizes roster data into Postgres. The Next.js portal reads data and performs authorized management operations. Both use a shared role map.'
        bridge = ['синхронизация →', 'данни ↔'] if bg else ['synchronize →', 'data ↔']
    colors = [VIOLET, BLUE, MINT]
    b = text(24 if mobile else 40, 35 if mobile else 40, kicker, 13 if mobile else 18, MUTED, 600)
    if mobile:
        for i, (name, label, color) in enumerate(zip(names, labels, colors)):
            y = 91 + i * 118
            b += f'<circle cx="36" cy="{y-7}" r="5" fill="{color}"/>'
            b += text(62, y, name, 27, color, 600) + text(62, y+27, label, 17)
            if i < 2:
                b += line(36, y+9, 36, y+96, LINE, 2)
                b += line(36, y+9, 36, y+96, color, 2, 'class="travel" pathLength="100"')
                b += text(62, y+68, bridge[i] if kind=='sync' else ('команда / NDJSON' if bg else 'command / NDJSON') if i==0 else ('локални проверки' if bg else 'local checks'), 14, MUTED)
        b += text(24, 407, foot, 13, MUTED)
        h = 430
    else:
        centers = [156, 500, 844]
        for i, (cx, name, label, color) in enumerate(zip(centers, names, labels, colors)):
            b += text(cx, 133, name, 35, color, 600, 'middle')
            b += text(cx, 169, label, 22, TEXT, anchor='middle')
            b += f'<circle cx="{cx}" cy="203" r="5" fill="{color}"/>'
            if i < 2:
                b += line(cx+14, 203, centers[i+1]-14, 203, LINE, 2)
                b += line(cx+14, 203, centers[i+1]-14, 203, color, 3, 'class="travel" pathLength="100"')
                b += text((cx+centers[i+1])/2, 239, bridge[i] if kind=='sync' else bridge[0] if i==0 else ('проверки →' if bg else 'checks →'), 17, MUTED, anchor='middle')
        if kind == 'native':
            b += line(486, 268, 170, 268, LINE, 1)
            b += line(486, 268, 170, 268, BLUE, 2, 'class="return" pathLength="100"')
            b += text(328, 297, bridge[1], 17, BLUE, anchor='middle')
        b += text(40, 335, foot, 16, MUTED)
        h = 360
    animation = '.travel{stroke-dasharray:8 192;animation:transit 14s ease-in-out infinite}.return{stroke-dasharray:8 192;animation:transit 14s ease-in-out 4s infinite}@keyframes transit{0%,12%{stroke-dashoffset:10}65%,100%{stroke-dashoffset:-105}}'
    return svg(w,h,kicker,desc,b,animation)


def toolkit(lang, mobile):
    bg=lang=='bg'; w=390 if mobile else 1000
    groups=[('NATIVE','Swift · SwiftUI','Node.js · NDJSON',VIOLET),('WEB','TypeScript · React','Next.js · Tailwind',BLUE),('DATA','Postgres · Drizzle','Supabase · discord.js',MINT)]
    b=text(24 if mobile else 40,36 if mobile else 42,'ТЕХНОЛОГИИ ЗАД ПРОЕКТИТЕ' if bg else 'TECHNOLOGY BEHIND THE WORK',13 if mobile else 18,MUTED,600)
    for i,(label,a,c,color) in enumerate(groups):
        x=24 if mobile else 40+i*328;y=85+i*112 if mobile else 97
        b+=text(x,y,label,14 if mobile else 17,color,600)
        b+=text(x,y+32,a,23 if mobile else 25,TEXT,600)
        b+=text(x,y+59,c,18 if mobile else 21,MUTED)
        b+=line(x,y+77,366 if mobile else x+280,y+77,color)
    return svg(w,410 if mobile else 208,'Технологии зад проектите' if bg else 'Technology behind the work','Selected technologies documented in the existing project descriptions. Full language and tool catalogue follows as selectable text.',b)


def screen(name, mobile):
    """Compose an exact viewport of an existing JPEG, without altering its pixels.

    Only legacy presentation headers are excluded on desktop. Mobile views are
    explicitly labelled as details in both READMEs, never as responsive app UI.
    Embedded bytes keep each SVG self-contained when loaded as an image on GitHub.
    """
    info={
        'bid':('before-i-deploy.jpg',1400,1104,(28,105,1344,934),(48,190,680,830),'Before I Deploy'),
        'police':('police-dashboard.jpg',1400,908,(28,105,1344,738),(610,475,377,190),'TLR Police Portal'),
        'education':('client-education.jpg',1400,1311,(28,105,1344,1139),(170,470,1000,742),'Помощ от приятел'),
    }
    file,iw,ih,desktop,narrow,title=info[name]
    x,y,cw,ch=narrow if mobile else desktop
    w=390 if mobile else 1000;h=round(w*ch/cw)
    data=base64.b64encode((ROOT/'assets/screens'/file).read_bytes()).decode()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)} — {'detail' if mobile else 'real capture'}</title><desc id="desc">Exact viewport of the existing redacted screenshot. No interface or data generated. {'This is a desktop screenshot detail, not a mobile application screenshot.' if mobile else 'Only the former decorative frame has been excluded.'}</desc><defs><clipPath id="clip"><rect width="{w}" height="{h}" rx="8"/></clipPath></defs><g clip-path="url(#clip)"><svg width="{w}" height="{h}" viewBox="{x} {y} {cw} {ch}"><image width="{iw}" height="{ih}" xlink:href="data:image/jpeg;base64,{data}"/></svg></g><rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="8" stroke="{LINE}" fill="none"/></svg>'''


def process(lang,mobile):
    bg=lang=='bg'; labels=['Обхват','Дизайн','Разработка','Проверка','Публикуване'] if bg else ['Scope','Design','Build','Verify','Release']
    w=390 if mobile else 1000
    b=text(24 if mobile else 40,36 if mobile else 40,'ОТ ЗАДАЧАТА ДО СЛЕДВАЩАТА ВЕРСИЯ' if bg else 'FROM BRIEF TO THE NEXT VERSION',13 if mobile else 17,MUTED,600)
    for i,label in enumerate(labels):
        x=24 if mobile else 40+i*191;y=85+i*61 if mobile else 100
        if mobile:
            b+=text(x,y,f'0{i+1}',15,[VIOLET,BLUE,MINT][i%3]) + text(65,y,label,24)
            if i<4:b+=line(31,y+10,31,y+37)
        else:
            b+=text(x,y,f'0{i+1}',18,[VIOLET,BLUE,MINT][i%3])+text(x,y+37,label,25)
    if not mobile:
        b+=line(40,164,960,164,LINE,2)+line(40,164,960,164,'url(#spectrum)',3,'class="sweep" pathLength="100"')
    return svg(w,360 if mobile else 195,'Процес на работа' if bg else 'Working process','Illustration of the working process, not a progress indicator.',b,'.sweep{stroke-dasharray:7 193;animation:sweep 20s ease-in-out infinite}@keyframes sweep{0%,8%{stroke-dashoffset:10}75%,100%{stroke-dashoffset:-105}}')


def activity(data,lang,mobile):
    bg=lang=='bg';w=390 if mobile else 1000;pad=24 if mobile else 40
    today=date.fromisoformat(data['updated']);days=data['days'];s=stats(days,today)
    b=text(pad,36 if mobile else 40,'GITHUB / АКТИВНОСТ' if bg else 'GITHUB / ACTIVITY',14 if mobile else 18,MUTED,600)
    labels=['Текущ streak','Най-дълъг streak','Активни дни','Приноси'] if bg else ['Current streak','Longest streak','Active days','Contributions']
    values=[s['current'],s['longest'],s['active'],s['total']]
    for i,(label,value) in enumerate(zip(labels,values)):
        x=pad+(i%2)*181 if mobile else pad+i*240;y=82+(i//2)*101 if mobile else 93
        b+=text(x,y,label,15 if mobile else 21,MUTED)+text(x,y+48,value,42 if mobile else 49,VIOLET if i<2 else MINT,600)
    y=285 if mobile else 190
    b+=line(pad,y-9,w-pad,y-9)
    b+=text(pad,y+20,('Последен принос: ' if bg else 'Last contribution: ')+(s['last'] or '—'),17 if mobile else 23)
    b+=text(pad,y+50,('Последни 30 дни: ' if bg else 'Last 30 days: ')+str(s['month']),17 if mobile else 23,MUTED)
    # Fit 27 visible calendar columns at 390 px; values retain annual scope.
    visible=days[-182:] if mobile else days
    start=date.fromisoformat(visible[0]['date']);start-=timedelta(days=(start.weekday()+1)%7)
    ncols=((date.fromisoformat(visible[-1]['date'])-start).days//7)+1
    step=(w-2*pad)/ncols;cell=step-3;top=y+80
    peak=max(d['count'] for d in days) or 1
    fills=['#25314A','#51446F','#79649F','#8F8BD2',MINT]
    for d in visible:
        n=(date.fromisoformat(d['date'])-start).days;c=d['count'];level=0 if c==0 else min(4,1+int(c/peak*3))
        b+=f'<rect x="{pad+n//7*step:.2f}" y="{top+n%7*step:.2f}" width="{cell:.2f}" height="{cell:.2f}" rx="2" fill="{fills[level]}"><title>{d["date"]}: {c}</title></rect>'
    foot=top+7*step+24
    if mobile:
        b+=text(pad,foot,('26 седмици · общите стойности са годишни' if bg else '26 weeks · totals use the annual window'),13,MUTED)
        b+=text(pad,foot+24,visible[0]['date']+' → '+visible[-1]['date'],14,MUTED)
    else:b+=text(pad,foot,visible[0]['date']+' → '+visible[-1]['date'],18,MUTED)
    b+=text(pad,foot+52,('Обновено: ' if bg else 'Updated: ')+data['updated'],14 if mobile else 18,MUTED)
    return svg(w,round(foot+76),'GitHub activity','Public contribution calendar. Streaks and totals use the shown annual window; mobile heatmap shows the last 26 weeks. Last contribution is not last login. No animated data.',b)


def languages(data,lang,mobile):
    bg=lang=='bg';w=390 if mobile else 1000;pad=24 if mobile else 40
    items=sorted(data['languages'],key=lambda row:row['bytes'],reverse=True)
    total=sum(x['bytes'] for x in items)
    if total<=0:raise ValueError('Empty language snapshot')
    rows=items[:6];other=sum(x['bytes'] for x in items[6:])
    if other:rows=rows+[dict(name='Други' if bg else 'Other',bytes=other)]
    b=text(pad,36 if mobile else 40,'ЕЗИЦИ / ОБЕМ КОД' if bg else 'LANGUAGES / CODE VOLUME',14 if mobile else 18,MUTED,600)
    b+=text(pad,66 if mobile else 76,('Снимка: ' if bg else 'Snapshot: ')+data['snapshot_date'],16 if mobile else 21)
    colors=[VIOLET,BLUE,MINT,'#C5C0ED','#A0B5DB','#7CB8C5','#8997B0']
    for i,(row,color) in enumerate(zip(rows,colors)):
        y=109+i*(49 if mobile else 44);pct=100*row['bytes']/total
        b+=text(pad,y,row['name'],18 if mobile else 22)+text(w-pad,y,f'{pct:.1f}%',18 if mobile else 22,color,anchor='end')
        b+=f'<rect x="{pad}" y="{y+10}" width="{w-pad*2}" height="5" rx="2" fill="#29364D"/><rect x="{pad}" y="{y+10}" width="{(w-pad*2)*pct/100:.3f}" height="5" rx="2" fill="{color}"/>'
    foot=109+len(rows)*(49 if mobile else 44)+7
    b+=text(pad,foot,'Обем код, не време или умения.' if bg else 'Code volume, not time or proficiency.',14 if mobile else 19,MUTED)
    return svg(w,foot+25,'Languages by code volume','Fixed aggregate language-byte snapshot. Includes private projects without their names or code; excludes the profile repository. Does not measure hours or skill.',b)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--metrics-only',action='store_true');args=ap.parse_args()
    data=json.loads((ROOT/'data/activity.json').read_text())
    language=json.loads((ROOT/'data/languages.json').read_text())
    files={}
    if not args.metrics_only:
        for name in ['bid','police','education']:
            for mobile in [False,True]:
                files[f'screens/{name}{"-mobile" if mobile else ""}.svg']=screen(name,mobile)
    for lang in ['bg','en']:
        for mobile in [False,True]:
            suffix=f'{lang}{"-mobile" if mobile else ""}.svg'
            files['metrics/activity-'+suffix]=activity(data,lang,mobile)
            files['metrics/languages-'+suffix]=languages(language,lang,mobile)
            if not args.metrics_only:
                files['native-'+suffix]=architecture(lang,mobile,'native')
                files['sync-'+suffix]=architecture(lang,mobile,'sync')
                files['toolkit-'+suffix]=toolkit(lang,mobile)
                files['process-'+suffix]=process(lang,mobile)
    for name,content in files.items():
        p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content+'\n')
    print(f'Rendered {len(files)} local SVGs.')


if __name__=='__main__':main()
