#!/usr/bin/env python3
"""Generate the animated studio visuals used by README.md and README.bg.md.

Run: python3 scripts/build_visuals.py
Writes assets/motion/*.svg. Inputs: data/technologies.json (all 68 technologies
plus the verified product stacks) and data/tech-icons.json (Simple Icons, CC0).
Decorative motion never represents live activity; architecture visuals are
labelled as illustrations. Activity/language panels are produced separately by
scripts/update_metrics.py.
"""
import json
import math
from functools import lru_cache
import random
from pathlib import Path

from profile_style import ACCENTS, C, document, esc, linear, radial, text, wrap
from typeset import fit, outline

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/motion'
TECH = json.loads((ROOT / 'data/technologies.json').read_text())
ICONS = json.loads((ROOT / 'data/tech-icons.json').read_text())['icons']

PRODUCT_COLORS = {'bid': C['violet'], 'police': C['cyan'], 'client': C['amber'], 'community': C['mint'], 'tlr': C['pink']}

T = {
    'en': {
        'hero_title': 'Yavor Yakow — independent developer',
        'hero_desc': 'Studio introduction: products with systems behind them. Websites, online stores, web and desktop software, admin panels, Discord bots, games and FiveM, APIs, automation and AI. Featured work: Before I Deploy, TLR Police Portal and The Last Republic. Contact: Fraisbg1@gmail.com, Discord Fraisbg, Instagram @y.yakowvw.sales. Orbits and light are decorative.',
        'kicker': 'YAVOR YAKOW  ·  INDEPENDENT DEVELOPER', 'kicker_m': 'YAVOR YAKOW · DEVELOPER',
        'head': ['Products with', 'systems behind them.'],
        'spec': ['Websites · online stores · web & desktop software', 'Admin panels · Discord bots · games & FiveM · APIs · AI'],
        'spec_m': ['Websites · online stores · software', 'Admin panels · Discord bots · games', 'FiveM · APIs · automation & AI'],
        'chips': ['Before I Deploy', 'TLR Police Portal', 'The Last Republic'],
        'decor': 'decorative motion',
        'divider': 'Chapter',
        'illus': 'Architecture illustration · not a live dashboard',
    },
    'bg': {
        'hero_title': 'Явор — независим разработчик',
        'hero_desc': 'Представяне: продукти със системи зад тях. Сайтове, онлайн магазини, уеб и настолен софтуер, админ панели, Discord ботове, игри и FiveM, API, автоматизации и AI. Избрана работа: Before I Deploy, TLR Police Portal и The Last Republic. Контакт: Fraisbg1@gmail.com, Discord Fraisbg, Instagram @y.yakowvw.sales. Орбитите и светлината са декоративни.',
        'kicker': 'ЯВОР  ·  YAVOR YAKOW  ·  НЕЗАВИСИМ РАЗРАБОТЧИК', 'kicker_m': 'ЯВОР · НЕЗАВИСИМ РАЗРАБОТЧИК',
        'head': ['Продукти със', 'системи зад тях.'],
        'spec': ['Сайтове · онлайн магазини · уеб и настолен софтуер', 'Админ панели · Discord ботове · игри и FiveM · API · AI'],
        'spec_m': ['Сайтове · онлайн магазини · софтуер', 'Админ панели · Discord ботове · игри', 'FiveM · API · автоматизации и AI'],
        'chips': ['Before I Deploy', 'TLR Police Portal', 'The Last Republic'],
        'decor': 'декоративно движение',
        'divider': 'Глава',
        'illus': 'Илюстрация на архитектурата · не е табло на живо',
    },
}
CONTACT = [('mail', 'Fraisbg1@gmail.com'), ('discord', 'Fraisbg'), ('instagram', '@y.yakowvw.sales')]


# ---------------------------------------------------------------- helpers
def icon(slug, x, y, size, fill):
    path = ICONS[slug]['path']
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({size / 24:.4f})"><path d="{path}" fill="{fill}"/></g>'


def glyph(kind, x, y, size, color):
    """Small drawn contact glyphs (no emoji fonts, no remote assets)."""
    s = size / 24
    if kind == 'discord':
        return icon('discord', x, y, size, color)
    if kind == 'instagram':
        return icon('instagram', x, y, size, color)
    if kind == 'mail':
        return (f'<g transform="translate({x} {y}) scale({s:.3f})" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round">'
                '<rect x="2" y="5" width="20" height="14" rx="3"/><path d="M3 6.5l9 6.5 9-6.5"/></g>')
    if kind == 'phone':
        return (f'<g transform="translate({x} {y}) scale({s:.3f})" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round">'
                '<path d="M6.6 3.5h3l1.5 4.2-2 1.5a12 12 0 005.7 5.7l1.5-2 4.2 1.5v3a2 2 0 01-2.2 2A17.6 17.6 0 014.6 5.7a2 2 0 012-2.2z"/></g>')
    raise ValueError(kind)


def ellipse_path(cx, cy, rx, ry):
    return f'M{cx - rx:.1f} {cy:.1f}a{rx} {ry} 0 1 0 {2 * rx} 0a{rx} {ry} 0 1 0 {-2 * rx} 0'


def on_ellipse(cx, cy, rx, ry, tilt, angle):
    a, t = math.radians(angle), math.radians(tilt)
    x, y = rx * math.cos(a), ry * math.sin(a)
    return cx + x * math.cos(t) - y * math.sin(t), cy + x * math.sin(t) + y * math.cos(t)


def frame(width, height, radius=28, fill='url(#bg)'):
    return (f'<clipPath id="frame"><rect width="{width}" height="{height}" rx="{radius}"/></clipPath>'
            f'<rect width="{width}" height="{height}" rx="{radius}" fill="{fill}"/>')


def stars(width, height, count, seed, top=0):
    rng = random.Random(seed)
    dots = ''
    for _ in range(count):
        dots += f'<circle cx="{rng.uniform(0, width):.0f}" cy="{rng.uniform(top, height):.0f}" r="{rng.choice([0.8, 1, 1.2, 1.6])}" fill="#fff" opacity="{rng.uniform(.15, .55):.2f}"/>'
    return dots


def pill_width(label, size):
    return len(label) * size * 0.56 + 52


def display(value, x, y, size, fill, anchor='start', weight=700, extra=''):
    """Display headline in Unbounded, outlined so it renders identically everywhere."""
    return f'<path d="{outline(value, x, y, size, weight, anchor)}" fill="{fill}" {extra}/>'


def write(name, content):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(content)


# ---------------------------------------------------------------- hero
def hero(lang, mobile):
    t = T[lang]
    w, h = (600, 1010) if mobile else (1200, 640)
    cx, cy = (300, 640) if mobile else (918, 300)
    k = 0.72 if mobile else 1.0
    tilt = -16
    defs = (linear('bg', [(0, C['night']), (.55, '#170F45'), (1, C['deep'])], x2=1, y2=1)
            + radial('rv', C['violet'], .55) + radial('rp', C['magenta'], .42) + radial('rc', C['cyan'], .32)
            + radial('ra', C['amber2'], .30)
            + linear('hg', [(0, C['lilac2']), (.5, C['pink']), (1, C['amber'])])
            + linear('acc', [(0, C['violet']), (.5, C['cyan']), (1, C['mint'])])
            + linear('o1', [(0, C['lilac'], .9), (1, C['cyan'], .15)])
            + linear('o2', [(0, C['pink'], .85), (1, C['amber'], .2)])
            + linear('o3', [(0, C['cyan'], .9), (1, C['mint'], .2)])
            + '<radialGradient id="core"><stop offset="0" stop-color="#FFF7FD"/><stop offset=".3" stop-color="#F9A8D4"/>'
              '<stop offset=".62" stop-color="#8B5CF6" stop-opacity=".9"/><stop offset="1" stop-color="#4C1D95" stop-opacity="0"/></radialGradient>'
            + linear('fy', [(0, '#000'), (.35, '#fff', .6), (1, '#fff')], x2=0, y2=1)
            + linear('fx', [(0, '#000'), (.5, '#fff'), (1, '#fff')])
            + linear('beam', [(0, '#fff', 0), (.5, '#fff', .13), (1, '#fff', 0)])
            + '<mask id="fadeY"><rect width="100%" height="100%" fill="url(#fy)"/></mask>'
            + '<mask id="fadeX"><rect width="100%" height="100%" fill="url(#fx)"/></mask>')
    motion = ('.b1{animation:drift1 30s ease-in-out infinite}.b2{animation:drift2 38s ease-in-out infinite}'
              '.b3{animation:drift3 44s ease-in-out infinite}.b4{animation:drift2 26s ease-in-out infinite reverse}'
              '.fl{animation:floor 8s cubic-bezier(.55,0,.9,.4) infinite}'
              '.halo{transform-box:fill-box;transform-origin:center;animation:breathe 9s ease-in-out infinite}'
              '.ring{transform-box:fill-box;transform-origin:center;animation:spin 60s linear infinite}'
              '.ring2{transform-box:fill-box;transform-origin:center;animation:spin 90s linear infinite reverse}'
              '.beam{animation:beam 16s ease-in-out infinite}.spark{animation:spark 11s cubic-bezier(.6,0,.3,1) infinite}'
              '@keyframes drift1{50%{transform:translate(-60px,40px)}}@keyframes drift2{50%{transform:translate(50px,-30px)}}'
              '@keyframes drift3{50%{transform:translate(70px,-50px)}}'
              f'@keyframes floor{{0%{{transform:translateY(0);opacity:0}}12%{{opacity:.9}}100%{{transform:translateY({(h - (cy + 140 * k)):.0f}px);opacity:.9}}}}'
              '@keyframes breathe{50%{transform:scale(1.12);opacity:.75}}@keyframes spin{to{transform:rotate(360deg)}}'
              f'@keyframes beam{{0%,20%{{transform:translateX(-500px)}}70%,100%{{transform:translateX({w + 300}px)}}}}'
              f'@keyframes spark{{0%{{transform:translateX(0);opacity:0}}8%{{opacity:1}}85%{{opacity:1}}100%{{transform:translateX({w - 2 * (32 if mobile else 72) - 140}px);opacity:0}}}}')
    b = frame(w, h) + '<g clip-path="url(#frame)">'
    b += (f'<g class="b1"><circle cx="{w * .8:.0f}" cy="{h * .2:.0f}" r="{380 * k:.0f}" fill="url(#rv)"/></g>'
          f'<g class="b2"><circle cx="{w * .92:.0f}" cy="{h * .85:.0f}" r="{320 * k:.0f}" fill="url(#rp)"/></g>'
          f'<g class="b3"><circle cx="{w * .2:.0f}" cy="{h * .98:.0f}" r="{340 * k:.0f}" fill="url(#rc)"/></g>'
          f'<g class="b4"><circle cx="{w * .52:.0f}" cy="{h * .05:.0f}" r="{220 * k:.0f}" fill="url(#ra)"/></g>')
    b += stars(w, h, 70 if not mobile else 45, 7)
    # perspective floor below the orbit system
    horizon = cy + 140 * k
    floor = ''
    for i in range(-14, 15):
        floor += f'<path d="M{cx + i * 16 * k:.0f} {horizon:.0f}L{cx + i * 120 * k:.0f} {h}" stroke="{C["lilac"]}" stroke-opacity=".28"/>'
    for i in range(1, 6):
        yy = horizon + (h - horizon) * (i / 6) ** 2
        floor += f'<path d="M0 {yy:.0f}H{w}" stroke="{C["cyan"]}" stroke-opacity=".18"/>'
    floor += '<g class="live">' + ''.join(
        f'<path class="fl" style="animation-delay:-{i * 1.6:.1f}s" d="M0 {horizon:.0f}H{w}" stroke="{C["mint2"]}" stroke-opacity=".55"/>'
        for i in range(5)) + '</g>'
    fade_x = '' if mobile else ' mask="url(#fadeX)"'
    b += f'<g mask="url(#fadeY)"><g{fade_x}>{floor}</g></g>'
    b += f'<g class="live"><rect class="beam" x="0" y="-200" width="160" height="{h + 400}" fill="url(#beam)" transform="rotate(18 {w / 2} {h / 2})"/></g>'
    # orbit system: each moving body is a product colour; the legend chips name them
    orbits = [(255, 90, 'o1', 24, PRODUCT_COLORS['bid'], 30), (190, 66, 'o2', 17, PRODUCT_COLORS['tlr'], 200),
              (126, 44, 'o3', 12, PRODUCT_COLORS['police'], 110)]
    b += f'<circle class="halo" cx="{cx}" cy="{cy}" r="{150 * k:.0f}" fill="url(#rp)"/>'
    g = f'<g transform="rotate({tilt} {cx} {cy})">'
    for rx, ry, grad, dur, color, start in orbits:
        rx, ry = rx * k, ry * k
        g += f'<path d="{ellipse_path(cx, cy, rx, ry)}" fill="none" stroke="url(#{grad})" stroke-width="1.6"/>'
    g += '</g>'
    b += g
    b += (f'<circle class="ring2" cx="{cx}" cy="{cy}" r="{80 * k:.0f}" fill="none" stroke="{C["lilac2"]}" stroke-opacity=".35" stroke-dasharray="2 9"/>'
          f'<circle class="ring" cx="{cx}" cy="{cy}" r="{62 * k:.0f}" fill="none" stroke="{C["pink"]}" stroke-opacity=".55" stroke-width="1.5" stroke-dasharray="60 30 8 30"/>'
          f'<circle cx="{cx}" cy="{cy}" r="{44 * k:.0f}" fill="url(#core)"/>')
    bodies_live, bodies_still = '', ''
    extra = [(255, 90, 34, PRODUCT_COLORS['community'], 210)]
    for rx, ry, _grad, dur, color, start in orbits + [(a, b2, None, d, c, s) for a, b2, d, c, s in extra]:
        rx, ry = rx * k, ry * k
        dot = (f'<circle r="{15 * k:.0f}" fill="{color}" opacity=".22"/><circle r="{6.5 * k:.1f}" fill="{color}"/>'
               f'<circle r="{2.4 * k:.1f}" fill="#fff"/>')
        bodies_live += (f'<g transform="rotate({tilt} {cx} {cy})"><g>{dot}<animateMotion dur="{dur}s" repeatCount="indefinite" '
                        f'begin="-{dur * start / 360:.2f}s" path="{ellipse_path(cx, cy, rx, ry)}"/></g></g>')
        px, py = on_ellipse(cx, cy, rx, ry, tilt, 180 + start)
        bodies_still += f'<g transform="translate({px:.1f} {py:.1f})">{dot}</g>'
    b += f'<g class="live">{bodies_live}</g><g class="still">{bodies_still}</g>'
    # typography
    x0 = 32 if mobile else 72
    if mobile:
        y = 78
        b += f'<rect x="{x0}" y="{y - 13}" width="26" height="4" rx="2" fill="url(#acc)"/>'
        b += text(x0 + 38, y - 4, t['kicker_m'], 18, C['lilac2'], 700, spacing=2)
        hs = min(fit(t['head'][0], 46, w - 2 * x0), fit(t['head'][1], 46, w - 2 * x0))
        b += display(t['head'][0], x0, 150, hs, C['text'])
        b += display(t['head'][1], x0, 150 + hs * 1.25, hs, 'url(#hg)')
        for i, line in enumerate(t['spec_m']):
            b += text(x0, 266 + i * 32, line, 21, C['soft'])
        chip_y = [372, 426, 426]
        chip_x = [x0, x0, None]
    else:
        b += f'<rect x="{x0}" y="{103}" width="34" height="4" rx="2" fill="url(#acc)"/>'
        b += text(x0 + 48, 110, t['kicker'], 16, C['lilac2'], 700, spacing=3.4)
        hs = min(fit(t['head'][0], 54, 640), fit(t['head'][1], 54, 640))
        b += display(t['head'][0], x0, 190, hs, C['text'])
        b += display(t['head'][1], x0, 190 + hs * 1.3, hs, 'url(#hg)')
        for i, line in enumerate(t['spec']):
            b += text(x0, 322 + i * 33, line, 21, C['soft'])
        chip_y = [408, 408, 408]
        chip_x = [x0, None, None]
    colors = [PRODUCT_COLORS['bid'], PRODUCT_COLORS['police'], PRODUCT_COLORS['tlr']]
    cursor = x0
    chip_size = 20 if mobile else 17
    for i, label in enumerate(t['chips']):
        pw = pill_width(label, chip_size)
        x = chip_x[i] if chip_x[i] is not None else cursor
        y = chip_y[i]
        ch = 42 if mobile else 38
        b += (f'<rect x="{x}" y="{y}" width="{pw:.0f}" height="{ch}" rx="{ch / 2:.0f}" fill="#ffffff" fill-opacity=".06" stroke="{colors[i]}" stroke-opacity=".7"/>'
              f'<circle cx="{x + 21}" cy="{y + ch / 2}" r="6" fill="{colors[i]}"/>')
        b += text(x + 36, y + ch / 2 + 6.5, label, chip_size, C['text'], 700)
        cursor = x + pw + 12
    # contact: always visible, never animated
    if mobile:
        for i, (kind, value) in enumerate(CONTACT):
            y = 800 + i * 58
            b += f'<rect x="{x0}" y="{y}" width="{w - 2 * x0}" height="46" rx="23" fill="#0B0824" fill-opacity=".72" stroke="#ffffff" stroke-opacity=".16"/>'
            b += glyph(kind, x0 + 18, y + 11, 24, [C['pink'], '#8C9EFF', '#FF4F93'][i])
            b += text(x0 + 56, y + 31, value, 22, C['text'], 600)
    else:
        y = 476
        b += f'<rect x="{x0}" y="{y}" width="676" height="58" rx="29" fill="#0B0824" fill-opacity=".72" stroke="#ffffff" stroke-opacity=".16"/>'
        x = x0 + 24
        for i, (kind, value) in enumerate(CONTACT):
            b += glyph(kind, x, y + 17, 24, [C['pink'], '#8C9EFF', '#FF4F93'][i])
            b += text(x + 34, y + 36, value, 19, C['text'], 600)
            x += 34 + len(value) * 10.4 + 34
            if i < 2:
                b += f'<path d="M{x - 18} {y + 18}v22" stroke="#fff" stroke-opacity=".18"/>'
    base = h - 34
    b += f'<rect x="{x0}" y="{base}" width="{w - 2 * x0}" height="3" rx="1.5" fill="url(#acc)" opacity=".85"/>'
    b += f'<g class="live"><rect class="spark" x="{x0}" y="{base - 2}" width="140" height="7" rx="3.5" fill="#E0FBFF"/></g>'
    b += '</g>'
    return document(w, h, t['hero_title'], t['hero_desc'], b, defs, motion)


# ---------------------------------------------------------------- chapter dividers
DIVIDERS = [('waves', 'violet'), ('beads', 'pink'), ('circuit', 'cyan'), ('constellation', 'mint'), ('sunrise', 'amber')]


def divider(index, lang, mobile):
    motif, accent = DIVIDERS[index]
    a1, a2 = ACCENTS[accent]
    w, h = (600, 92) if mobile else (1200, 104)
    mid = h / 2
    r = 26 if mobile else 30
    bx = r + 6
    defs = (linear('g', [(0, a1), (1, a2)]) + linear('ge', [(0, a1, 0), (.12, a1, .9), (.88, a2, .9), (1, a2, 0)])
            + radial('glow', a1, .55) + linear('band', [(0, C['ink']), (.5, C['indigo']), (1, C['ink'])]))
    motion = ('.ringd{transform-box:fill-box;transform-origin:center;animation:spin 24s linear infinite}'
              '@keyframes spin{to{transform:rotate(360deg)}}')
    x0, x1 = bx + r + 24, w - 8
    span = x1 - x0
    m = ''
    if motif == 'waves':
        period = 150 if mobile else 240
        for j, (amp, op, sw) in enumerate([(14, .9, 2.2), (9, .55, 1.4), (20, .3, 1)]):
            d = f'M{x0 - period * 2} {mid}'
            for i in range(int((span + period * 4) / (period / 2)) + 2):
                xx = x0 - period * 2 + (i + 1) * period / 2
                cy_ = mid + (amp if (i + j) % 2 == 0 else -amp) * (1 if mobile is False else .7)
                d += f'Q{xx - period / 4:.0f} {cy_:.0f} {xx:.0f} {mid}'
            m += f'<path class="wv" style="animation-duration:{10 + j * 4}s" d="{d}" fill="none" stroke="url(#g)" stroke-width="{sw}" opacity="{op}"/>'
        motion += f'.wv{{animation:wave 12s linear infinite}}@keyframes wave{{to{{transform:translateX({period}px)}}}}'
    elif motif == 'beads':
        n = 26 if mobile else 46
        for i in range(n):
            xx = x0 + span * i / (n - 1)
            yy = mid + math.sin(i / 2.6) * (h * .16)
            m += (f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="{3.2 if i % 3 else 4.6}" fill="url(#g)" opacity=".75"/>'
                  f'<circle class="bd" style="animation-delay:{i * .11:.2f}s" cx="{xx:.1f}" cy="{yy:.1f}" r="9" fill="{a2}" opacity="0"/>')
        motion += f'.bd{{animation:bead {n * .11 + 2:.1f}s ease-in-out infinite}}@keyframes bead{{0%,12%,100%{{opacity:0}}5%{{opacity:.55}}}}'
    elif motif == 'circuit':
        rng = random.Random(index * 11 + (1 if mobile else 0))
        lanes = [mid - h * .22, mid, mid + h * .22]
        for j, ly in enumerate(lanes):
            d = f'M{x0} {ly:.0f}'
            xx = x0
            while xx < x1 - 60:
                step = rng.randint(60, 140)
                xx = min(xx + step, x1)
                d += f'H{xx}'
                if rng.random() < .45 and xx < x1 - 40:
                    other = lanes[(j + rng.choice([1, 2])) % 3]
                    d += f'L{xx + 14} {other:.0f}L{xx + 28} {ly:.0f}'
                    xx += 28
                    m += f'<circle cx="{xx - 14}" cy="{other:.0f}" r="2.6" fill="{a2}"/>'
            m += f'<path d="{d}H{x1}" fill="none" stroke="url(#ge)" stroke-width="1.4" opacity=".55"/>'
            m += f'<path class="live ct" style="animation-delay:-{j * 2.2}s" d="{d}H{x1}" fill="none" stroke="#E0FFFB" stroke-width="2.2" pathLength="100" stroke-dasharray="4 96" stroke-linecap="round"/>'
        motion += '.ct{animation:trace 7s linear infinite}@keyframes trace{from{stroke-dashoffset:100}to{stroke-dashoffset:0}}'
    elif motif == 'constellation':
        rng = random.Random(4 + (1 if mobile else 0))
        pts = [(x0 + span * (i + rng.uniform(.1, .9)) / (14 if not mobile else 8), rng.uniform(h * .2, h * .8))
               for i in range(14 if not mobile else 8)]
        for (ax, ay), (bx_, by) in zip(pts, pts[1:]):
            m += f'<path d="M{ax:.0f} {ay:.0f}L{bx_:.0f} {by:.0f}" stroke="url(#ge)" stroke-opacity=".6"/>'
        for i, (px, py) in enumerate(pts):
            m += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{2.5 + (i % 3)}" fill="{a1 if i % 2 else a2}"/>'
            m += f'<circle class="st" style="animation-delay:{i * .7:.1f}s" cx="{px:.0f}" cy="{py:.0f}" r="10" fill="url(#glow)" opacity=".15"/>'
        motion += f'.st{{animation:star {len(pts) * .7:.1f}s ease-in-out infinite}}@keyframes star{{0%,100%{{opacity:.15}}8%{{opacity:1}}20%{{opacity:.15}}}}'
    elif motif == 'sunrise':
        cxs = x0 + span / 2
        for i in range(6):
            rr = 24 + i * (h * .3 if not mobile else h * .28)
            m += (f'<path class="{"sr" if i % 2 else "sr2"}" d="M{cxs - rr:.0f} {h}A{rr:.0f} {rr:.0f} 0 0 1 {cxs + rr:.0f} {h}" fill="none" '
                  f'stroke="url(#g)" stroke-width="1.6" opacity="{.85 - i * .12:.2f}" stroke-dasharray="{14 + i * 6} {10 + i * 4}"/>')
        m += f'<path d="M{x0} {h - 1}H{x1}" stroke="url(#ge)" stroke-width="2"/>'
        motion += ('.sr{animation:dash 14s linear infinite}.sr2{animation:dash 20s linear infinite reverse}'
                   '@keyframes dash{to{stroke-dashoffset:-240}}')
    clip = f'<clipPath id="motif"><rect x="{x0}" y="0" width="{span}" height="{h}"/></clipPath>'
    num = f'{index + 1:02d}'
    b = f'<rect width="{w}" height="{h}" rx="{h / 2:.0f}" fill="url(#band)"/>' + clip + f'<g clip-path="url(#motif)">{m}</g>'
    b += (f'<circle cx="{bx}" cy="{mid}" r="{r + 10}" fill="url(#glow)" opacity=".6"/>'
          f'<circle cx="{bx}" cy="{mid}" r="{r}" fill="{C["ink"]}" stroke="url(#g)" stroke-width="2"/>'
          f'<circle class="ringd" cx="{bx}" cy="{mid}" r="{r + 6}" fill="none" stroke="{a2}" stroke-opacity=".7" stroke-dasharray="3 7"/>')
    b += text(bx, mid + (8 if mobile else 9), num, 22 if mobile else 24, C['text'], 800, anchor='middle')
    label = f"{T[lang]['divider']} {num}"
    return document(w, h, label, f'{label}. Decorative section transition.' if lang == 'en' else f'{label}. Декоративен преход между секциите.', b, defs, motion)


# ---------------------------------------------------------------- project accents
PROJECTS = {
    'bid': {'n': '01', 'name': 'Before I Deploy', 'accent': ('#8B5CF6', '#22D3EE'), 'motif': 'scan',
            'en': ('NATIVE macOS APP', 'SwiftUI interface · Node.js check engine · hosting & cloud links'),
            'bg': ('НАТИВНО macOS ПРИЛОЖЕНИЕ', 'SwiftUI интерфейс · Node.js модул за проверки · хостинг и облак')},
    'police': {'n': '02', 'name': 'TLR Police Portal', 'accent': ('#22D3EE', '#34D399'), 'motif': 'tree',
               'en': ('FIVEM COMMUNITY OPERATIONS', 'Staff roster · ranks · handbook · Discord-synchronised roles'),
               'bg': ('ОПЕРАЦИИ ЗА FIVEM ОБЩНОСТ', 'Състав · звания · наръчник · роли, синхронизирани с Discord')},
    'tlr': {'n': '03', 'name': 'The Last Republic', 'accent': ('#F472B6', '#8B5CF6'), 'motif': 'network',
            'en': ('COMMUNITY INFRASTRUCTURE', 'Public interface · rules · Discord-connected applications'),
            'bg': ('ОБЩНОСТНА ИНФРАСТРУКТУРА', 'Публичен интерфейс · правила · кандидатстване чрез Discord')},
    'studio': {'n': '04', 'name': 'readme-studio', 'accent': ('#34D399', '#22D3EE'), 'motif': 'page',
               'en': ('OPEN SOURCE · MIT', 'Animated, bilingual GitHub profiles from one JSON file'),
               'bg': ('ОТВОРЕН КОД · MIT', 'Анимирани двуезични GitHub профили от един JSON файл')},
}


def project_motif(kind, x, y, w, h, a1, a2):
    m, css = '', ''
    if kind == 'scan':
        rng = random.Random(3)
        rows = 6
        for i in range(rows):
            yy = y + 10 + i * (h - 20) / (rows - 1)
            ln = rng.uniform(.35, .8) * (w - 60)
            m += f'<rect x="{x}" y="{yy - 4:.0f}" width="{ln:.0f}" height="8" rx="4" fill="{a1}" opacity=".28"/>'
            m += f'<rect x="{x}" y="{yy - 4:.0f}" width="{ln * .35:.0f}" height="8" rx="4" fill="{a1}" opacity=".55"/>'
            color = C['amber'] if i == 3 else C['mint']
            m += f'<circle cx="{x + w - 22}" cy="{yy:.0f}" r="6" fill="{color}" opacity=".35"/>'
            m += f'<circle class="ok" style="animation-delay:{.6 + i * .55:.2f}s" cx="{x + w - 22}" cy="{yy:.0f}" r="6" fill="{color}" opacity=".35"/>'
        m += f'<rect class="scanb" x="{x - 10}" y="{y}" width="4" height="{h}" rx="2" fill="{a2}" opacity=".9"/>'
        css = (f'.scanb{{animation:scan 6s cubic-bezier(.5,0,.5,1) infinite}}@keyframes scan{{0%{{transform:translateX(0);opacity:0}}8%{{opacity:.9}}60%{{transform:translateX({w - 30}px);opacity:.9}}70%,100%{{transform:translateX({w - 30}px);opacity:0}}}}'
               '.ok{animation:ok 6s ease-out infinite}@keyframes ok{0%,100%{opacity:.35}8%,60%{opacity:1}}')
    elif kind == 'tree':
        levels = [[.5], [.2, .5, .8], [.08, .26, .42, .58, .74, .92]]
        pts = []
        for li, level in enumerate(levels):
            yy = y + 12 + li * (h - 24) / 2
            pts.append([(x + w * f, yy) for f in level])
        for li in range(2):
            for i, (px, py) in enumerate(pts[li + 1]):
                parent = pts[li][min(len(pts[li]) - 1, i * len(pts[li]) // len(pts[li + 1]))]
                m += f'<path d="M{parent[0]:.0f} {parent[1]:.0f}C{parent[0]:.0f} {(parent[1] + py) / 2:.0f} {px:.0f} {(parent[1] + py) / 2:.0f} {px:.0f} {py:.0f}" fill="none" stroke="{a1}" stroke-opacity=".4"/>'
        k = 0
        for li, level in enumerate(pts):
            for px, py in level:
                m += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{9 - li * 2}" fill="{C["ink"]}" stroke="{a1 if li < 2 else a2}" stroke-width="2"/>'
                m += f'<circle class="nd" style="animation-delay:{li * .9 + k * .08:.2f}s" cx="{px:.0f}" cy="{py:.0f}" r="{9 - li * 2}" fill="{a2}" opacity="0"/>'
                k += 1
        css = '.nd{animation:node 7s ease-in-out infinite}@keyframes node{0%,100%{opacity:0}6%,22%{opacity:.85}36%{opacity:0}}'
    elif kind == 'network':
        hub = (x + w / 2, y + h / 2)
        sats = [(x + w / 2 + math.cos(a) * w * .38, y + h / 2 + math.sin(a) * h * .42) for a in [i * math.pi / 3 + .3 for i in range(6)]]
        for i, (px, py) in enumerate(sats):
            m += f'<path d="M{hub[0]:.0f} {hub[1]:.0f}L{px:.0f} {py:.0f}" stroke="{a1}" stroke-opacity=".35"/>'
            m += f'<path class="lk" style="animation-delay:-{i * .8:.1f}s" d="M{hub[0]:.0f} {hub[1]:.0f}L{px:.0f} {py:.0f}" stroke="{a2}" stroke-width="2" pathLength="100" stroke-dasharray="10 90"/>'
            m += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="7" fill="{C["ink"]}" stroke="{a2}" stroke-width="2"/>'
        m += f'<circle cx="{hub[0]:.0f}" cy="{hub[1]:.0f}" r="16" fill="{a1}" opacity=".3"/><circle cx="{hub[0]:.0f}" cy="{hub[1]:.0f}" r="9" fill="{a1}"/>'
        css = '.lk{animation:link 4.8s linear infinite}@keyframes link{from{stroke-dashoffset:100}to{stroke-dashoffset:-10}}'
    elif kind == 'hex':
        size = 15
        cols, rows = int(w / (size * 1.8)), 4
        k = 0
        for r_ in range(rows):
            for c_ in range(cols):
                cx_ = x + 14 + c_ * size * 1.75 + (size * .87 if r_ % 2 else 0)
                cy_ = y + 16 + r_ * size * 1.5
                if cx_ > x + w - 10:
                    continue
                pts = ' '.join(f'{cx_ + size * math.cos(math.radians(60 * i + 30)):.1f},{cy_ + size * math.sin(math.radians(60 * i + 30)):.1f}' for i in range(6))
                m += f'<polygon points="{pts}" fill="none" stroke="{a1}" stroke-opacity=".35"/>'
                m += f'<polygon class="hx" style="animation-delay:{(c_ + r_) * .16:.2f}s" points="{pts}" fill="{a2}" opacity="0"/>'
                k += 1
        css = '.hx{animation:hex 6s ease-in-out infinite}@keyframes hex{0%,100%{opacity:0}10%{opacity:.5}24%{opacity:0}}'
    elif kind == 'page':
        blocks = [(0, 0, 1, .14, a1), (0, .22, .58, .3, a2), (.64, .22, .36, .3, a1), (0, .6, .31, .4, a2), (.345, .6, .31, .4, a1), (.69, .6, .31, .4, a2)]
        m += f'<rect x="{x - 6}" y="{y - 6}" width="{w + 12}" height="{h + 12}" rx="12" fill="none" stroke="{a1}" stroke-opacity=".35" stroke-dasharray="4 6"/>'
        for i, (bx_, by_, bw, bh, col) in enumerate(blocks):
            m += f'<rect class="pg" style="animation-delay:{i * .45:.2f}s" x="{x + bx_ * w:.0f}" y="{y + by_ * h:.0f}" width="{bw * w:.0f}" height="{bh * h:.0f}" rx="7" fill="{col}" opacity=".45"/>'
        css = '.pg{animation:pg 9s ease-in-out infinite}@keyframes pg{0%{opacity:.08}8%,70%{opacity:.6}85%,100%{opacity:.08}}'
    return m, css


def project_marker(key, lang, mobile):
    p = PROJECTS[key]
    a1, a2 = p['accent']
    kicker, role = p[lang]
    w, h = (600, 330) if mobile else (1200, 210)
    defs = (linear('bg', [(0, C['ink']), (.6, C['indigo']), (1, C['deep'])], x2=1, y2=1) + linear('g', [(0, a1), (1, a2)])
            + linear('name', [(0, '#FFFFFF'), (.55, '#FFFFFF'), (1, a2)]) + radial('gl', a1, .5) + radial('gl2', a2, .4))
    motion = '.aur{animation:aur 22s ease-in-out infinite}@keyframes aur{50%{transform:translate(-40px,14px)}}'
    b = frame(w, h, 22) + '<g clip-path="url(#frame)">'
    b += (f'<g class="aur"><circle cx="{w * .82:.0f}" cy="{h * .3:.0f}" r="{h * 1.3:.0f}" fill="url(#gl)"/></g>'
          f'<circle cx="{w * .08:.0f}" cy="{h:.0f}" r="{h:.0f}" fill="url(#gl2)"/>')
    b += f'<rect x="0" y="0" width="{w}" height="3" fill="url(#g)"/>'
    if mobile:
        b += text(24, 92, p['n'], 80, 'none', 800, extra=f'stroke="url(#g)" stroke-width="2"')
        kl = wrap(kicker, 22)
        for i, line in enumerate(kl):
            b += text(140, 50 + i * 24, line, 19, a1, 800, spacing=2)
        ny = 76 + len(kl) * 24
        b += display(p['name'], 32, ny + 34, fit(p['name'], 40, w - 64), 'url(#name)')
        for i, line in enumerate(wrap(role, 40)):
            b += text(32, ny + 76 + i * 28, line, 21, C['soft'])
        mm, css = project_motif(p['motif'], 30, h - 82, w - 60, 58, a1, a2)
    else:
        b += text(40, 150, p['n'], 118, 'none', 800, extra=f'stroke="url(#g)" stroke-width="2"')
        b += text(40, 150, p['n'], 118, a1, 800, extra='opacity=".08"')
        b += text(232, 62, kicker, 15, a1, 800, spacing=3)
        b += display(p['name'], 232, 118, fit(p['name'], 44, 640), 'url(#name)')
        b += text(232, 160, role, 20, C['soft'])
        mm, css = project_motif(p['motif'], 900, 52, 260, 108, a1, a2)
    b += f'<g>{mm}</g></g>'
    title = f'{p["n"]} · {kicker}'
    desc = f'{title}. {role}. ' + ('Decorative project accent.' if lang == 'en' else 'Декоративен акцент на проекта.')
    return document(w, h, title, desc, b, defs, motion + css)


def wrap_segments(value, limit, sep=' · '):
    """Wrap a ' · '-separated list without starting a line with the separator."""
    lines, line = [], ''
    for part in value.split(sep):
        candidate = f'{line}{sep}{part}' if line else part
        if len(candidate) > limit and line:
            lines.append(line)
            line = part
        else:
            line = candidate
    return lines + [line] if line else lines


# ---------------------------------------------------------------- architecture
A = {
    'en': {'kicker': 'UNDER THE INTERFACE · ARCHITECTURE', 'app': ('SwiftUI app', 'macOS interface'),
           'engine': ('Node.js engine', 'commands · checks'), 'host': ('Hosting', 'preview · production'),
           'cmd': 'commands', 'evt': 'NDJSON events',
           'checks': ['Git', 'Secrets', 'Dependencies', 'Lint', 'Types', 'Build', 'Site', 'Hosting'],
           'gate': 'Confirm', 'gate_note': ['changed files →', 'explicit confirmation'],
           'local': ('LOCAL', 'Project files · Keychain'), 'cloud': ('OPTIONAL CLOUD', 'Supabase · Postgres · Deno Edge Functions'),
           'bid_title': 'Before I Deploy architecture',
           'bid_desc': 'Illustration. The SwiftUI app sends commands to a Node.js engine and receives NDJSON events back. The engine runs one chain of eight checks: Git, secrets, dependencies, lint, types, build, site quality and hosting readiness. If project files changed, production needs explicit confirmation before hosting. Project files and Keychain stay local; Supabase, Postgres and Deno Edge Functions are optional cloud services.',
           'tlr_kicker': 'CONNECTED SYSTEMS · ARCHITECTURE',
           'discord': ('Discord', 'Gateway · membership'), 'bot': ('Node.js bot', 'discord.js'),
           'pg': ('Postgres', 'Neon · Drizzle ORM'), 'portal': ('Next.js portal', 'staff operations'),
           'staff': ('Staff browser', 'Discord sign-in'), 'roles': 'Shared role map', 'roles_m': 'Shared role map · bot + portal',
           'l1': ['persistent Gateway'], 'l2': ['roster sync'], 'l3': ['authorized actions', 'server-side permissions'],
           'audit': 'roster · audit records',
           'tlr_title': 'TLR Police Portal architecture',
           'tlr_desc': 'Illustration. Discord membership events need a persistent connection, so a separate Node.js bot holds the Gateway connection and synchronises Discord-owned roster fields into Postgres (Neon, Drizzle ORM). The Next.js portal reads the roster and performs authorized management actions after server-side permission checks, writing audit records. Bot and portal share one role map. Staff sign in with Discord.'},
    'bg': {'kicker': 'ПОД ИНТЕРФЕЙСА · АРХИТЕКТУРА', 'app': ('SwiftUI приложение', 'macOS интерфейс'),
           'engine': ('Node.js модул', 'команди · проверки'), 'host': ('Хостинг', 'preview · production'),
           'cmd': 'команди', 'evt': 'NDJSON събития',
           'checks': ['Git', 'Тайни', 'Зависимости', 'Lint', 'Типове', 'Build', 'Сайт', 'Хостинг'],
           'gate': 'Потвърди', 'gate_note': ['променени файлове →', 'изрично потвърждение'],
           'local': ('ЛОКАЛНО', 'Файлове на проекта · Keychain'), 'cloud': ('ОБЛАК ПО ИЗБОР', 'Supabase · Postgres · Deno Edge Functions'),
           'bid_title': 'Архитектура на Before I Deploy',
           'bid_desc': 'Илюстрация. SwiftUI приложението изпраща команди към Node.js модул и получава обратно NDJSON събития. Модулът изпълнява една верига от осем проверки: Git, тайни, зависимости, lint, типове, build, качество на сайта и готовност на хостинга. Ако файловете на проекта са променени, продукционното публикуване изисква изрично потвърждение. Файловете и Keychain остават локално; Supabase, Postgres и Deno Edge Functions са облачни услуги по избор.',
           'tlr_kicker': 'СВЪРЗАНИ СИСТЕМИ · АРХИТЕКТУРА',
           'discord': ('Discord', 'Gateway · членство'), 'bot': ('Node.js бот', 'discord.js'),
           'pg': ('Postgres', 'Neon · Drizzle ORM'), 'portal': ('Next.js портал', 'действия на екипа'),
           'staff': ('Служители', 'вход с Discord'), 'roles': 'Обща карта на ролите', 'roles_m': 'Обща карта на ролите · бот + портал',
           'l1': ['постоянен Gateway'], 'l2': ['синхронизация'], 'l3': ['разрешени действия', 'права на сървъра'],
           'audit': 'състав · журнал на действията',
           'tlr_title': 'Архитектура на TLR Police Portal',
           'tlr_desc': 'Илюстрация. Събитията за членство в Discord изискват постоянна връзка, затова отделен Node.js бот поддържа Gateway връзката и синхронизира данните за състава в Postgres (Neon, Drizzle ORM). Next.js порталът чете състава и изпълнява разрешени действия след проверка на правата на сървъра, като записва журнал. Ботът и порталът използват обща карта на ролите. Служителите влизат с Discord.'},
}


def box(x, y, w, h, title, sub, color, logo=None, title_size=22, compact=False, sub_size=None):
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{C["glass"]}" fill-opacity=".92" stroke="{color}" stroke-opacity=".75" stroke-width="1.6"/>'
           f'<rect x="{x + 16}" y="{y + 18}" width="4" height="{h - 36}" rx="2" fill="{color}"/>')
    tx = x + 36
    if logo:
        lx = x + (48 if compact else 56)
        out += f'<circle cx="{lx}" cy="{y + h / 2}" r="{19 if compact else 22}" fill="{color}" fill-opacity=".18"/>' + icon(logo, lx - 11, y + h / 2 - 11, 22, color)
        tx = x + (78 if compact else 92)
    out += text(tx, y + h / 2 - 4, title, title_size, C['text'], 700)
    out += text(tx, y + h / 2 + 23, sub, sub_size or (14 if compact else 16), C['muted'])
    return out


def arch_frame(w, h, kicker, color):
    defs = (linear('bg', [(0, C['ink']), (.6, C['indigo']), (1, C['deep'])], x2=1, y2=1)
            + radial('ga', C['violet'], .35) + radial('gb', C['cyan'], .28)
            + '<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#8C85D9" stroke-opacity=".07"/></pattern>')
    b = frame(w, h, 24) + f'<rect width="{w}" height="{h}" rx="24" fill="url(#grid)"/>'
    b += f'<g clip-path="url(#frame)"><circle cx="{w * .85:.0f}" cy="{h * .1:.0f}" r="{w * .35:.0f}" fill="url(#ga)"/><circle cx="{w * .1:.0f}" cy="{h * .95:.0f}" r="{w * .3:.0f}" fill="url(#gb)"/></g>'
    b += f'<rect x="40" y="38" width="28" height="4" rx="2" fill="{color}"/>' + text(80, 46, kicker, 14, C['lilac2'], 700, spacing=3)
    return defs, b


def flow_dashes(d, color, dur, width=2, dash='8 10', reverse=False, extra=''):
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-opacity=".25" stroke-width="{width}"/>'
            f'<path class="live" d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}" stroke-linecap="round" '
            f'style="animation:flow {dur}s linear infinite{" reverse" if reverse else ""}" {extra}/>'
            f'<path class="still" d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}" stroke-linecap="round"/>')


def arch_bid(lang, mobile):
    t = A[lang]
    period = 10.0
    if mobile:
        w, h = 600, 1190
        defs, b = arch_frame(w, h, t['kicker'], C['violet'])
        b += box(40, 80, 520, 86, *t['app'], C['violet'], 'swift', title_size=26, sub_size=19)
        b += flow_dashes('M262 166V262', C['lilac'], 1.6) + flow_dashes('M338 262V166', C['pink'], 1.6, 5, '1 14')
        b += text(248, 220, t['cmd'], 18, C['lilac2'], anchor='end', mono=True) + text(352, 220, t['evt'], 18, C['pink'], mono=True)
        b += box(40, 262, 520, 86, *t['engine'], C['cyan'], 'nodedotjs', title_size=26, sub_size=19)
        path, xs = 'M300 348V390H110V930', [414 + i * 56 for i in range(8)]
        lens = [42 + 190 + (y - 390) for y in xs]
        total, gate_d = 42 + 190 + 540, 42 + 190 + 470
        b += f'<path d="M300 348V390H110V930" fill="none" stroke="url(#chain)" stroke-width="2.4" opacity=".55"/>'
        for i, (y, label) in enumerate(zip(xs, t['checks'])):
            delay = period * .8 * lens[i] / total
            b += (f'<circle cx="110" cy="{y}" r="9" fill="{C["ink"]}" stroke="{C["lilac"]}" stroke-width="2"/>'
                  f'<circle class="ring" style="animation-delay:{delay:.2f}s" cx="110" cy="{y}" r="15" fill="none" stroke="{C["mint2"]}" stroke-width="2.4"/>')
            b += text(142, y + 8, label, 23, C['soft'])
        b += (f'<rect class="gate" x="30" y="840" width="160" height="40" rx="20" fill="{C["ink"]}" stroke="{C["amber"]}" stroke-width="2" '
              f'style="animation-delay:{period * .8 * gate_d / total:.2f}s"/>') + text(110, 866, t['gate'], 17, C['amber'], 700, anchor='middle')
        b += text(204, 854, t['gate_note'][0], 18, C['amber']) + text(204, 878, t['gate_note'][1], 18, '#FDE68A')
        b += box(40, 930, 520, 86, *t['host'], C['mint'], title_size=26, sub_size=19)
        b += (f'<rect x="40" y="1040" width="250" height="104" rx="16" fill="none" stroke="{C["lilac"]}" stroke-opacity=".5" stroke-dasharray="5 6"/>'
              + text(60, 1070, t['local'][0], 15, C['lilac2'], 700, spacing=2) + ''.join(text(60, 1098 + i * 24, s, 18, C['soft']) for i, s in enumerate(wrap_segments(t['local'][1], 20))))
        b += (f'<rect x="310" y="1040" width="250" height="104" rx="16" fill="none" stroke="{C["cyan"]}" stroke-opacity=".5" stroke-dasharray="5 6"/>'
              + text(330, 1070, t['cloud'][0], 15, C['cyan'], 700, spacing=2) + ''.join(text(330, 1098 + i * 24, s, 18, C['soft']) for i, s in enumerate(wrap_segments(t['cloud'][1], 20))))
        b += text(w / 2, h - 20, T[lang]['illus'], 16, C['muted'], anchor='middle')
    else:
        w, h = 1200, 500
        defs, b = arch_frame(w, h, t['kicker'], C['violet'])
        b += box(48, 96, 270, 96, *t['app'], C['violet'], 'swift')
        b += box(465, 96, 270, 96, *t['engine'], C['cyan'], 'nodedotjs')
        b += box(882, 96, 270, 96, *t['host'], C['mint'])
        b += flow_dashes('M318 128H465', C['lilac'], 1.6) + flow_dashes('M465 162H318', C['pink'], 1.6, 5, '1 14')
        b += text(391, 118, t['cmd'], 13, C['lilac2'], anchor='middle', mono=True) + text(391, 186, t['evt'], 13, C['pink'], anchor='middle', mono=True)
        path, xs = 'M600 192V246H120V300H1017V192', [120 + i * 107 for i in range(8)]
        lens = [54 + 480 + 54 + (x - 120) for x in xs]
        total, gate_d = 54 + 480 + 54 + 897 + 108, 54 + 480 + 54 + 897
        b += f'<path d="{path}" fill="none" stroke="url(#chain)" stroke-width="2.4" opacity=".55"/>'
        for i, (x, label) in enumerate(zip(xs, t['checks'])):
            delay = period * .8 * lens[i] / total
            b += (f'<circle cx="{x}" cy="300" r="9" fill="{C["ink"]}" stroke="{C["lilac"]}" stroke-width="2"/>'
                  f'<circle class="ring" style="animation-delay:{delay:.2f}s" cx="{x}" cy="300" r="15" fill="none" stroke="{C["mint2"]}" stroke-width="2.4"/>')
            b += text(x, 340, label, 15, C['soft'], anchor='middle')
        b += (f'<rect class="gate" x="947" y="280" width="140" height="40" rx="20" fill="{C["ink"]}" stroke="{C["amber"]}" stroke-width="2" '
              f'style="animation-delay:{period * .8 * gate_d / total:.2f}s"/>') + text(1017, 306, t['gate'], 17, C['amber'], 700, anchor='middle')
        b += text(1017, 346, t['gate_note'][0], 14, C['amber'], anchor='middle') + text(1017, 366, t['gate_note'][1], 14, '#FDE68A', anchor='middle')
        b += f'<path d="M654 192V392" stroke="{C["cyan"]}" stroke-opacity=".5" stroke-dasharray="4 6"/>'
        b += (f'<rect x="48" y="392" width="380" height="68" rx="16" fill="none" stroke="{C["lilac"]}" stroke-opacity=".5" stroke-dasharray="5 6"/>'
              + text(68, 418, t['local'][0], 12, C['lilac2'], 700, spacing=2.4) + text(68, 444, t['local'][1], 17, C['soft']))
        b += (f'<rect x="470" y="392" width="682" height="68" rx="16" fill="none" stroke="{C["cyan"]}" stroke-opacity=".5" stroke-dasharray="5 6"/>'
              + text(490, 418, t['cloud'][0], 12, C['cyan'], 700, spacing=2.4) + text(490, 444, t['cloud'][1], 17, C['soft']))
        b += text(w - 40, h - 14, T[lang]['illus'], 13, C['muted'], anchor='end')
    defs += linear('chain', [(0, C['violet']), (.6, C['cyan']), (1, C['amber'])], x2=1, y2=1 if mobile else 0)
    b += (f'<g class="live"><g><circle r="16" fill="{C["cyan"]}" opacity=".25"/><circle r="6" fill="#E9FDFF"/>'
          f'<animateMotion dur="{period}s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;.8;1" calcMode="linear" path="{path}"/></g></g>')
    motion = ('@keyframes flow{to{stroke-dashoffset:-36}}'
              f'.ring{{opacity:.15;animation:lit {period}s ease-out infinite}}@keyframes lit{{0%{{opacity:1}}30%{{opacity:.7}}75%,100%{{opacity:.15}}}}'
              f'.gate{{animation:gate {period}s ease-out infinite}}@keyframes gate{{0%{{stroke-width:5;fill:#3A2A06}}25%,100%{{stroke-width:2;fill:{C["ink"]}}}}}')
    return document(w, h, t['bid_title'], t['bid_desc'], b, defs, motion)


def packet(x1, y1, x2, y2, color, dur, delay, name):
    dx, dy = x2 - x1, y2 - y1
    css = (f'.{name}{{animation:{name} {dur}s cubic-bezier(.5,0,.5,1) infinite;animation-delay:{delay}s}}'
           f'@keyframes {name}{{0%{{transform:translate(0,0);opacity:0}}5%{{opacity:1}}35%{{transform:translate({dx}px,{dy}px);opacity:1}}42%,100%{{transform:translate({dx}px,{dy}px);opacity:0}}}}')
    el = f'<g class="live"><g class="{name}"><circle cx="{x1}" cy="{y1}" r="13" fill="{color}" opacity=".25"/><circle cx="{x1}" cy="{y1}" r="5.5" fill="#F4FBFF"/></g></g>'
    return el, css


def shield(x, y, color, cls=''):
    return (f'<g transform="translate({x - 13} {y - 15})"><path class="{cls}" d="M13 0l13 5v9c0 8-6 14-13 16C6 28 0 22 0 14V5z" fill="{C["ink"]}" stroke="{color}" stroke-width="2"/>'
            f'<path d="M8 15l4 4 7-8" fill="none" stroke="{color}" stroke-width="2.4" stroke-linecap="round"/></g>')


def arch_tlr(lang, mobile):
    t = A[lang]
    blurple = '#5865F2'
    css = '@keyframes flow{to{stroke-dashoffset:-36}}.sh{animation:sh 6s ease-out infinite;animation-delay:3.4s}@keyframes sh{0%{stroke-width:5}30%,100%{stroke-width:2}}'
    if not mobile:
        w, h = 1200, 470
        defs, b = arch_frame(w, h, t['tlr_kicker'], C['cyan'])
        b += f'<rect x="400" y="70" width="400" height="52" rx="26" fill="{C["ink"]}" stroke="{C["lilac"]}" stroke-opacity=".7" stroke-dasharray="6 6"/>'
        b += text(600, 103, t['roles'], 18, C['lilac2'], 700, anchor='middle')
        b += f'<path d="M440 122V170M800 96H1040V170" fill="none" stroke="{C["lilac"]}" stroke-opacity=".55" stroke-dasharray="4 6"/>'
        xs = [40, 320, 600, 920]
        for x, spec, col, logo in zip(xs, [t['discord'], t['bot'], t['pg'], t['portal']], [blurple, C['violet'], '#4F7BFF', C['cyan']],
                                      ['discord', 'nodedotjs', 'postgresql', 'nextdotjs']):
            b += box(x, 170, 240, 96, *spec, col, logo, 19, compact=True)
        b += box(920, 352, 240, 76, *t['staff'], C['mint'], None, 19)
        b += flow_dashes('M280 218H320', blurple, 1.2, 3, '6 8')
        b += f'<path d="M560 210H600" stroke="{C["violet"]}" stroke-opacity=".5" stroke-width="2"/>'
        b += f'<path d="M920 206H840" stroke="{C["cyan"]}" stroke-opacity=".5" stroke-width="2"/>'
        b += flow_dashes('M840 236H920', C['mint'], 2.2, 1.5, '3 7')
        b += flow_dashes('M1040 352V266', C['mint'], 2.4, 1.5, '3 7')
        b += shield(880, 206, C['amber'], 'sh')
        p1, c1 = packet(560, 210, 600, 210, C['violet'], 5, 0, 'pk1')
        p2, c2 = packet(920, 206, 840, 206, C['cyan'], 6, 2.2, 'pk2')
        b += p1 + p2
        css += c1 + c2
        for cx_, lines, col in [(300, t['l1'], '#8C9EFF'), (580, t['l2'], C['lilac2']), (880, t['l3'], C['amber'])]:
            for i, line in enumerate(lines):
                b += text(cx_, 300 + i * 20, line, 14, col if i == 0 else '#FDE68A', anchor='middle', mono=True)
        b += text(720, 344, t['audit'], 14, C['muted'], anchor='middle')
        b += text(w - 40, h - 14, T[lang]['illus'], 13, C['muted'], anchor='end')
    else:
        w, h = 600, 1080
        defs, b = arch_frame(w, h, t['tlr_kicker'], C['cyan'])
        ys = [86, 262, 438, 614]
        specs = [(t['discord'], blurple, 'discord'), (t['bot'], C['violet'], 'nodedotjs'), (t['pg'], '#4F7BFF', 'postgresql'), (t['portal'], C['cyan'], 'nextdotjs')]
        for y, (spec, col, logo) in zip(ys, specs):
            b += box(40, y, 520, 90, *spec, col, logo, title_size=26, sub_size=19)
        b += flow_dashes('M300 176V262', blurple, 1.2, 3, '6 8')
        b += f'<path d="M300 352V438" stroke="{C["violet"]}" stroke-opacity=".5" stroke-width="2"/>'
        b += f'<path d="M280 614V528" stroke="{C["cyan"]}" stroke-opacity=".5" stroke-width="2"/>'
        b += flow_dashes('M330 528V614', C['mint'], 2.2, 1.5, '3 7')
        b += shield(280, 572, C['amber'], 'sh')
        p1, c1 = packet(300, 352, 300, 438, C['violet'], 5, 0, 'pk1')
        p2, c2 = packet(280, 614, 280, 528, C['cyan'], 6, 2.2, 'pk2')
        b += p1 + p2
        css += c1 + c2
        b += text(322, 226, t['l1'][0], 18, '#8C9EFF', mono=True)
        b += text(322, 402, t['l2'][0], 18, C['lilac2'], mono=True)
        b += text(344, 564, t['l3'][0], 17, C['amber'], mono=True) + text(344, 590, t['l3'][1], 17, '#FDE68A', mono=True)
        b += flow_dashes('M300 790V704', C['mint'], 2.4, 1.5, '3 7')
        b += box(40, 790, 520, 86, *t['staff'], C['mint'], title_size=26, sub_size=19)
        b += f'<rect x="40" y="910" width="520" height="64" rx="32" fill="{C["ink"]}" stroke="{C["lilac"]}" stroke-opacity=".7" stroke-dasharray="6 6"/>'
        b += text(300, 950, t['roles_m'], 20, C['lilac2'], 700, anchor='middle')
        b += text(300, 1012, t['audit'], 18, C['muted'], anchor='middle')
        b += text(w / 2, h - 20, T[lang]['illus'], 16, C['muted'], anchor='middle')
    return document(w, h, t['tlr_title'], t['tlr_desc'], b, defs, css)


# ---------------------------------------------------------------- technology
GROUPS = {
    'tools': ('violet', {'en': 'Additional Tools & Interests', 'bg': 'Допълнителни инструменти и интереси'}),
    'languages': ('pink', {'en': 'Wider Programming Language Ecosystem', 'bg': 'Други програмни езици'}),
    'web': ('cyan', {'en': 'Web & Application Ecosystem', 'bg': 'Уеб технологии и приложения'}),
    'data': ('mint', {'en': 'Data, Infrastructure & Delivery', 'bg': 'Данни, инфраструктура и публикуване'}),
    'games': ('amber', {'en': 'Games, Communities & AI', 'bg': 'Игри, общности и AI'}),
}
TS = {
    'en': {'count': '{n} technologies', 'legend': 'used in the featured products', 'used_title': 'Used in the featured products',
           'used_sub': 'Verified in the inspected implementations. The same tools carry a mint ring in the panels below.',
           'kinds': {'bid': 'native macOS app', 'police': 'web portal + Discord bot', 'community': 'React frontend · source showcase',
                     'client': 'client website', 'space': 'browser experiment', 'tlr': 'Next.js site + Discord platform'},
           'names': {'community': 'Community platform'}, 'group_desc': 'Interests and possible project choices: {names}.'},
    'bg': {'count': '{n} технологии', 'legend': 'използвано в представените проекти', 'used_title': 'Използвано в представените проекти',
           'used_sub': 'Проверено в прегледаните реализации. Същите инструменти имат ментов кръг в панелите по-долу.',
           'kinds': {'bid': 'нативно macOS приложение', 'police': 'уеб портал + Discord бот', 'community': 'React интерфейс · преглед на кода',
                     'client': 'клиентски сайт', 'space': 'браузърен експеримент', 'tlr': 'Next.js сайт + Discord платформа'},
           'names': {'community': 'Общностна платформа'}, 'group_desc': 'Интереси и възможни избори: {names}.'},
}


def shape(w, h, variant):
    cut = 46
    if variant == 0:
        return f'M24 0H{w - cut}L{w} {cut}V{h - 24}Q{w} {h} {w - 24} {h}H24Q0 {h} 0 {h - 24}V24Q0 0 24 0Z'
    if variant == 1:
        return f'M40 0H{w - 40}Q{w} 0 {w} 40V{h - 40}Q{w} {h} {w - 40} {h}H40Q0 {h} 0 {h - 40}V40Q0 0 40 0Z'
    if variant == 2:
        return f'M{cut} 0H{w - 24}Q{w} 0 {w} 24V{h - cut}L{w - cut} {h}H24Q0 {h} 0 {h - 24}V{cut}Z'
    if variant == 3:
        return f'M24 0H{w - 24}Q{w} 0 {w} 24V{h - 24}Q{w} {h} {w - 24} {h}H{cut}L0 {h - cut}V24Q0 0 24 0Z'
    return f'M24 0H{w * .62:.0f}L{w * .62 + 30:.0f} 22H{w - 24}Q{w} 22 {w} 46V{h - 24}Q{w} {h} {w - 24} {h}H24Q0 {h} 0 {h - 24}V24Q0 0 24 0Z'


def logo_tile(item, x, y, size):
    """Badge-style tile: original badge colour as background, original logo colour."""
    out = (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .25:.0f}" fill="{item["tile"]}"/>'
           f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .25:.0f}" fill="url(#shine)"/>'
           f'<rect x="{x + .75}" y="{y + .75}" width="{size - 1.5}" height="{size - 1.5}" rx="{size * .25:.0f}" fill="none" stroke="#fff" stroke-opacity=".2" stroke-width="1.5"/>')
    if item.get('icon'):
        s = size * .5
        out += icon(item['icon'], x + (size - s) / 2, y + (size - s) / 2, s, item['ink'])
    else:
        mono = item['monogram']
        fs = size * (.36 if len(mono) <= 2 else .3 if len(mono) == 3 else .25)
        out += text(x + size / 2, y + size / 2 + fs * .36, mono, round(fs), item['ink'], 800, anchor='middle')
    return out


def stack_group(group, variant, lang, mobile):
    accent, titles = GROUPS[group]
    a1, a2 = ACCENTS[accent]
    items = [i for i in TECH['technologies'] if i['group'] == group]
    n = len(items)
    w = 600 if mobile else 1200
    cell_w, cell_h, tile, gap = (134, 178, 96, 8) if mobile else (128, 150, 86, 12)
    if mobile:
        cols = 4
    else:
        rows_ = math.ceil(n / 8)
        cols = math.ceil(n / rows_)
    rows = math.ceil(n / cols)
    title = titles[lang]
    title_lines = wrap(title, 24) if mobile else [title]
    head = (118 if mobile else 106) + (len(title_lines) - 1) * 38 + (40 if mobile and any(i['featured'] for i in items) else 0)
    h = head + rows * cell_h + 34
    step = .62
    defs = (linear('g', [(0, a1), (1, a2)]) + radial('au1', a1, .42) + radial('au2', a2, .32)
            + linear('bg', [(0, C['ink']), (.65, C['indigo']), (1, C['deep'])], x2=1, y2=1)
            + linear('shine', [(0, '#fff', .28), (.5, '#fff', .04), (1, '#000', .12)], x2=0, y2=1)
            + f'<clipPath id="panel"><path d="{shape(w, h, variant)}"/></clipPath>')
    motion = (f'.aur{{animation:aur 26s ease-in-out infinite}}.aur2{{animation:aur 34s ease-in-out infinite reverse}}@keyframes aur{{50%{{transform:translate(-80px,30px)}}}}'
              f'.contour{{animation:contour 18s linear infinite}}@keyframes contour{{to{{stroke-dashoffset:-1000}}}}'
              f'.seq{{opacity:0;animation:seq {n * step:.2f}s ease-in-out infinite}}'
              f'@keyframes seq{{0%{{opacity:0}}{100 / n * .6:.2f}%{{opacity:1}}{100 / n * 2.2:.2f}%,100%{{opacity:0}}}}')
    b = f'<path d="{shape(w, h, variant)}" fill="url(#bg)"/>'
    b += (f'<g clip-path="url(#panel)"><g class="aur"><circle cx="{w * .85:.0f}" cy="{h * .15:.0f}" r="{max(w, h) * .45:.0f}" fill="url(#au1)"/></g>'
          f'<g class="aur2"><circle cx="{w * .12:.0f}" cy="{h * .9:.0f}" r="{max(w, h) * .38:.0f}" fill="url(#au2)"/></g></g>')
    b += f'<path d="{shape(w, h, variant)}" fill="none" stroke="url(#g)" stroke-opacity=".55" stroke-width="1.5"/>'
    b += (f'<path class="live contour" d="{shape(w, h, variant)}" fill="none" stroke="#fff" stroke-width="2.5" pathLength="1000" stroke-dasharray="60 440" stroke-linecap="round"/>')
    x0 = 32 if mobile else 48
    b += text(x0, 52, TS[lang]['count'].format(n=n).upper(), 18 if mobile else 13, a1, 800, spacing=2.4)
    for i, line in enumerate(title_lines):
        b += text(x0, (98 if mobile else 92) + i * 38, line, 33 if mobile else 31, C['text'], 800)
    if any(i['featured'] for i in items):
        lx, ly = (x0 + 12, head - 22) if mobile else (w - 48, 52)
        legend = TS[lang]['legend']
        if mobile:
            b += f'<circle cx="{lx}" cy="{ly - 7}" r="11" fill="none" stroke="{C["mint"]}" stroke-width="3"/>' + text(lx + 22, ly, legend, 19, C['soft'])
        else:
            b += f'<circle cx="{lx - len(legend) * 6.9 - 16:.0f}" cy="{ly - 5}" r="9" fill="none" stroke="{C["mint"]}" stroke-width="2.5"/>' + text(lx, ly, legend, 15, C['soft'], anchor='end')
    grid_w = cols * cell_w + (cols - 1) * gap
    for idx, item in enumerate(items):
        r_, c_ = divmod(idx, cols)
        in_row = min(cols, n - r_ * cols)
        row_w = in_row * cell_w + (in_row - 1) * gap
        sx = (w - row_w) / 2 if not mobile else (w - grid_w) / 2
        cx_ = sx + c_ * (cell_w + gap) + cell_w / 2
        ty = head + r_ * cell_h + 10
        tx = cx_ - tile / 2
        if item['featured']:
            b += f'<rect x="{tx - 6}" y="{ty - 6}" width="{tile + 12}" height="{tile + 12}" rx="{tile * .3:.0f}" fill="none" stroke="{C["mint"]}" stroke-width="2.5"/>'
        b += logo_tile(item, tx, ty, tile)
        b += (f'<rect class="live seq" style="animation-delay:{idx * step:.2f}s" x="{tx - 4}" y="{ty - 4}" width="{tile + 8}" height="{tile + 8}" '
              f'rx="{tile * .28:.0f}" fill="#fff" fill-opacity=".14" stroke="#fff" stroke-width="2.5"/>')
        if mobile:
            parts = item['name'].split(' ', 1) if len(item['name']) > 10 and ' ' in item['name'] else [item['name']]
            for j, part in enumerate(parts):
                b += text(cx_, ty + tile + 30 + j * 22, part, 19, C['soft'], 600, anchor='middle')
        else:
            b += text(cx_, ty + tile + 30, item['name'], 15 if len(item['name']) < 13 else 14, C['soft'], 600, anchor='middle')
    names = ', '.join(i['name'] + (' (featured)' if i['featured'] else '') for i in items)
    desc = TS[lang]['group_desc'].format(names=names)
    return document(w, h, f'{title} — {n}', desc, b, defs, motion)


def stack_used(lang, mobile):
    w = 600 if mobile else 1200
    tile, cell_w, cell_h = (92, 134, 166) if mobile else (78, 118, 132)
    products = TECH['products']
    rows = []
    m_title = wrap(TS[lang]['used_title'], 26)
    m_sub = wrap(TS[lang]['used_sub'], 46)[:3]
    y = 150 if not mobile else 98 + len(m_title) * 34 + len(m_sub) * 24 + 24
    for p in products:
        n = len(p['items'])
        if mobile:
            per = 4
            r = math.ceil(n / per)
            rows.append((p, y, r))
            y += 78 + r * cell_h + 12
        else:
            rows.append((p, y, 1))
            y += cell_h + 16
    h = y + 24
    defs = (linear('bg', [(0, C['night']), (.5, '#141046'), (1, C['deep'])], x2=1, y2=1)
            + linear('g', [(0, C['violet']), (.5, C['cyan']), (1, C['mint'])])
            + radial('au1', C['violet'], .4) + radial('au2', C['mint'], .3))
    for p in products:
        for it in p['items']:
            col = ICONS[it[1]]['hex'] if it[1] else it[2]
            gid = 'h' + col.strip('#')
            if gid not in defs:
                defs += radial(gid, col if col != '#000000' else '#9CA3AF', .55)
    total = sum(len(p['items']) for p in products)
    step = .45
    motion = (f'.aur{{animation:aur 28s ease-in-out infinite}}@keyframes aur{{50%{{transform:translate(-90px,40px)}}}}'
              f'.seq{{opacity:0;animation:seq {total * step:.2f}s ease-in-out infinite}}'
              f'@keyframes seq{{0%{{opacity:0}}{100 / total * .7:.2f}%{{opacity:1}}{100 / total * 3:.2f}%,100%{{opacity:0}}}}')
    b = frame(w, h, 30) + '<g clip-path="url(#frame)">'
    b += f'<g class="aur"><circle cx="{w * .8:.0f}" cy="{h * .1:.0f}" r="{w * .5:.0f}" fill="url(#au1)"/></g><circle cx="{w * .1:.0f}" cy="{h:.0f}" r="{w * .45:.0f}" fill="url(#au2)"/>'
    b += f'<rect x="0" y="0" width="{w}" height="4" fill="url(#g)"/>'
    x0 = 32 if mobile else 48
    b += text(x0, 58, 'VERIFIED · IN USE' if lang == 'en' else 'ПРОВЕРЕНО · В УПОТРЕБА', 17 if mobile else 13, C['mint'], 800, spacing=2.4)
    if mobile:
        for i, line in enumerate(m_title):
            b += text(x0, 98 + i * 34, line, 29, C['text'], 800)
        sub_y = 98 + len(m_title) * 34 - 4
        for i, line in enumerate(m_sub):
            b += text(x0, sub_y + i * 24, line, 18, C['muted'])
    else:
        b += text(x0, 98, TS[lang]['used_title'], 32, C['text'], 800)
        b += text(x0, 128, TS[lang]['used_sub'], 16, C['muted'])
    k = 0
    for p, y, r in rows:
        color = PRODUCT_COLORS.get(p['key'], C['lilac'])
        name = TS[lang]['names'].get(p['key'], p['name'])
        kind = TS[lang]['kinds'][p['key']]
        if mobile:
            b += f'<circle cx="{x0 + 8}" cy="{y + 18}" r="8" fill="{color}"/>' + text(x0 + 26, y + 26, name, 25, C['text'], 800)
            b += text(x0 + 26, y + 54, kind, 18, C['muted'])
            ty0, sx = y + 78, (w - 4 * cell_w) / 2
        else:
            b += f'<circle cx="{x0 + 7}" cy="{y + 34}" r="7" fill="{color}"/>' + text(x0 + 24, y + 41, name, 21, C['text'], 800)
            b += text(x0 + 24, y + 66, kind, 14, C['muted'])
            b += f'<path d="M{x0} {y + cell_h + 4}H{w - x0}" stroke="#fff" stroke-opacity=".07"/>'
            ty0, sx = y + 4, 330
        for i, it in enumerate(p['items']):
            rr, cc = divmod(i, 4) if mobile else (0, i)
            cx_ = sx + cc * cell_w + cell_w / 2
            ty = ty0 + rr * cell_h
            tx = cx_ - tile / 2
            col = ICONS[it[1]]['hex'] if it[1] else it[2]
            ink = '#FFFFFF' if col in ('#000000',) else col
            b += f'<circle cx="{cx_}" cy="{ty + tile / 2}" r="{tile * .78:.0f}" fill="url(#h{col.strip("#")})" opacity=".55"/>'
            b += (f'<rect x="{tx}" y="{ty}" width="{tile}" height="{tile}" rx="{tile * .28:.0f}" fill="#0E0B2C" fill-opacity=".9" stroke="{ink}" stroke-opacity=".55" stroke-width="1.5"/>')
            if it[1]:
                b += icon(it[1], tx + tile * .24, ty + tile * .24, tile * .52, ink)
            else:
                mono = it[3]
                b += text(cx_, ty + tile / 2 + 7, mono, 19 if len(mono) <= 3 else 16, ink, 800, anchor='middle')
            b += (f'<rect class="live seq" style="animation-delay:{k * step:.2f}s" x="{tx - 4}" y="{ty - 4}" width="{tile + 8}" height="{tile + 8}" '
                  f'rx="{tile * .3:.0f}" fill="{ink}" fill-opacity=".16" stroke="{ink}" stroke-width="2.5"/>')
            if mobile:
                parts = it[0].split(' ', 1) if len(it[0]) > 10 and ' ' in it[0] else [it[0]]
                for j, part in enumerate(parts):
                    b += text(cx_, ty + tile + 28 + j * 21, part, 18, C['soft'], 600, anchor='middle')
            else:
                b += text(cx_, ty + tile + 24, it[0], 13 if len(it[0]) > 11 else 14, C['soft'], 600, anchor='middle')
            k += 1
    b += '</g>'
    desc = '; '.join(f"{TS[lang]['names'].get(p['key'], p['name'])}: " + ', '.join(i[0] for i in p['items']) for p in products)
    return document(w, h, TS[lang]['used_title'], desc, b, defs, motion)


# ---------------------------------------------------------------- process
P = {
    'en': {'kicker': 'PROCESS · 5 STEPS', 'title': 'From idea to working product',
           'steps': [('Discover', 'Understand your goals, users and requirements'), ('Design', 'Define the interface, architecture and scope'),
                     ('Build', 'Develop features and connect the systems'), ('Validate', 'Test behavior, fix issues and check readiness'),
                     ('Launch', 'Deploy, document and plan the next improvements')]},
    'bg': {'kicker': 'ПРОЦЕС · 5 СТЪПКИ', 'title': 'От идея до работещ продукт',
           'steps': [('Проучване', 'Цели, потребители и изисквания'), ('Дизайн', 'Интерфейс, архитектура и обхват'),
                     ('Разработка', 'Функции и интеграции'), ('Проверка', 'Поведение, грешки и готовност'),
                     ('Публикуване', 'Публикуване, документация и следващи подобрения')]},
}
STEP_COLORS = [C['violet'], C['pink'], C['cyan'], C['mint'], C['amber']]


def process(lang, mobile):
    t = P[lang]
    period = 12.0
    defs = (linear('bg', [(0, C['ink']), (.6, '#160F42'), (1, C['deep'])], x2=1, y2=1)
            + linear('rib', [(0, C['violet']), (.25, C['pink']), (.5, C['cyan']), (.75, C['mint']), (1, C['amber'])], x2=1 if not mobile else 0, y2=0 if not mobile else 1)
            + radial('au', C['violet'], .35) + ''.join(radial(f's{i}', c, .6) for i, c in enumerate(STEP_COLORS)))
    if mobile:
        w, h = 600, 1090
        pts = [(80, 150 + i * 190) for i in range(5)]
        path = f'M80 150V{150 + 4 * 190}'
    else:
        w, h = 1200, 440
        pts = [(130 + i * 235, 170 if i % 2 == 0 else 236) for i in range(5)]
        path = f'M{pts[0][0]} {pts[0][1]}' + ''.join(
            f'C{a[0] + 110} {a[1]} {b_[0] - 110} {b_[1]} {b_[0]} {b_[1]}' for a, b_ in zip(pts, pts[1:]))
    motion = (f'.st{{animation:st {period}s ease-out infinite}}@keyframes st{{0%{{opacity:.95;transform:scale(1.25)}}20%{{opacity:.35;transform:scale(1)}}100%{{opacity:.35;transform:scale(1)}}}}'
              '.aur{animation:aur 30s ease-in-out infinite}@keyframes aur{50%{transform:translate(60px,-30px)}}')
    b = frame(w, h, 28) + '<g clip-path="url(#frame)">'
    b += f'<g class="aur"><circle cx="{w * .5:.0f}" cy="{h * .5:.0f}" r="{max(w, h) * .45:.0f}" fill="url(#au)"/></g>'
    b += text(40 if not mobile else 32, 52, t['kicker'], 18 if mobile else 13, C['lilac2'], 800, spacing=2.4)
    b += f'<path d="{path}" fill="none" stroke="url(#rib)" stroke-width="10" stroke-opacity=".18" stroke-linecap="round"/>'
    b += f'<path d="{path}" fill="none" stroke="url(#rib)" stroke-width="2.5" stroke-linecap="round"/>'
    for i, ((x, y), (name, desc)) in enumerate(zip(pts, t['steps'])):
        col = STEP_COLORS[i]
        b += (f'<circle class="live st" style="animation-delay:{i * period * .8 / 4:.2f}s;transform-box:fill-box;transform-origin:center" cx="{x}" cy="{y}" r="58" fill="url(#s{i})"/>'
              f'<circle class="still" cx="{x}" cy="{y}" r="58" fill="url(#s{i})" opacity=".35"/>'
              f'<circle cx="{x}" cy="{y}" r="34" fill="{C["ink"]}" stroke="{col}" stroke-width="2.5"/>')
        b += text(x, y + 8, f'{i + 1:02d}', 21, col, 800, anchor='middle')
        if mobile:
            b += text(140, y - 8, name, 28, C['text'], 800)
            for j, line in enumerate(wrap(desc, 28)):
                b += text(140, y + 24 + j * 26, line, 20, C['soft'])
        else:
            ty = y + 72
            b += text(x, ty, name, 21, C['text'], 800, anchor='middle')
            for j, line in enumerate(wrap(desc, 22)):
                b += text(x, ty + 26 + j * 21, line, 15, C['soft'], anchor='middle')
    b += (f'<g class="live"><g><circle r="18" fill="#fff" opacity=".18"/><circle r="6" fill="#fff"/>'
          f'<animateMotion dur="{period}s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;.8;1" calcMode="linear" path="{path}"/></g></g>')
    b += '</g>'
    desc = '; '.join(f'{i + 1:02d} {n}: {d}' for i, (n, d) in enumerate(t['steps']))
    return document(w, h, t['title'], desc, b, defs, motion)


# ---------------------------------------------------------------- finale & footer
F = {
    'en': {'status': 'AVAILABLE FOR PAID PROJECTS', 'head': 'What should we build next?',
           'sub': 'A website, a custom tool, a bot or your next big idea.',
           'sub2': 'Send the idea, main features, timeline and budget range — we define the scope together.',
           'labels': ['EMAIL', 'DISCORD', 'INSTAGRAM'],
           'title': 'Contact Yavor', 'words': ['WEBSITES', 'SOFTWARE', 'BOTS', 'GAMES', 'AUTOMATION'],
           'tag': 'Your idea. A clear plan. Software that works.', 'steps': 'BUILD · TEST · VERIFY · DEPLOY · IMPROVE'},
    'bg': {'status': 'ПРИЕМАМ ПЛАТЕНИ ПРОЕКТИ', 'head': 'Какво да създадем следващо?',
           'sub': 'Сайт, инструмент, бот или следващата ви идея.',
           'sub2': 'Изпратете идеята, основните функции, срока и бюджета — ще уточним обхвата заедно.',
           'labels': ['ИМЕЙЛ', 'DISCORD', 'INSTAGRAM'],
           'title': 'Контакт с Явор', 'words': ['САЙТОВЕ', 'СОФТУЕР', 'БОТОВЕ', 'ИГРИ', 'АВТОМАТИЗАЦИИ'],
           'tag': 'Вашата идея. Ясен план. Работещ софтуер.', 'steps': 'СЪЗДАВАНЕ · ТЕСТВАНЕ · ПРОВЕРКА · ПУБЛИКУВАНЕ · РАЗВИТИЕ'},
}
CARDS = [('mail', 'Fraisbg1@gmail.com', C['pink']),
         ('discord', 'Fraisbg', '#7C8BFF'), ('instagram', '@y.yakowvw.sales', '#FF4F93')]


def finale(lang, mobile):
    t = F[lang]
    w, h = (600, 560) if mobile else (1200, 340)
    sx, sy = w / 2, h + 40
    defs = (linear('bg', [(0, C['night']), (.55, '#1B0F3E'), (1, '#2A0E2E')], x2=0, y2=1)
            + radial('sun', C['amber2'], .6) + radial('pk', C['magenta'], .5) + radial('vi', C['violet'], .45)
            + linear('hg', [(0, C['amber']), (.5, C['pink']), (1, C['lilac2'])])
            + linear('ray', [(0, '#FFD89B', .0), (1, '#FFD89B', .18)], x2=0, y2=1))
    rays = ''.join(f'<path d="M{sx} {sy}L{sx + math.cos(math.radians(a)) * 1400:.0f} {sy + math.sin(math.radians(a)) * 1400:.0f}L{sx + math.cos(math.radians(a + 3)) * 1400:.0f} {sy + math.sin(math.radians(a + 3)) * 1400:.0f}Z" fill="#FFD89B" opacity=".06"/>'
                   for a in range(180, 361, 12))
    n = len(CARDS)
    motion = ('.rays{transform-origin:%.0fpx %.0fpx;animation:spin 120s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}' % (sx, sy)
              + '.sun{transform-box:fill-box;transform-origin:center;animation:sun 14s ease-in-out infinite}@keyframes sun{50%{transform:scale(1.08)}}'
              + f'.cg{{opacity:0;animation:cg {n * 2.2}s ease-in-out infinite}}@keyframes cg{{0%,100%{{opacity:0}}6%,20%{{opacity:1}}28%{{opacity:0}}}}'
              + '.orb{transform-box:view-box;transform-origin:%.0fpx %.0fpx;animation:spin 70s linear infinite reverse}' % (sx, sy))
    b = frame(w, h, 32) + '<g clip-path="url(#frame)">'
    b += f'<g class="rays">{rays}</g>'
    b += (f'<circle class="sun" cx="{sx}" cy="{sy}" r="{h * .75:.0f}" fill="url(#sun)"/>'
          f'<circle cx="{w * .18:.0f}" cy="{h * .78:.0f}" r="{w * .32:.0f}" fill="url(#pk)"/><circle cx="{w * .86:.0f}" cy="{h * .25:.0f}" r="{w * .3:.0f}" fill="url(#vi)"/>')
    for i in range(4):
        rr = h * (.42 + i * .16)
        b += f'<circle cx="{sx}" cy="{sy}" r="{rr:.0f}" fill="none" stroke="#FFD89B" stroke-opacity="{.22 - i * .04:.2f}" stroke-dasharray="{3 + i} {9 + i * 3}"/>'
    b += '<g class="live orb">' + ''.join(
        f'<circle cx="{sx + math.cos(math.radians(a)) * h * 1.02:.0f}" cy="{sy + math.sin(math.radians(a)) * h * 1.02:.0f}" r="{3 + i % 3}" fill="{[C["amber"], C["pink"], C["lilac2"], C["mint"]][i % 4]}"/>'
        for i, a in enumerate(range(190, 350, 26))) + '</g>'
    b += stars(w, h * .5, 30, 9)
    # status + headline
    sw = len(t['status']) * 11.4 + 64
    b += (f'<rect x="{sx - sw / 2:.0f}" y="{48 if not mobile else 52}" width="{sw:.0f}" height="38" rx="19" fill="#0B2A22" fill-opacity=".85" stroke="{C["mint"]}" stroke-opacity=".7"/>'
          f'<circle cx="{sx - sw / 2 + 22:.0f}" cy="{(48 if not mobile else 52) + 19}" r="5.5" fill="#4ADE80"/>')
    b += text(sx - sw / 2 + 40, (48 if not mobile else 52) + 25, t['status'], 15, '#B3F6D2', 800, spacing=1.6)
    if mobile:
        lines = wrap(t['head'], 16)
        fs = min(fit(line, 40, w - 64) for line in lines)
        for i, line in enumerate(lines):
            b += display(line, sx, 160 + i * fs * 1.3, fs, 'url(#hg)', anchor='middle')
        y = 160 + len(lines) * fs * 1.3 + 6
        for i, line in enumerate(wrap(t['sub'], 34)):
            b += text(sx, y + i * 28, line, 21, C['text'], 600, anchor='middle')
        y += len(wrap(t['sub'], 34)) * 28 + 12
        for i, line in enumerate(wrap(t['sub2'], 44)):
            b += text(sx, y + i * 26, line, 19, C['soft'], anchor='middle')
        cards = []
    else:
        b += display(t['head'], sx, 168, fit(t['head'], 50, 1060), 'url(#hg)', anchor='middle')
        b += text(sx, 216, t['sub'], 23, C['text'], 600, anchor='middle')
        b += text(sx, 252, t['sub2'], 18, C['soft'], anchor='middle')
        cards = []
    for i, ((kind, value, col), (x, y, cw, ch)) in enumerate(zip(CARDS, cards)):
        b += f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="24" fill="#0C0926" fill-opacity=".82" stroke="{col}" stroke-opacity=".75" stroke-width="1.6"/>'
        b += f'<rect class="live cg" style="animation-delay:{i * 2.2}s" x="{x - 3}" y="{y - 3}" width="{cw + 6}" height="{ch + 6}" rx="26" fill="{col}" fill-opacity=".1" stroke="{col}" stroke-width="3"/>'
        if mobile:
            b += f'<circle cx="{x + 56}" cy="{y + ch / 2}" r="30" fill="{col}" fill-opacity=".18"/>' + glyph(kind, x + 42, y + ch / 2 - 14, 28, col)
            b += text(x + 104, y + ch / 2 - 10, t['labels'][i], 18, col, 800, spacing=2)
            b += text(x + 104, y + ch / 2 + 24, value, 26, C['text'], 700)
        else:
            b += f'<circle cx="{x + 50}" cy="{y + 50}" r="28" fill="{col}" fill-opacity=".18"/>' + glyph(kind, x + 36, y + 36, 28, col)
            b += text(x + 26, y + 112, t['labels'][i], 13, col, 800, spacing=2.4)
            b += text(x + 26, y + 138, value, 19 if len(value) < 17 else 18, C['text'], 700)
    b += '</g>'
    desc = f"{t['status']}. {t['head']} {t['sub']} {t['sub2']}"
    return document(w, h, t['title'], desc, b, defs, motion)


FOOT_COLORS = ['#2563EB', '#7C3AED', '#5865F2', '#E11D48', '#059669']


def footer(lang, mobile):
    t = F[lang]
    w, h = (600, 320) if mobile else (1200, 200)
    defs = linear('fb', [(0, C['ink']), (.5, '#1A1146'), (1, C['ink'])]) + linear('hg', [(0, C['lilac2']), (.5, C['pink']), (1, C['amber'])]) + linear('sh', [(0, '#fff', 0), (.5, '#fff', .55), (1, '#fff', 0)])
    widths = [len(wd) * 12.5 + 40 for wd in t['words']]
    rows = [list(range(5))] if not mobile else [[0, 1, 2], [3, 4]]
    b, y = f'<rect width="{w}" height="{h}" rx="26" fill="url(#fb)"/>', 26
    n = 5
    motion = f'.shn{{animation:shn {n * 1.4:.1f}s ease-in-out infinite}}@keyframes shn{{0%{{transform:translateX(-80px);opacity:0}}4%{{opacity:1}}{100 / n:.0f}%{{transform:translateX(var(--d));opacity:0}}100%{{opacity:0}}}}'
    for row in rows:
        total = sum(widths[i] for i in row) + 14 * (len(row) - 1)
        x = (w - total) / 2
        for i in row:
            pw = widths[i]
            b += f'<clipPath id="c{i}"><rect x="{x:.0f}" y="{y}" width="{pw:.0f}" height="42" rx="8"/></clipPath>'
            b += f'<rect x="{x:.0f}" y="{y}" width="{pw:.0f}" height="42" rx="8" fill="{FOOT_COLORS[i]}"/>'
            b += (f'<g clip-path="url(#c{i})" class="live"><rect class="shn" style="--d:{pw + 80:.0f}px;animation-delay:{i * 1.4:.1f}s" '
                  f'x="{x:.0f}" y="{y}" width="60" height="42" fill="url(#sh)" transform="skewX(-18)"/></g>')
            b += text(x + pw / 2, y + 28, t['words'][i], 17, '#fff', 800, anchor='middle', spacing=2)
            x += pw + 14
        y += 56
    y += 30
    tag = wrap(t['tag'], 26) if mobile else [t['tag']]
    fs = min(fit(line, 30 if not mobile else 28, w - 60) for line in tag)
    for i, line in enumerate(tag):
        b += display(line, w / 2, y + i * 38, fs, 'url(#hg)', anchor='middle')
    y += (len(tag) - 1) * 38 + 36
    steps = t['steps'] if not mobile or len(t['steps']) < 46 else t['steps'].replace(' · ', ' · ', 2)
    if mobile:
        halves = steps.split(' · ')
        b += text(w / 2, y, ' · '.join(halves[:3]), 17, C['muted'], 700, anchor='middle', mono=True)
        b += text(w / 2, y + 26, ' · '.join(halves[3:]), 17, C['muted'], 700, anchor='middle', mono=True)
    else:
        b += text(w / 2, y, steps, 15, C['muted'], 700, anchor='middle', mono=True, spacing=1)
    return document(w, h, t['tag'], f"{' · '.join(t['words'])}. {t['tag']} {t['steps']}", b, defs, motion)


# ---------------------------------------------------------------- contact buttons
BUTTONS = {
    'mail': ('Fraisbg1@gmail.com', C['pink'], {'en': 'EMAIL', 'bg': 'ИМЕЙЛ'}),
    'discord': ('Fraisbg', '#7C8BFF', {'en': 'DISCORD', 'bg': 'DISCORD'}),
    'instagram': ('@y.yakowvw.sales', '#FF4F93', {'en': 'INSTAGRAM', 'bg': 'INSTAGRAM'}),
}


def contact_button(kind, lang):
    value, col, labels = BUTTONS[kind]
    label = labels[lang]
    h = 64
    w = round(84 + max(len(value) * 10.6, len(label) * 9) + 26)
    defs = linear('bg', [(0, '#0C0926'), (1, C['indigo'])], x2=1, y2=1) + linear('edge', [(0, col), (1, col, .35)])
    b = (f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="{h / 2 - 1:.0f}" fill="url(#bg)" stroke="url(#edge)" stroke-width="2"/>'
         f'<circle cx="33" cy="{h / 2}" r="21" fill="{col}" fill-opacity=".18"/>' + glyph(kind, 21, h / 2 - 12, 24, col))
    b += text(66, 27, label, 12, col, 800, spacing=2)
    b += text(66, 48, value, 18, C['text'], 700)
    return document(w, h, f'{label}: {value}', f'{label}: {value}', b, defs)


# ---------------------------------------------------------------- certificates
CERTS = json.loads((ROOT / 'data/certificates.json').read_text())
MONTHS = {'en': 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(),
          'bg': 'яну фев мар апр май юни юли авг сеп окт ное дек'.split()}
CT = {
    'en': {'kicker': 'CREDENTIALS · {n} CERTIFICATES · {m} LESSONS', 'lead': 'Issued by Google, HubSpot Academy and Advance Academy.',
           'issued': 'Issued', 'valid': 'valid until', 'badge': 'Badge', 'cert': 'CERTIFICATION', 'course': 'COURSE',
           'program': 'Program', 'lessons_title': 'Google Applied Digital Skills', 'lessons_sub': 'project-based lessons, each with its own Google credential',
           'lessons_date': 'Completed {a} – {b}',
           'topics': {'workspace': 'Google Workspace', 'creative': 'Creative & research', 'career': 'Career & professional',
                      'data_logic': 'Data & logic', 'ai_safety': 'AI & digital safety'},
           'title': 'Certificates', 'lessons_alt': 'Google Applied Digital Skills lessons'},
    'bg': {'kicker': 'КВАЛИФИКАЦИИ · {n} СЕРТИФИКАТА · {m} УРОКА', 'lead': 'Издадени от Google, HubSpot Academy и Advance Academy.',
           'issued': 'Издаден', 'valid': 'валиден до', 'badge': 'Значка', 'cert': 'СЕРТИФИКАЦИЯ', 'course': 'КУРС',
           'program': 'Програма', 'lessons_title': 'Google Applied Digital Skills', 'lessons_sub': 'практически урока, всеки със собствен Google документ',
           'lessons_date': 'Завършени {a} – {b}',
           'topics': {'workspace': 'Google Workspace', 'creative': 'Творчество и проучване', 'career': 'Кариера и професия',
                      'data_logic': 'Данни и логика', 'ai_safety': 'AI и дигитална сигурност'},
           'title': 'Сертификати', 'lessons_alt': 'Уроци от Google Applied Digital Skills'},
}
TOPIC_COLORS = {'workspace': '#38BDF8', 'creative': '#F472B6', 'career': '#FBBF24', 'data_logic': '#34D399', 'ai_safety': '#A78BFA'}


def fmt_date(value, lang):
    y, m, d = value.split('-')
    return f'{int(d)} {MONTHS[lang][int(m) - 1]} {y}'


def cert_card(c, x, y, w, h, lang, idx, mobile):
    t = CT[lang]
    col = c['color']
    gid = f'cg{idx}'
    out = (f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{col}" stop-opacity=".22"/>'
           f'<stop offset=".55" stop-color="#0E0B2C" stop-opacity=".92"/><stop offset="1" stop-color="#0E0B2C" stop-opacity=".96"/></linearGradient>')
    out += (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24" fill="url(#{gid})" stroke="{col}" stroke-opacity=".6" stroke-width="1.6"/>'
            f'<rect x="{x + 24}" y="{y}" width="{w - 48}" height="3" rx="1.5" fill="{col}"/>')
    mx, my, r = x + 54, y + 58, 30
    out += (f'<circle cx="{mx}" cy="{my}" r="{r + 14}" fill="{col}" opacity=".12"/>'
            f'<circle class="medal" cx="{mx}" cy="{my}" r="{r + 7}" fill="none" stroke="{col}" stroke-opacity=".7" stroke-dasharray="3 6"/>'
            f'<circle cx="{mx}" cy="{my}" r="{r}" fill="#0B0824" stroke="{col}" stroke-width="2"/>')
    if c.get('icon'):
        out += icon(c['icon'], mx - 15, my - 15, 30, col if c['icon'] != 'google' else '#fff')
    else:
        out += text(mx, my + 8, c['monogram'], 21, col, 800, anchor='middle')
    kind = {'certification': t['cert'], 'course': t['course'], 'badge': t['badge'].upper()}[c['kind']]
    out += text(x + 100, y + 50, c['issuer'].upper(), 12 if not mobile else 15, col, 800, spacing=1.4)
    out += text(x + 100, y + 72, kind, 11 if not mobile else 14, C['muted'], 700, spacing=2)
    lines = wrap(c['title'], 22 if not mobile else 28)
    for i, line in enumerate(lines):
        out += text(x + 26, y + 130 + i * 30, line, 25 if not mobile else 28, C['text'], 800)
    if c.get('valid_until'):
        foot = f"{t['issued']} {fmt_date(c['issued'], lang)} · {t['valid']} {fmt_date(c['valid_until'], lang)}"
    elif c.get('period'):
        a, b2 = c['period'].split('/')
        foot = f"{t['program']} {MONTHS[lang][int(a[5:]) - 1]}–{MONTHS[lang][int(b2[5:]) - 1]} {b2[:4]} · {t['issued']} {fmt_date(c['issued'], lang)}"
    elif c.get('issued'):
        foot = f"{t['issued']} {fmt_date(c['issued'], lang)}"
    else:
        foot = f"{c.get('level', '')} · Google for Education"
    out += text(x + 26, y + h - 26, foot, 14 if not mobile else 17, C['soft'])
    out += (f'<g class="live"><clipPath id="cl{idx}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24"/></clipPath>'
            f'<g clip-path="url(#cl{idx})"><rect class="shine" style="animation-delay:{idx * 1.6:.1f}s" x="{x - 160}" y="{y - 40}" width="110" height="{h + 80}" '
            f'fill="url(#shine)" transform="skewX(-16)"/></g></g>')
    return out


def certificates(lang, mobile):
    t = CT[lang]
    feats = CERTS['featured']
    lessons = sum(len(c['lessons']) for c in CERTS['collections'])
    w = 600 if mobile else 1200
    if mobile:
        cw, ch, cols, gap, x0, top = 536, 228, 1, 18, 32, 168
    else:
        cw, ch, cols, gap, x0, top = 352, 250, 3, 24, 48, 150
    rows = math.ceil(len(feats) / cols)
    h = top + rows * ch + (rows - 1) * gap + 40
    n = len(feats)
    defs = (linear('bg', [(0, C['night']), (.55, '#170F45'), (1, C['deep'])], x2=1, y2=1)
            + linear('g', [(0, C['amber']), (.5, C['pink']), (1, C['violet'])])
            + linear('shine', [(0, '#fff', 0), (.5, '#fff', .16), (1, '#fff', 0)])
            + radial('au1', C['violet'], .4) + radial('au2', C['amber2'], .28))
    motion = (f'.shine{{animation:shine {n * 1.6:.1f}s ease-in-out infinite}}'
              f'@keyframes shine{{0%{{transform:translateX(0) skewX(-16deg)}}{100 / n * 1.4:.1f}%,100%{{transform:translateX({cw + 320}px) skewX(-16deg)}}}}'
              '.medal{transform-box:fill-box;transform-origin:center;animation:spin 40s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}'
              '.aur{animation:aur 30s ease-in-out infinite}@keyframes aur{50%{transform:translate(-80px,40px)}}')
    b = frame(w, h, 30) + '<g clip-path="url(#frame)">'
    b += f'<g class="aur"><circle cx="{w * .85:.0f}" cy="{h * .1:.0f}" r="{w * .5:.0f}" fill="url(#au1)"/></g><circle cx="{w * .1:.0f}" cy="{h:.0f}" r="{w * .45:.0f}" fill="url(#au2)"/>'
    b += f'<rect width="{w}" height="4" fill="url(#g)"/>'
    b += text(x0, 58, t['kicker'].format(n=n, m=lessons), 17 if mobile else 13, C['amber'], 800, spacing=2.4)
    for i, line in enumerate(wrap(t['lead'], 40) if mobile else [t['lead']]):
        b += text(x0, (100 if mobile else 100) + i * 30, line, 24 if mobile else 26, C['text'], 800)
    for i, c in enumerate(feats):
        r_, c_ = divmod(i, cols)
        b += cert_card(c, x0 + c_ * (cw + gap), top + r_ * (ch + gap), cw, ch, lang, i, mobile)
    b += '</g>'
    desc = '; '.join(f"{c['title']} — {c['issuer']}" + (f", {c['issued']}" if c.get('issued') else '') for c in feats)
    return document(w, h, t['title'], desc, b, defs, motion)


def lessons_panel(lang, mobile):
    t = CT[lang]
    col = CERTS['collections'][0]
    items = col['lessons']
    n = len(items)
    counts = {k: sum(1 for l in items if l['topic'] == k) for k in t['topics']}
    order = sorted(counts, key=lambda k: -counts[k])
    dates = sorted(l['date'] for l in items)
    w, h = (600, 640) if mobile else (1200, 272)
    defs = (linear('bg', [(0, C['ink']), (.6, '#160F42'), (1, C['deep'])], x2=1, y2=1)
            + linear('num', [(0, C['cyan']), (.5, C['lilac']), (1, C['pink'])], x2=1, y2=1)
            + linear('sweep', [(0, '#fff', 0), (.5, '#fff', .5), (1, '#fff', 0)]) + radial('au', C['cyan'], .3))
    x0 = 32 if mobile else 48
    bw = w - 2 * x0 if mobile else 580
    bx = x0 if mobile else w - 48 - bw
    by = 330 if mobile else 92
    motion = (f'.sweep{{animation:sweep 8s ease-in-out infinite}}@keyframes sweep{{0%,10%{{transform:translateX(0)}}60%,100%{{transform:translateX({bw + 200}px)}}}}'
              '.aur{animation:aur 28s ease-in-out infinite}@keyframes aur{50%{transform:translate(60px,-30px)}}')
    b = frame(w, h, 28) + '<g clip-path="url(#frame)">'
    b += f'<g class="aur"><circle cx="{w * .2:.0f}" cy="{h * .5:.0f}" r="{w * .4:.0f}" fill="url(#au)"/></g>'
    b += icon('google', x0, 40, 22, '#fff') + text(x0 + 34, 58, t['lessons_title'].upper(), 15 if mobile else 13, C['cyan'], 800, spacing=2)
    b += text(x0 - 4, 178 if mobile else 172, str(n), 120 if mobile else 112, 'url(#num)', 800)
    sub = wrap(t['lessons_sub'], 30 if mobile else 26)
    for i, line in enumerate(sub):
        b += text(x0 + (0 if mobile else 220), (220 if mobile else 128) + i * 28, line, 21 if mobile else 20, C['text'], 700)
    b += text(x0 + (0 if mobile else 220), (220 if mobile else 128) + len(sub) * 28 + 6,
              t['lessons_date'].format(a=fmt_date(dates[0], lang), b=fmt_date(dates[-1], lang)), 17 if mobile else 15, C['muted'])
    if mobile:
        by = 220 + len(sub) * 28 + 60
    b += f'<clipPath id="bar"><rect x="{bx}" y="{by}" width="{bw}" height="26" rx="13"/></clipPath><g clip-path="url(#bar)">'
    x = bx
    for k in order:
        seg = bw * counts[k] / n
        b += f'<rect x="{x:.1f}" y="{by}" width="{seg + .6:.1f}" height="26" fill="{TOPIC_COLORS[k]}"/>'
        x += seg
    b += f'<rect class="live sweep" x="{bx - 140}" y="{by}" width="140" height="26" fill="url(#sweep)"/></g>'
    for i, k in enumerate(order):
        if mobile:
            lx, ly = bx, by + 64 + i * 40
        else:
            lx, ly = bx + (i % 2) * (bw / 2 + 12), by + 62 + (i // 2) * 38
        cw_ = bw if mobile else bw / 2 - 12
        b += f'<circle cx="{lx + 8}" cy="{ly - 6}" r="8" fill="{TOPIC_COLORS[k]}"/>'
        b += text(lx + 26, ly, f"{t['topics'][k]}", 18 if mobile else 16, C['soft'], 600)
        b += f'<path d="M{lx + 26} {ly + 9}H{lx + cw_}" stroke="#fff" stroke-opacity=".08"/>'
        b += text(lx + cw_, ly, str(counts[k]), 18 if mobile else 16, TOPIC_COLORS[k], 800, anchor='end')
    b += '</g>'
    desc = f"{n} {t['lessons_alt']}: " + ', '.join(f"{t['topics'][k]} {counts[k]}" for k in order)
    return document(w, h, t['lessons_alt'], desc, b, defs, motion)


# ---------------------------------------------------------------- live product scenes
SCENES = {
    'bid': {'device': 'laptop', 'accent': (C['violet'], C['cyan']),
            'screens': [('before-i-deploy', {'en': 'Release checklist', 'bg': 'Списък за публикуване'}),
                        ('bid-mission-control', {'en': 'Mission Control', 'bg': 'Mission Control'}),
                        ('bid-command-palette', {'en': 'Command palette', 'bg': 'Командна палитра'})],
            'title': {'en': 'Before I Deploy — real screens', 'bg': 'Before I Deploy — реални екрани'}},
    'tlr': {'device': 'browser', 'bar': 'The Last Republic', 'accent': (C['pink'], C['violet']),
            'screens': [('tlr/home', {'en': 'Home', 'bg': 'Начало'}),
                        ('tlr/application-path', {'en': 'Application path', 'bg': 'Път до кандидатстване'}),
                        ('tlr/rules-hub', {'en': 'Rules hub', 'bg': 'Правила'}),
                        ('tlr/server-rules', {'en': 'Server rules with search', 'bg': 'Правилник с търсене'}),
                        ('tlr/police-entry', {'en': 'Police Portal entry', 'bg': 'Вход в полицейския портал'})],
            'title': {'en': 'The Last Republic — real screens', 'bg': 'The Last Republic — реални екрани'}},
    'police': {'device': 'tablet', 'bar': 'TLR Police Portal', 'shield': True, 'accent': (C['cyan'], C['mint']),
               'screens': [('police-dashboard', {'en': 'Dashboard', 'bg': 'Табло'}),
                           ('police-employees', {'en': 'Staff directory', 'bg': 'Служители'}),
                           ('police-ranks', {'en': 'Rank hierarchy', 'bg': 'Звания'}),
                           ('police-handbook', {'en': 'Handbook', 'bg': 'Наръчник'})],
               'title': {'en': 'TLR Police Portal — real screens', 'bg': 'TLR Police Portal — реални екрани'}},
}
SCENE_NOTE = {'en': 'Real captures · animated presentation', 'bg': 'Реални кадри · анимирано представяне'}


@lru_cache(maxsize=None)
def screen_data(name):
    """Genuine capture without its presentation caption, as an embedded JPEG."""
    import base64
    import io
    from PIL import Image
    from frame_screens import inner_area
    image = Image.open(ROOT / f'assets/screens/{name}.jpg').convert('RGB')
    crop = image if '/' in name else image.crop(inner_area(image))
    crop = crop.resize((1100, round(crop.height * 1100 / crop.width)), Image.LANCZOS)
    buffer = io.BytesIO()
    crop.save(buffer, 'JPEG', quality=74, optimize=True, progressive=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buffer.getvalue()).decode(), crop.size


MENU = {'en': (['File', 'Edit', 'View', 'Window', 'Help'], 'Mon 5 Oct  9:41'),
        'bg': (['Файл', 'Редакция', 'Изглед', 'Прозорец', 'Помощ'], 'пн 5 окт  9:41')}


def lerp(a, b, t):
    return a + (b - a) * t


def macbook_back(sx, sy, sw, sh, a1, a2, lang):
    """Lid, bezel, wallpaper, menu bar and window chrome of a MacBook Pro.
    Returns (svg, content rect) — the app capture is placed inside the rect."""
    out = ''
    # aluminium lid rim and black glass bezel
    out += (f'<rect x="{sx - 18}" y="{sy - 18}" width="{sw + 36}" height="{sh + 38}" rx="26" fill="url(#lid)"/>'
            f'<rect x="{sx - 18}" y="{sy - 18}" width="{sw + 36}" height="{sh + 38}" rx="26" fill="none" stroke="#9AA0AE" stroke-opacity=".55" stroke-width="1.2"/>'
            f'<rect x="{sx - 15}" y="{sy - 15}" width="{sw + 30}" height="{sh + 32}" rx="23" fill="#040406"/>'
            f'<rect x="{sx - 15}" y="{sy - 15}" width="{sw + 30}" height="{sh + 32}" rx="23" fill="url(#bezel)"/>')
    # desktop wallpaper
    out += (f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="9" fill="url(#wall)"/>'
            f'<g clip-path="url(#screen)"><circle cx="{sx + sw * .18:.0f}" cy="{sy + sh * .95:.0f}" r="{sh * .7:.0f}" fill="url(#w1)"/>'
            f'<circle cx="{sx + sw * .85:.0f}" cy="{sy + sh * .1:.0f}" r="{sh * .65:.0f}" fill="url(#w2)"/>'
            f'<path d="M{sx} {sy + sh * .72:.0f}C{sx + sw * .3:.0f} {sy + sh * .5:.0f} {sx + sw * .6:.0f} {sy + sh * .95:.0f} {sx + sw} {sy + sh * .62:.0f}V{sy + sh}H{sx}Z" fill="#fff" opacity=".05"/>'
            f'<path d="M{sx} {sy + sh * .82:.0f}C{sx + sw * .35:.0f} {sy + sh * .62:.0f} {sx + sw * .7:.0f} {sy + sh:.0f} {sx + sw} {sy + sh * .74:.0f}V{sy + sh}H{sx}Z" fill="#000" opacity=".18"/></g>')
    # menu bar
    items, clock = MENU[lang]
    mb = 24
    out += f'<rect x="{sx}" y="{sy}" width="{sw}" height="{mb}" fill="#0B0A18" fill-opacity=".55"/>'
    out += icon('apple', sx + 14, sy + 5, 14, '#FFFFFF')
    x = sx + 42
    out += text(x, sy + 16.5, 'Before I Deploy', 12.5, '#FFFFFF', 700)
    x += 112
    notch_left = sx + sw / 2 - 54 - 14
    for item in items:
        width = sum(8.2 if '\u0400' <= ch <= '\u04FF' else 7.4 for ch in item)
        if x + width > notch_left:
            break
        out += text(x, sy + 16.5, item, 12.5, '#FFFFFF', 400, extra='fill-opacity=".92"')
        x += width + 18
    rx_ = sx + sw - 14
    out += text(rx_, sy + 16.5, clock, 12.5, '#FFFFFF', 500, anchor='end')
    bx = rx_ - 118
    out += (f'<g transform="translate({bx} {sy + 7})"><rect width="22" height="10.5" rx="3" fill="none" stroke="#fff" stroke-opacity=".9"/>'
            f'<rect x="1.8" y="1.8" width="15" height="6.9" rx="1.6" fill="#fff"/><rect x="23" y="3.4" width="1.6" height="3.8" rx=".8" fill="#fff" opacity=".7"/></g>')
    wx_ = bx - 22
    out += (f'<g transform="translate({wx_} {sy + 18})" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round">'
            '<path d="M-7.5 -7.5a10.6 10.6 0 0 1 15 0"/><path d="M-4.6 -4.6a6.5 6.5 0 0 1 9.2 0"/></g>'
            f'<circle cx="{wx_}" cy="{sy + 16.5}" r="1.6" fill="#fff"/>')
    out += (f'<g transform="translate({wx_ - 34} {sy + 12})" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round">'
            '<circle cx="0" cy="0" r="4.6"/><path d="M3.4 3.4l3.6 3.6"/></g>')
    # app window
    wx, wy = sx + 30, sy + mb + 12
    ww, wh = sw - 60, sh - mb - 12 - 18
    tb = 30
    out += (f'<rect x="{wx}" y="{wy + 10}" width="{ww}" height="{wh}" rx="12" fill="#000" opacity=".55" filter="url(#wshadow)"/>'
            f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="11" fill="#17161D"/>'
            f'<path d="M{wx} {wy + tb}V{wy + 11}Q{wx} {wy} {wx + 11} {wy}H{wx + ww - 11}Q{wx + ww} {wy} {wx + ww} {wy + 11}V{wy + tb}Z" fill="url(#titlebar)"/>'
            f'<path d="M{wx} {wy + tb}H{wx + ww}" stroke="#000" stroke-opacity=".6"/>')
    for i, col in enumerate(('#FF5F57', '#FEBC2E', '#28C840')):
        out += f'<circle cx="{wx + 18 + i * 20}" cy="{wy + tb / 2}" r="6" fill="{col}"/><circle cx="{wx + 18 + i * 20}" cy="{wy + tb / 2}" r="6" fill="none" stroke="#000" stroke-opacity=".18"/>'
    out += text(wx + ww / 2, wy + tb / 2 + 4.5, 'Before I Deploy', 13, '#D8D7E0', 600, anchor='middle')
    return out, (wx, wy + tb, ww, wh - tb)


def macbook_front(sx, sy, sw, sh, a1, a2, w):
    """Window frame highlight, notch, glass, hinge and the keyboard deck in perspective."""
    out = f'<rect x="{sx + 30}" y="{sy + 36}" width="{sw - 60}" height="{sh - 54}" rx="11" fill="none" stroke="#fff" stroke-opacity=".14"/>'
    # notch with camera
    cx, nw, nh = sx + sw / 2, 108, 25
    out += (f'<path d="M{cx - nw / 2 - 6} {sy - 1}Q{cx - nw / 2} {sy - 1} {cx - nw / 2} {sy + 5}V{sy + nh - 9}Q{cx - nw / 2} {sy + nh} {cx - nw / 2 + 9} {sy + nh}'
            f'H{cx + nw / 2 - 9}Q{cx + nw / 2} {sy + nh} {cx + nw / 2} {sy + nh - 9}V{sy + 5}Q{cx + nw / 2} {sy - 1} {cx + nw / 2 + 6} {sy - 1}Z" fill="#040406"/>'
            f'<circle cx="{cx}" cy="{sy + 11}" r="4.2" fill="#0B0D16" stroke="#1E2336" stroke-width="1"/>'
            f'<circle cx="{cx}" cy="{sy + 11}" r="2" fill="#1C2850"/><circle cx="{cx - .8}" cy="{sy + 10.2}" r=".7" fill="#fff" opacity=".55"/>'
            f'<circle cx="{cx + 14}" cy="{sy + 11}" r="1.2" fill="#14161F"/>')
    # glass reflection
    out += (f'<path d="M{sx} {sy}H{sx + sw * .46:.0f}L{sx + sw * .2:.0f} {sy + sh}H{sx}Z" fill="url(#glass)" clip-path="url(#screen)"/>')
    hinge = sy + sh + 20
    # hinge
    out += (f'<rect x="{sx - 4}" y="{hinge - 1}" width="{sw + 8}" height="10" rx="3" fill="url(#hinge)"/>')
    # deck (trapezoid, back edge under the hinge)
    by, fy = hinge + 9, hinge + 98
    bl, br = sx - 18, sx + sw + 18
    fl, fr = 72, w - 72
    out += (f'<path d="M{bl} {by}H{br}L{fr} {fy}H{fl}Z" fill="url(#deck)"/>'
            f'<path d="M{bl} {by}H{br}L{fr} {fy}H{fl}Z" fill="url(#spill)"/>'
            f'<path d="M{fl} {fy}H{fr}" stroke="#C9CDD8" stroke-opacity=".55" stroke-width="1.2"/>')

    def at(t_y, t_x):
        """Point on the deck: t_y 0 = back, 1 = front; t_x 0 = left, 1 = right."""
        y = lerp(by, fy, t_y)
        left, right = lerp(bl, fl, t_y), lerp(br, fr, t_y)
        return lerp(left, right, t_x), y

    def quad(t0, t1, x0, x1, fill, extra=''):
        pts = [at(t0, x0), at(t0, x1), at(t1, x1), at(t1, x0)]
        d = 'M' + 'L'.join(f'{px:.1f} {py:.1f}' for px, py in pts) + 'Z'
        return f'<path d="{d}" fill="{fill}" {extra}/>'

    # keyboard well
    kx0, kx1, ky0, ky1 = .155, .845, .07, .58
    out += quad(ky0, ky1, kx0, kx1, '#0D0E12', 'stroke="#000" stroke-opacity=".6"')
    rows = [(.10, 14, 'fn'), (.12, 14, ''), (.12, 14, ''), (.12, 13, ''), (.12, 12, ''), (.135, 0, 'space')]
    t = ky0 + .012
    span = (ky1 - ky0 - .024)
    total = sum(r[0] for r in rows)
    for frac, count, kind in rows:
        th = span * frac / total
        t0, t1 = t + th * .1, t + th * .92
        if kind == 'space':
            keys = [(0, .07), (.075, .145), (.15, .22), (.225, .33), (.335, .665), (.67, .775), (.78, .85), (.855, .925), (.93, 1)]
        else:
            gap = .006
            keys = [(i / count + gap / 2, (i + 1) / count - gap / 2) for i in range(count)]
        for i, (k0, k1) in enumerate(keys):
            x0 = kx0 + .006 + (kx1 - kx0 - .012) * k0
            x1 = kx0 + .006 + (kx1 - kx0 - .012) * k1
            fill = '#1E1F26' if not (kind == 'fn' and i == count - 1) else '#25262E'
            out += quad(t0, t1, x0, x1, fill, 'stroke="#3A3C46" stroke-opacity=".35" stroke-width=".6"')
        t += th
    # speaker grilles
    for side in ((.035, .135), (.865, .965)):
        for r_ in range(6):
            ty = ky0 + .03 + r_ * (ky1 - ky0 - .06) / 5
            for c_ in range(9):
                px, py = at(ty, lerp(side[0], side[1], c_ / 8))
                out += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{lerp(.7, 1.05, ty):.2f}" fill="#0F1014" opacity=".85"/>'
    # trackpad
    out += quad(.64, .965, .335, .665, 'url(#pad)', 'stroke="#1E2027" stroke-opacity=".7" stroke-width=".8"')
    # front lip with thumb scoop and shadow
    out += (f'<path d="M{fl} {fy}H{fr}Q{fr + 4} {fy + 2} {fr - 6} {fy + 11}H{fl + 6}Q{fl - 4} {fy + 2} {fl} {fy}Z" fill="url(#lip)"/>'
            f'<path d="M{w / 2 - 70} {fy + .5}Q{w / 2} {fy + 9} {w / 2 + 70} {fy + .5}Z" fill="#15161B" opacity=".75"/>')
    return out, fy + 11


IPAD = {'en': 'Mon 5 Oct', 'bg': 'пн 5 окт'}


@lru_cache(maxsize=None)
def page_color(name):
    """Average colour of the capture's last rows, used to extend short pages."""
    from PIL import Image
    from frame_screens import inner_area
    image = Image.open(ROOT / f'assets/screens/{name}.jpg').convert('RGB')
    crop = image if '/' in name else image.crop(inner_area(image))
    strip = crop.crop((0, crop.height - 40, max(4, crop.width // 60), crop.height)).resize((1, 1), Image.LANCZOS)
    return '#%02X%02X%02X' % strip.getpixel((0, 0))


def ipad_back(sx, sy, sw, sh, cfg, lang):
    """iPad Pro in landscape: aluminium frame, buttons, Apple Pencil, bezel, status bar and Safari.
    Returns (svg, content rect)."""
    out = ''
    # Apple Pencil attached to the magnetic top edge
    px0, px1, py = sx + sw * .42, sx + sw * .86, sy - 31
    out += (f'<path d="M{px0} {py}H{px1 - 26}L{px1} {py + 5.5}L{px1 - 26} {py + 11}H{px0}Q{px0 - 6} {py + 11} {px0 - 6} {py + 5.5}Q{px0 - 6} {py} {px0} {py}Z" fill="url(#pencil)"/>'
            f'<path d="M{px1 - 26} {py}L{px1} {py + 5.5}L{px1 - 26} {py + 11}Z" fill="#D9DCE3"/>'
            f'<path d="M{px1 - 6} {py + 3.7}L{px1} {py + 5.5}L{px1 - 6} {py + 7.3}Z" fill="#3A3D46"/>'
            f'<path d="M{px0 + 30} {py + 11}H{px1 - 70}" stroke="#AEB3BE" stroke-width="1"/>')
    # buttons: top button and volume rocker
    out += (f'<rect x="{sx + 50}" y="{sy - 25}" width="62" height="6" rx="3" fill="url(#btn)"/>'
            f'<rect x="{sx + sw + 18}" y="{sy + 40}" width="6" height="46" rx="3" fill="url(#btnv)"/>'
            f'<rect x="{sx + sw + 18}" y="{sy + 96}" width="6" height="46" rx="3" fill="url(#btnv)"/>')
    # aluminium frame, chamfer highlight and black bezel
    out += (f'<rect x="{sx - 22}" y="{sy - 22}" width="{sw + 44}" height="{sh + 44}" rx="46" fill="url(#alu)"/>'
            f'<rect x="{sx - 22}" y="{sy - 22}" width="{sw + 44}" height="{sh + 44}" rx="46" fill="none" stroke="#E3E6EE" stroke-opacity=".7" stroke-width="1.2"/>'
            f'<rect x="{sx - 19.5}" y="{sy - 19.5}" width="{sw + 39}" height="{sh + 39}" rx="43.5" fill="#030305"/>'
            f'<rect x="{sx - 19.5}" y="{sy - 19.5}" width="{sw + 39}" height="{sh + 39}" rx="43.5" fill="url(#bezel)"/>')
    # front camera on the landscape edge
    cx = sx + sw / 2
    out += (f'<circle cx="{cx}" cy="{sy - 10}" r="3.6" fill="#0B0D16" stroke="#1E2336"/>'
            f'<circle cx="{cx}" cy="{sy - 10}" r="1.6" fill="#1C2850"/><circle cx="{cx - .7}" cy="{sy - 10.7}" r=".6" fill="#fff" opacity=".5"/>')
    # display
    out += f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="26" fill="#0A0B12"/>'
    # status bar
    sb, tb = 26, 48
    status = ''
    status += text(sx + 30, sy + 18, '9:41', 14, '#FFFFFF', 700)
    status += text(sx + 70, sy + 18, IPAD[lang], 14, '#FFFFFF', 600)
    rx_ = sx + sw - 30
    status += (f'<g transform="translate({rx_ - 26} {sy + 8})"><rect width="24" height="11.5" rx="3.4" fill="none" stroke="#fff" stroke-opacity=".9"/>'
               f'<rect x="2" y="2" width="20" height="7.5" rx="1.8" fill="#fff"/><rect x="25" y="3.8" width="1.8" height="4" rx=".9" fill="#fff" opacity=".7"/></g>')
    status += text(rx_ - 32, sy + 18, '100%', 13.5, '#FFFFFF', 600, anchor='end')
    wx_ = rx_ - 86
    status += (f'<g transform="translate({wx_} {sy + 19})" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round">'
               '<path d="M-8 -8a11.3 11.3 0 0 1 16 0"/><path d="M-4.9 -4.9a6.9 6.9 0 0 1 9.8 0"/></g>'
               f'<circle cx="{wx_}" cy="{sy + 17.2}" r="1.7" fill="#fff"/>')
    out += f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sb + tb}" fill="#16161C" clip-path="url(#screen)"/>' + status
    # Safari toolbar
    ty = sy + sb
    icons = '#4F8DF7'
    out += (f'<g fill="none" stroke="{icons}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="{sx + 26}" y="{ty + 15}" width="22" height="18" rx="4"/><path d="M{sx + 34} {ty + 15}v18"/>'
            f'<path d="M{sx + 76} {ty + 16}l-8 8 8 8"/><path d="M{sx + 100} {ty + 16}l8 8-8 8" stroke-opacity=".35"/>'
            f'<path d="M{sx + sw - 132} {ty + 21}v-8m-5 5l5-5 5 5M{sx + sw - 140} {ty + 19}v13h16v-13"/>'
            f'<path d="M{sx + sw - 86} {ty + 24}h16m-8-8v16"/>'
            f'<rect x="{sx + sw - 48}" y="{ty + 18}" width="14" height="14" rx="3"/><path d="M{sx + sw - 44} {ty + 14}h10a4 4 0 0 1 4 4v10"/></g>')
    pw = 420
    px = sx + sw / 2 - pw / 2
    out += f'<rect x="{px}" y="{ty + 9}" width="{pw}" height="31" rx="11" fill="#2A2A33"/>'
    out += text(px + 16, ty + 29.5, 'aA', 14, '#D7D7DE', 600)
    out += shield(sx + sw / 2 - 74, ty + 25, C['mint'])
    out += text(sx + sw / 2 + 10, ty + 30, cfg['bar'], 15, '#F2F2F6', 600, anchor='middle')
    out += (f'<path d="M{px + pw - 22} {ty + 20}a6.5 6.5 0 1 0 1.8 4.6M{px + pw - 22} {ty + 16}v4.5h-4.5" fill="none" stroke="#D7D7DE" stroke-width="1.7" stroke-linecap="round"/>')
    out += f'<path d="M{sx} {ty + tb}H{sx + sw}" stroke="#000" stroke-opacity=".7"/>'
    return out, (sx, ty + tb, sw, sh - sb - tb)


def ipad_front(sx, sy, sw, sh):
    out = (f'<rect x="{sx + sw / 2 - 80}" y="{sy + sh - 11}" width="160" height="5" rx="2.5" fill="#fff" opacity=".85"/>'
           f'<path d="M{sx} {sy}H{sx + sw * .44:.0f}L{sx + sw * .18:.0f} {sy + sh}H{sx}Z" fill="url(#glass)" clip-path="url(#screen)"/>')
    return out


def scene(key, lang):
    cfg = SCENES[key]
    a1, a2 = cfg['accent']
    screens = cfg['screens']
    n = len(screens)
    seg = 4.6
    period = n * seg
    laptop = cfg['device'] == 'laptop'
    tablet = cfg['device'] == 'tablet'
    w, h = (1200, 900) if laptop else (1200, 880) if tablet else (1200, 800)
    if laptop:
        sx, sy, sw, sh = 150, 58, 900, 563
    elif tablet:
        sx, sy, sw, sh = 140, 82, 920, 660
    else:
        sx, sy, sw, sh = 90, 108, 1020, 566
    defs = (linear('bg', [(0, C['night']), (.55, '#150F40'), (1, C['deep'])], x2=1, y2=1)
            + radial('g1', a1, .55) + radial('g2', a2, .4)
            + linear('sheen', [(0, '#fff', 0), (.5, '#fff', .07), (1, '#fff', 0)])
            + linear('fade', [(0, '#000', 0), (1, '#000', .35)], x2=0, y2=1)
            + f'<clipPath id="screen"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="{9 if laptop else 26 if tablet else 0}"/></clipPath>')
    if laptop:
        defs += (linear('lid', [(0, '#5E636F'), (.5, '#2E3139'), (1, '#4A4E59')], x2=0, y2=1)
                 + linear('bezel', [(0, '#16171D', .9), (.5, '#000', 0), (1, '#0E0F14', .9)], x2=1, y2=1)
                 + linear('wall', [(0, '#1B1250'), (.45, '#4C1D95'), (.75, '#0E3A5C'), (1, '#071B2B')], x2=1, y2=1)
                 + radial('w1', a1, .65) + radial('w2', a2, .45)
                 + linear('titlebar', [(0, '#302F38'), (1, '#24232B')], x2=0, y2=1)
                 + linear('glass', [(0, '#fff', .07), (1, '#fff', 0)], x2=1, y2=1)
                 + linear('hinge', [(0, '#08090C'), (.6, '#2B2E36'), (1, '#121318')], x2=0, y2=1)
                 + linear('deck', [(0, '#2B2E36'), (.35, '#3E424C'), (1, '#6A6F7C')], x2=0, y2=1)
                 + linear('spill', [(0, a1, .22), (.5, a1, .05), (1, a1, 0)], x2=0, y2=1)
                 + linear('pad', [(0, '#3A3D47'), (1, '#5D616D')], x2=0, y2=1)
                 + linear('lip', [(0, '#8C919E'), (.3, '#3C3F48'), (1, '#18191E')], x2=0, y2=1)
                 + '<radialGradient id="shadow"><stop offset="0" stop-color="#000" stop-opacity=".7"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'
                 + '<filter id="wshadow" x="-10%" y="-10%" width="120%" height="130%"><feGaussianBlur stdDeviation="12"/></filter>')
    elif tablet:
        defs += (linear('alu', [(0, '#A9AEB9'), (.08, '#6E737E'), (.5, '#4A4E58'), (.92, '#6E737E'), (1, '#B7BCC6')], x2=0, y2=1)
                 + linear('bezel', [(0, '#16171D', .9), (.5, '#000', 0), (1, '#0E0F14', .9)], x2=1, y2=1)
                 + linear('glass', [(0, '#fff', .07), (1, '#fff', 0)], x2=1, y2=1)
                 + linear('pencil', [(0, '#FFFFFF'), (.6, '#E6E8EE'), (1, '#B9BDC7')], x2=0, y2=1)
                 + linear('btn', [(0, '#C9CDD6'), (1, '#5E636E')], x2=0, y2=1)
                 + linear('btnv', [(0, '#5E636E'), (1, '#C9CDD6')])
                 + '<radialGradient id="shadow"><stop offset="0" stop-color="#000" stop-opacity=".7"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>')
    else:
        defs += linear('metal', [(0, '#3A3F55'), (.5, '#8E93A8'), (1, '#2A2E40')])
    css = ''
    motion = ('.g1{animation:drift 26s ease-in-out infinite}.g2{animation:drift 34s ease-in-out infinite reverse}'
              '@keyframes drift{50%{transform:translate(-50px,30px)}}'
              f'.sheen{{animation:sheen 9s ease-in-out infinite}}@keyframes sheen{{0%,25%{{transform:translateX(-400px)}}75%,100%{{transform:translateX({sw + 400}px)}}}}')
    # Screens dip through black instead of cross-fading, so two captures never overlap.
    fade = 0.38 / period * 100
    for i in range(n):
        start, end = i / n * 100, (i + 1) / n * 100
        css += f'.s{i}{{opacity:{1 if i == 0 else 0}}}.d{i}{{opacity:{1 if i == 0 else .3}}}.l{i}{{opacity:{1 if i == 0 else 0}}}'
        frames = (f'0%{{opacity:0}}{start:.2f}%{{opacity:0}}{start + fade:.2f}%{{opacity:1}}{end - fade:.2f}%{{opacity:1}}'
                  f'{end:.2f}%{{opacity:0}}100%{{opacity:0}}')
        dots = (f'0%{{opacity:.3}}{start:.2f}%{{opacity:.3}}{start + fade:.2f}%{{opacity:1}}{end - fade:.2f}%{{opacity:1}}'
                f'{end:.2f}%{{opacity:.3}}100%{{opacity:.3}}')
        motion += (f'.s{i},.l{i}{{animation:show{i} {period:.1f}s linear infinite}}@keyframes show{i}{{{frames}}}'
                   f'.d{i}{{animation:dot{i} {period:.1f}s linear infinite}}@keyframes dot{i}{{{dots}}}')
    b = f'<rect width="{w}" height="{h}" rx="30" fill="url(#bg)"/>'
    b += (f'<clipPath id="frame"><rect width="{w}" height="{h}" rx="30"/></clipPath><g clip-path="url(#frame)">'
          f'<g class="g1"><circle cx="{w * .22:.0f}" cy="{h * .3:.0f}" r="420" fill="url(#g1)"/></g>'
          f'<g class="g2"><circle cx="{w * .82:.0f}" cy="{h * .75:.0f}" r="380" fill="url(#g2)"/></g>'
          + stars(w, h, 50, 21) + '</g>')
    if laptop:
        b += f'<ellipse cx="{w / 2}" cy="{sy + sh + 132}" rx="600" ry="26" fill="url(#shadow)"/>'
        chrome, (cx_, cy_, cw_, ch_) = macbook_back(sx, sy, sw, sh, a1, a2, lang)
        b += chrome
        b += (f'<clipPath id="content"><path d="M{cx_} {cy_}H{cx_ + cw_}V{cy_ + ch_ - 11}Q{cx_ + cw_} {cy_ + ch_} {cx_ + cw_ - 11} {cy_ + ch_}'
              f'H{cx_ + 11}Q{cx_} {cy_ + ch_} {cx_} {cy_ + ch_ - 11}Z"/></clipPath>')
        b += f'<rect x="{cx_}" y="{cy_}" width="{cw_}" height="{ch_}" fill="#121116"/><g clip-path="url(#content)">'
    elif tablet:
        b += f'<ellipse cx="{w / 2}" cy="{sy + sh + 46}" rx="560" ry="22" fill="url(#shadow)"/>'
        chrome, (cx_, cy_, cw_, ch_) = ipad_back(sx, sy, sw, sh, cfg, lang)
        b += chrome
        b += (f'<clipPath id="content"><path d="M{cx_} {cy_}H{cx_ + cw_}V{cy_ + ch_ - 26}Q{cx_ + cw_} {cy_ + ch_} {cx_ + cw_ - 26} {cy_ + ch_}'
              f'H{cx_ + 26}Q{cx_} {cy_ + ch_} {cx_} {cy_ + ch_ - 26}Z"/></clipPath>')
        b += f'<rect x="{cx_}" y="{cy_}" width="{cw_}" height="{ch_}" fill="#0A0B12"/><g clip-path="url(#content)">'
    else:
        b += (f'<ellipse cx="{w / 2}" cy="{sy + sh + 40}" rx="540" ry="22" fill="#000" opacity=".45"/>'
              f'<rect x="{sx - 2}" y="{sy - 46}" width="{sw + 4}" height="{sh + 48}" rx="18" fill="#0B0D18" stroke="#33395A" stroke-width="2"/>'
              f'<circle cx="{sx + 24}" cy="{sy - 23}" r="6.5" fill="#FF5F57"/><circle cx="{sx + 46}" cy="{sy - 23}" r="6.5" fill="#FEBC2E"/>'
              f'<circle cx="{sx + 68}" cy="{sy - 23}" r="6.5" fill="#28C840"/>'
              f'<rect x="{w / 2 - 210}" y="{sy - 37}" width="420" height="28" rx="14" fill="#161A2C"/>')
        if cfg.get('shield'):
            b += shield(w / 2 - 186, sy - 22, C['mint'])
        b += text(w / 2 + 6, sy - 17, cfg['bar'], 15, C['soft'], 600, anchor='middle')
        cx_, cy_, cw_, ch_ = sx, sy, sw, sh
        b += f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="#05060C"/><g clip-path="url(#screen)">'
    for i, (name, _labels) in enumerate(screens):
        href, (iw, ih) = screen_data(name)
        dh = ih * cw_ / iw
        overflow = max(0, dh - ch_)
        scroll = (f'.sc{i}{{animation:scroll{i} {period:.1f}s ease-in-out infinite}}@keyframes scroll{i}{{0%,{i / n * 100 + 8:.1f}%{{transform:translateY(0)}}'
                  f'{(i + 1) / n * 100 - 4:.1f}%,100%{{transform:translateY(-{overflow:.0f}px)}}}}') if overflow > 12 else ''
        motion += scroll
        page, tail = '', ''
        if tablet and dh < ch_:
            col = page_color(name)
            defs += linear(f'pf{i}', [(0, col, 0), (1, col, 1)], x2=0, y2=1)
            page = f'<rect x="{cx_}" y="{cy_}" width="{cw_}" height="{ch_}" fill="{col}"/>'
            tail = f'<rect x="{cx_}" y="{cy_ + dh - 90:.0f}" width="{cw_}" height="91" fill="url(#pf{i})"/>'
        b += (f'<g class="s{i}">{page}<g class="sc{i}"><image href="{href}" x="{cx_}" y="{cy_}" width="{cw_}" height="{dh:.0f}" preserveAspectRatio="xMidYMin meet"/></g>{tail}</g>')
    if laptop:
        b += f'<rect x="{cx_}" y="{cy_ + ch_ - 70}" width="{cw_}" height="70" fill="url(#fade)"/></g>'
        b += f'<g class="live" clip-path="url(#screen)"><rect class="sheen" x="{sx - 200}" y="{sy}" width="220" height="{sh}" fill="url(#sheen)" transform="skewX(-14)"/></g>'
        front, _bottom = macbook_front(sx, sy, sw, sh, a1, a2, w)
        b += front
    elif tablet:
        b += '</g>'
        b += f'<g class="live" clip-path="url(#screen)"><rect class="sheen" x="{sx - 200}" y="{sy}" width="220" height="{sh}" fill="url(#sheen)" transform="skewX(-14)"/></g>'
        b += ipad_front(sx, sy, sw, sh)
    else:
        b += f'<rect x="{sx}" y="{sy + sh - 120}" width="{sw}" height="120" fill="url(#fade)"/>'
        b += f'<g class="live"><rect class="sheen" x="{sx - 200}" y="{sy}" width="220" height="{sh}" fill="url(#sheen)" transform="skewX(-14)"/></g></g>'
    # caption: current screen + progress dots
    cy = h - 46
    for i, (_name, labels) in enumerate(screens):
        b += f'<g class="l{i}">' + text(w / 2, cy - 22, labels[lang], 24, C['text'], 700, anchor='middle') + '</g>'
    total = n * 30
    for i in range(n):
        b += f'<rect class="d{i}" x="{w / 2 - total / 2 + i * 30}" y="{cy}" width="22" height="5" rx="2.5" fill="{a2 if i else a1}"/>'
    b += text(w - 34, h - 22, SCENE_NOTE[lang], 13, C['muted'], anchor='end')
    labels = ', '.join(l[lang] for _n, l in screens)
    desc = f"{cfg['title'][lang]}: {labels}. " + ('Genuine captures presented as an animated sequence; identities are redacted.' if lang == 'en'
                                                  else 'Истински кадри, показани като анимирана последователност; личните данни са скрити.')
    return document(w, h, cfg['title'][lang], desc, b, defs, motion, css)


# ---------------------------------------------------------------- under the hood (Before I Deploy metrics)
BIDM = json.loads((ROOT / 'data/bid-metrics.json').read_text())
UH = {'en': {'kicker': 'UNDER THE HOOD · BEFORE I DEPLOY · MEASURED {d}', 'stream': 'engine → app · NDJSON',
             'stream_note': 'real event format, illustrative values', 'overall': '→ overall: warnings · 1 warn', 'code': 'Code composition', 'title': 'Before I Deploy under the hood'},
      'bg': {'kicker': 'ПОД КАПАКА · BEFORE I DEPLOY · ИЗМЕРЕНО {d}', 'stream': 'engine → приложение · NDJSON',
             'stream_note': 'реален формат на събитията, примерни стойности', 'overall': '→ общо: warnings · 1 предупреждение', 'code': 'Състав на кода', 'title': 'Before I Deploy под капака'}}


def json_line(line, x, y, size):
    """Colour a single NDJSON line: keys lilac, strings mint, literals amber, punctuation muted."""
    import re as _re
    out, cx = '', x
    char_w = size * .6
    for tok in _re.findall(r'"[^"]*"(?=:)|"[^"]*"|true|false|[{}\[\]:,]|[^"{}\[\]:,]+', line):
        if tok.endswith('"') and line[line.find(tok) + len(tok):line.find(tok) + len(tok) + 1] == ':' and tok.startswith('"'):
            col = C['lilac2']
        elif tok.startswith('"'):
            col = C['mint2']
        elif tok in ('true', 'false') or tok.startswith('…'):
            col = C['amber']
        else:
            col = C['muted']
        out += f'<tspan x="{cx:.1f}" fill="{col}">{esc(tok)}</tspan>'
        cx += len(tok) * char_w
    return f'<text y="{y}" font-size="{size}" class="mono">{out}</text>'


def under_hood(lang, mobile):
    t = UH[lang]
    stats, comp, events = BIDM['stats'], BIDM['composition'], BIDM['events']
    y_, m_, d_ = BIDM['measured'].split('-')
    measured = f"{int(d_)} {MONTHS[lang][int(m_) - 1]} {y_}".upper()
    w = 600 if mobile else 1200
    x0 = 32 if mobile else 48
    if mobile:
        tile_w, tile_h, cols = 260, 128, 2
        grid_x, grid_y = x0, 96
        term_x, term_y, term_w = x0, grid_y + 4 * (tile_h + 16) + 10, w - 2 * x0
        lines_shown = events
        term_h = 70 + len(lines_shown) * 30
        bar_y = term_y + term_h + 70
        h = bar_y + 190
    else:
        tile_w, tile_h, cols = 290, 120, 2
        grid_x, grid_y = x0, 100
        term_x, term_y, term_w = 680, 100, 472
        lines_shown = events
        term_h = 4 * (tile_h + 16) - 16
        bar_y = grid_y + 4 * (tile_h + 16) + 50
        h = bar_y + 120
    n_ev = len(lines_shown)
    period = n_ev * 1.1 + 3
    defs = (linear('bg', [(0, C['night']), (.55, '#150F40'), (1, C['deep'])], x2=1, y2=1)
            + linear('num', [(0, '#FFFFFF'), (.6, C['lilac2']), (1, C['cyan'])], x2=1, y2=1)
            + linear('top', [(0, C['violet']), (.5, C['cyan']), (1, C['mint'])])
            + radial('au1', C['violet'], .4) + radial('au2', C['cyan'], .3)
            + linear('sweep', [(0, '#fff', 0), (.5, '#fff', .5), (1, '#fff', 0)]))
    css = ''.join(f'.e{i}{{opacity:1}}' for i in range(n_ev))
    motion = ('.aur{animation:aur 30s ease-in-out infinite}@keyframes aur{50%{transform:translate(-70px,30px)}}'
              f'.sweep{{animation:sweep 9s ease-in-out infinite}}@keyframes sweep{{0%,15%{{transform:translateX(0)}}60%,100%{{transform:translateX({w}px)}}}}'
              '.cur{animation:cur 1.1s steps(1) infinite}@keyframes cur{50%{opacity:0}}')
    for i in range(n_ev):
        on = (i * 1.1) / period * 100
        motion += (f'.e{i}{{animation:ev{i} {period:.1f}s linear infinite}}'
                   f'@keyframes ev{i}{{0%,{max(on - .1, 0):.2f}%{{opacity:0}}{on + 2:.2f}%,94%{{opacity:1}}100%{{opacity:0}}}}')
    b = frame(w, h, 30) + '<g clip-path="url(#frame)">'
    b += f'<g class="aur"><circle cx="{w * .85:.0f}" cy="{h * .15:.0f}" r="{w * .5:.0f}" fill="url(#au1)"/></g><circle cx="{w * .1:.0f}" cy="{h:.0f}" r="{w * .45:.0f}" fill="url(#au2)"/>'
    b += f'<rect width="{w}" height="4" fill="url(#top)"/>'
    kick = t['kicker'].format(d=measured)
    for i, line in enumerate(wrap(kick, 34) if mobile else [kick]):
        b += text(x0, 56 + i * 24, line, 16 if mobile else 13, C['cyan'], 800, spacing=2.2)
    # stat tiles
    for i, st in enumerate(stats):
        r_, c_ = divmod(i, cols)
        tx = grid_x + c_ * (tile_w + 16)
        ty = grid_y + r_ * (tile_h + 16) + (24 if mobile else 0)
        b += (f'<rect x="{tx}" y="{ty}" width="{tile_w}" height="{tile_h}" rx="20" fill="#0E0B2C" fill-opacity=".72" stroke="#fff" stroke-opacity=".1"/>'
              f'<rect x="{tx + 18}" y="{ty}" width="{tile_w - 36}" height="2" fill="url(#top)" opacity=".7"/>')
        b += display(st['value'], tx + 20, ty + (66 if not mobile else 70), 44 if not mobile else 46, 'url(#num)', weight=800)
        b += text(tx + 20, ty + tile_h - 22, st[lang], 15 if not mobile else 18, C['soft'], 600)
    if mobile:
        term_y += 24
        bar_y += 24
        h += 24
    # terminal with the event stream
    b += (f'<rect x="{term_x}" y="{term_y}" width="{term_w}" height="{term_h}" rx="18" fill="#05060F" fill-opacity=".9" stroke="{C["line"]}"/>'
          f'<circle cx="{term_x + 22}" cy="{term_y + 22}" r="6" fill="#FF5F57"/><circle cx="{term_x + 42}" cy="{term_y + 22}" r="6" fill="#FEBC2E"/>'
          f'<circle cx="{term_x + 62}" cy="{term_y + 22}" r="6" fill="#28C840"/>')
    b += text(term_x + term_w - 18, term_y + 27, t['stream'], 13 if not mobile else 15, C['muted'], 700, anchor='end', mono=True)
    size = 13.2 if not mobile else 15.2
    gap = 40 if not mobile else 30
    top = term_y + (100 if not mobile else 66)
    if not mobile:
        b += text(term_x + 20, term_y + 64, '$ bid check', 14, C['text'], 700, mono=True)
    for i, line in enumerate(lines_shown):
        b += f'<g class="e{i}">' + json_line(line, term_x + 20, top + i * gap, size) + '</g>'
    if not mobile:
        b += f'<g class="e{n_ev - 1}">' + text(term_x + 20, top + n_ev * gap + 4, t['overall'], 14, C['amber'], 700, mono=True) + '</g>'
    b += f'<rect class="live cur" x="{term_x + 20}" y="{term_y + term_h - 26}" width="9" height="16" fill="{C["mint"]}"/>'
    b += text(term_x + term_w - 18, term_y + term_h - 12, t['stream_note'], 11 if not mobile else 13, C['muted'], anchor='end')
    # code composition bar
    total = sum(c['lines'] for c in comp)
    b += text(x0, bar_y - 16, t['code'], 16 if not mobile else 19, C['text'], 700)
    bw = w - 2 * x0
    b += f'<clipPath id="cbar"><rect x="{x0}" y="{bar_y}" width="{bw}" height="20" rx="10"/></clipPath><g clip-path="url(#cbar)">'
    x = x0
    for c in comp:
        seg = bw * c['lines'] / total
        b += f'<rect x="{x:.1f}" y="{bar_y}" width="{seg + .5:.1f}" height="20" fill="{c["color"]}"/>'
        x += seg
    b += f'<rect class="live sweep" x="{x0 - 140}" y="{bar_y}" width="140" height="20" fill="url(#sweep)"/></g>'
    lx, ly = x0, bar_y + 50
    for i, c in enumerate(comp):
        label = f"{c['name']} {c['lines'] / 1000:.1f}k"
        if mobile:
            lx, ly = x0 + (i % 2) * 270, bar_y + 48 + (i // 2) * 34
        b += f'<circle cx="{lx + 7}" cy="{ly - 5}" r="7" fill="{c["color"]}"/>' + text(lx + 22, ly, label, 15 if not mobile else 17, C['soft'], 600)
        if not mobile:
            lx += len(label) * 8.4 + 54
    b += '</g>'
    desc = '; '.join(f"{st['value']} {st[lang]}" for st in stats) + '. ' + ', '.join(f"{c['name']} {c['lines']}" for c in comp)
    return document(w, h, t['title'], desc, b, defs, motion, css)


# ---------------------------------------------------------------- whitelist flow (The Last Republic)
WF = {
    'en': {'kicker': 'WHITELIST FLOW · ARCHITECTURE',
           'top': [('Applicant', 'Discord sign-in'), ('Whitelist exam', '2 h · 3 attempts'), ('Postgres', 'application saved'),
                   ('Discord bot', 'always-on Gateway'), ('Staff', 'accept / reject + reason')],
           'bottom': [('Signed relay', 'HMAC-SHA256 + time'), ('Next.js site', 'applies the decision'), ('Applicant', 'channel post + DM')],
           'gate': ['Police Portal gate: a fresh Discord member lookup on every request,', 'matched by role ID only, never by name. Any error denies access.'],
           'title': 'The Last Republic whitelist flow',
           'desc': 'Illustration of the implemented flow: the applicant signs in with Discord and takes a two-hour exam with three attempts per account; the application is saved in Postgres; an always-on Discord bot posts it with accept and reject buttons; staff decide with a mandatory reason; the bot relays the decision to the site with an HMAC-SHA256 signature and timestamp; the site applies it and the applicant gets a channel post and a direct message. The Police Portal checks Discord role IDs server-side on every request and fails closed.'},
    'bg': {'kicker': 'ПЪТ НА КАНДИДАТУРАТА · АРХИТЕКТУРА',
           'top': [('Кандидат', 'вход с Discord'), ('Whitelist изпит', '2 часа · 3 опита'), ('Postgres', 'записана кандидатура'),
                   ('Discord бот', 'постоянен Gateway'), ('Екип', 'решение + причина')],
           'bottom': [('Подписан relay', 'HMAC-SHA256 + час'), ('Next.js сайт', 'прилага решението'), ('Кандидат', 'канал + лично съобщение')],
           'gate': ['Полицейски портал: нова проверка в Discord при всяка заявка,', 'само по ID на ролята, никога по име. Всяка грешка отказва достъпа.'],
           'title': 'Път на кандидатурата в The Last Republic',
           'desc': 'Илюстрация на реализирания поток: кандидатът влиза с Discord и решава двучасов изпит с три опита на акаунт; кандидатурата се записва в Postgres; постоянно свързан Discord бот я публикува с бутони за приемане и отказ; екипът решава със задължителна причина; ботът препраща решението към сайта с HMAC-SHA256 подпис и час; сайтът го прилага, а кандидатът получава публикация и лично съобщение. Полицейският портал проверява ID на ролите в Discord на сървъра при всяка заявка и отказва при грешка.'},
}


def packet_svg(path, period):
    return (f'<g class="live"><g><circle r="18" fill="{C["pink"]}" opacity=".3"/><circle r="7" fill="#FFF0F7"/>'
            f'<animateMotion dur="{period}s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;.85;1" calcMode="linear" path="{path}"/></g></g>')


def arch_whitelist(lang, mobile):
    t = WF[lang]
    period = 14.0
    steps = t['top'] + t['bottom']
    cols = [C['lilac'], C['pink'], '#4F7BFF', '#7C8BFF', C['amber'], C['mint'], C['cyan'], C['lilac2']]
    if mobile:
        w, h = 600, 1220
        defs, b = arch_frame(w, h, t['kicker'], C['pink'])
        ys = [86 + i * 104 for i in range(8)]
        path = f'M300 {ys[0] + 40}V{ys[-1] + 40}'
        for i, ((title, sub), col) in enumerate(zip(steps, cols)):
            b += box(40, ys[i], 520, 80, title, sub, col, None, 22, sub_size=17)
        b += '<!--packet-->'
        for i in range(7):
            b += f'<path d="M300 {ys[i] + 80}V{ys[i + 1]}" stroke="{cols[i + 1]}" stroke-opacity=".7" stroke-width="2" stroke-dasharray="3 5"/>'
        gy = ys[-1] + 112
        b += f'<rect x="40" y="{gy}" width="520" height="120" rx="18" fill="none" stroke="{C["amber"]}" stroke-opacity=".6" stroke-dasharray="6 6"/>'
        b += shield(76, gy + 40, C['amber'])
        for i, line in enumerate(wrap(' '.join(t['gate']), 40)):
            b += text(110, gy + 34 + i * 24, line, 16, '#FDE68A' if i else C['amber'])
        b += text(w / 2, h - 20, T[lang]['illus'], 15, C['muted'], anchor='middle')
        lens = [ys[i] - ys[0] for i in range(8)]
        total = ys[-1] - ys[0]
        anchors = [(300, y + 40) for y in ys]
    else:
        w, h = 1200, 520
        defs, b = arch_frame(w, h, t['kicker'], C['pink'])
        cx = [145, 375, 605, 835, 1065]
        top_y, bot_y = 92, 262
        path = f'M{cx[0]} {top_y + 44}H{cx[4]}V{bot_y + 44}H{cx[0]}'
        b += f'<path d="{path}" fill="none" stroke="url(#chain)" stroke-width="2.4" opacity=".5"/>' + '<!--packet-->'
        for i, (title, sub) in enumerate(t['top']):
            b += box(cx[i] - 105, top_y, 210, 88, title, sub, cols[i], None, 18, sub_size=13)
        for j, (title, sub) in enumerate(t['bottom']):
            x = [cx[4], cx[2], cx[0]][j]
            b += box(x - 105, bot_y, 210, 88, title, sub, cols[5 + j], None, 18, sub_size=13)
        gy = 392
        b += f'<rect x="40" y="{gy}" width="1120" height="76" rx="18" fill="none" stroke="{C["amber"]}" stroke-opacity=".6" stroke-dasharray="6 6"/>'
        b += shield(80, gy + 38, C['amber'])
        b += text(112, gy + 32, t['gate'][0], 16, C['amber'], 600) + text(112, gy + 56, t['gate'][1], 16, '#FDE68A')
        b += text(w - 40, h - 14, T[lang]['illus'], 13, C['muted'], anchor='end')
        seg_top = cx[4] - cx[0]
        lens = [cx[i] - cx[0] for i in range(5)] + [seg_top + 170, seg_top + 170 + (cx[4] - cx[2]), seg_top + 170 + (cx[4] - cx[0])]
        total = seg_top * 2 + 170
        anchors = [(x, top_y + 44) for x in cx] + [(cx[4], bot_y + 44), (cx[2], bot_y + 44), (cx[0], bot_y + 44)]
    b = b.replace('<!--packet-->', packet_svg(path, period))
    defs += linear('chain', [(0, C['lilac']), (.5, C['pink']), (1, C['mint'])], x2=1 if not mobile else 0, y2=0 if not mobile else 1)
    return document(w, h, t['title'], t['desc'], b, defs)


# ---------------------------------------------------------------- bento overview
BENTO = {
    'en': {'title': 'Selected work at a glance', 'kicker': 'SELECTED WORK',
           'bid': ('NATIVE macOS APP', 'Before I Deploy', 'Checks a web project and takes it to release.', ['172 tests passing', '8 checks', '3 platforms']),
           'police': ('FIVEM OPERATIONS', 'TLR Police Portal', 'Roster, ranks and handbook synced with Discord.', ['role-ID access', 'audit records']),
           'tlr': ('COMMUNITY PLATFORM', 'The Last Republic', 'Site, rules and a timed exam reviewed in Discord.', ['23 API routes', 'signed Discord flow']),
           'loc': ('42.6k', 'lines of code in Before I Deploy'),
           'certs': ('6 + 129', 'certificates and Google lessons'),
           'stack': ('68', 'technologies · 12 in shipped products'),
           'hire': ('AVAILABLE', 'Paid projects', 'websites · software · bots', 'Fraisbg1@gmail.com')},
    'bg': {'title': 'Избрана работа накратко', 'kicker': 'ИЗБРАНА РАБОТА',
           'bid': ('НАТИВНО macOS ПРИЛОЖЕНИЕ', 'Before I Deploy', 'Проверява уеб проект и го води до публикуване.', ['172 теста минават', '8 проверки', '3 платформи']),
           'police': ('FIVEM ОПЕРАЦИИ', 'TLR Police Portal', 'Състав, звания и наръчник, свързани с Discord.', ['достъп по ID на роля', 'журнал']),
           'tlr': ('ОБЩНОСТНА ПЛАТФОРМА', 'The Last Republic', 'Сайт, правила и изпит с решения в Discord.', ['23 API маршрута', 'подписан Discord поток']),
           'loc': ('42.6k', 'реда код в Before I Deploy'),
           'certs': ('6 + 129', 'сертификата и Google урока'),
           'stack': ('68', 'технологии · 12 в готови продукти'),
           'hire': ('СВОБОДЕН', 'Платени проекти', 'сайтове · софтуер · ботове', 'Fraisbg1@gmail.com')},
}


@lru_cache(maxsize=None)
def thumb(name, width=640, crop_h=None):
    import base64
    import io
    from PIL import Image
    from frame_screens import inner_area
    image = Image.open(ROOT / f'assets/screens/{name}.jpg').convert('RGB')
    image = image if '/' in name else image.crop(inner_area(image))
    image = image.resize((width, round(image.height * width / image.width)), Image.LANCZOS)
    buffer = io.BytesIO()
    image.save(buffer, 'JPEG', quality=70, optimize=True, progressive=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buffer.getvalue()).decode(), image.size


def bento_tile(idx, x, y, w, h, a1, a2):
    gid = f'bt{idx}'
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a1}" stop-opacity=".22"/>'
            f'<stop offset=".5" stop-color="#0E0B2C" stop-opacity=".9"/><stop offset="1" stop-color="{a2}" stop-opacity=".14"/></linearGradient>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="url(#{gid})" stroke="#fff" stroke-opacity=".1"/>'
            f'<rect class="live edge" style="animation-delay:{idx * 1.3:.1f}s" x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="none" '
            f'stroke="{a1}" stroke-width="2" pathLength="1000" stroke-dasharray="120 880"/>')


def bento_shot(idx, name, x, y, w, h, crop_from_top=True):
    href, (iw, ih) = thumb(name)
    dh = ih * w / iw
    return (f'<clipPath id="bs{idx}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14"/></clipPath>'
            f'<g clip-path="url(#bs{idx})"><g class="kb" style="animation-delay:-{idx * 3}s">'
            f'<image href="{href}" x="{x}" y="{y}" width="{w}" height="{dh:.0f}" preserveAspectRatio="xMidYMin meet"/></g>'
            f'<rect x="{x}" y="{y + h - 70}" width="{w}" height="70" fill="url(#shade)"/></g>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="none" stroke="#fff" stroke-opacity=".14"/>')


def bento(lang, mobile):
    t = BENTO[lang]
    w = 600 if mobile else 1200
    pad, gap = (32, 16) if mobile else (32, 16)
    defs = (linear('bg', [(0, C['night']), (.55, '#150F40'), (1, C['deep'])], x2=1, y2=1)
            + linear('shade', [(0, '#05060C', 0), (1, '#05060C', .85)], x2=0, y2=1)
            + linear('hot', [(0, '#FFFFFF'), (.6, C['lilac2']), (1, C['cyan'])], x2=1, y2=1)
            + linear('warm', [(0, C['amber']), (1, C['pink'])], x2=1, y2=1)
            + radial('au1', C['violet'], .4) + radial('au2', C['cyan'], .28))
    motion = ('.edge{animation:edge 10.4s linear infinite;opacity:0}@keyframes edge{0%{opacity:1;stroke-dashoffset:0}12%{opacity:1}14%,100%{opacity:0;stroke-dashoffset:-1000}}'
              '.kb{transform-box:fill-box;transform-origin:center top;animation:kb 18s ease-in-out infinite alternate}@keyframes kb{to{transform:scale(1.06)}}'
              '.aur{animation:aur 30s ease-in-out infinite}@keyframes aur{50%{transform:translate(-70px,30px)}}'
              '.pulse{animation:pulse 3.6s ease-in-out infinite}@keyframes pulse{50%{opacity:.35}}')
    if mobile:
        cw = w - 2 * pad
        half = (cw - gap) / 2
        tiles = {'bid': (pad, 32, cw, 432), 'police': (pad, 480, cw, 330), 'tlr': (pad, 826, cw, 330),
                 'loc': (pad, 1172, half, 200), 'certs': (pad + half + gap, 1172, half, 200),
                 'stack': (pad, 1388, half, 200), 'hire': (pad + half + gap, 1388, half, 200)}
        h = 1620
    else:
        unit = (w - 2 * pad - 3 * gap) / 4
        row = 206
        tiles = {'bid': (pad, 32, unit * 2 + gap, row * 2 + gap), 'police': (pad + 2 * (unit + gap), 32, unit * 2 + gap, row),
                 'tlr': (pad + 2 * (unit + gap), 32 + row + gap, unit * 2 + gap, row),
                 'loc': (pad, 32 + 2 * (row + gap), unit, row - 20), 'certs': (pad + unit + gap, 32 + 2 * (row + gap), unit, row - 20),
                 'stack': (pad + 2 * (unit + gap), 32 + 2 * (row + gap), unit, row - 20), 'hire': (pad + 3 * (unit + gap), 32 + 2 * (row + gap), unit, row - 20)}
        h = int(32 + 3 * row + 2 * gap - 20 + 32)
    b = frame(w, h, 32) + '<g clip-path="url(#frame)">'
    b += f'<g class="aur"><circle cx="{w * .8:.0f}" cy="{h * .1:.0f}" r="{w * .5:.0f}" fill="url(#au1)"/></g><circle cx="{w * .1:.0f}" cy="{h:.0f}" r="{w * .45:.0f}" fill="url(#au2)"/>'
    accents = {'bid': (C['violet'], C['cyan']), 'police': (C['cyan'], C['mint']), 'tlr': (C['pink'], C['violet']),
               'loc': (C['lilac'], C['cyan']), 'certs': (C['amber'], C['pink']), 'stack': (C['mint'], C['cyan']), 'hire': (C['mint'], C['lilac'])}
    shots = {'bid': 'before-i-deploy', 'police': 'police-dashboard', 'tlr': 'tlr/home'}
    for idx, (key, (x, y, tw, th)) in enumerate(tiles.items()):
        a1, a2 = accents[key]
        b += bento_tile(idx, x, y, tw, th, a1, a2)
        if key in shots:
            kicker, name, line, chips = t[key]
            big = key == 'bid'
            if big and not mobile:
                sx, sy, sw, sh = x + 22, y + 22, tw - 44, th - 210
                ty = y + th - 168
            elif big:
                sx, sy, sw, sh = x + 18, y + 18, tw - 36, 210
                ty = y + 262
            else:
                if mobile:
                    sx, sy, sw, sh = x + 18, y + 18, tw - 36, 120
                    ty = y + 170
                else:
                    sw = tw * .46
                    sx, sy, sh = x + tw - sw - 18, y + 18, th - 36
                    ty = y + 50
            b += bento_shot(idx, shots[key], sx, sy, sw, sh)
            tx = x + (22 if big or mobile else 24)
            maxw = (tw - 48) if (big or mobile) else (tw - sw - 66)
            b += text(tx, ty, kicker, 12 if not mobile else 15, a1, 800, spacing=2)
            b += display(name, tx, ty + (40 if big else 34), fit(name, 34 if big else 24, maxw), 'url(#hot)')
            for i, l in enumerate(wrap(line, 52 if big and not mobile else (40 if mobile else 26))[:2 if (not big or mobile) else 1]):
                b += text(tx, ty + (70 if big else 60) + i * 21, l, 15 if not mobile else 17, C['soft'])
            cx_ = tx
            cy_ = y + th - (28 if not mobile else 26)
            for chip in chips if (big or mobile or True) else []:
                cwid = len(chip) * (7.6 if not mobile else 8.6) + 26
                if cx_ + cwid > x + (tw if (big or mobile) else tw - sw - 30) - 10:
                    break
                b += (f'<rect x="{cx_}" y="{cy_ - 20}" width="{cwid:.0f}" height="28" rx="14" fill="{a1}" fill-opacity=".14" stroke="{a1}" stroke-opacity=".5"/>'
                      + text(cx_ + 13, cy_ - 1, chip, 13 if not mobile else 15, C['text'], 700))
                cx_ += cwid + 8
        elif key == 'hire':
            badge, line, sub, mail = t['hire']
            b += f'<circle class="pulse" cx="{x + 30}" cy="{y + 40}" r="7" fill="#4ADE80"/>'
            b += text(x + 46, y + 46, badge, 14 if not mobile else 15, '#B3F6D2', 800, spacing=2)
            words = line.split()
            fs = min(fit(wd, 26, tw - 48) for wd in words)
            for i, wd in enumerate(words):
                b += display(wd, x + 24, y + 88 + i * fs * 1.2, fs, 'url(#hot)')
            b += text(x + 24, y + 96 + len(words) * fs * 1.2 - fs * .6, sub, 13 if not mobile else 14, C['soft'])
            b += glyph('mail', x + 24, y + th - 40, 20, C['pink']) + text(x + 52, y + th - 24, mail, 13 if not mobile else 14, C['text'], 700)
        else:
            value, label = t[key]
            b += display(value, x + 24, y + 86, fit(value, 46, tw - 48), 'url(#warm)' if key == 'certs' else 'url(#hot)', weight=800)
            for i, l in enumerate(wrap(label, 24 if not mobile else 20)):
                b += text(x + 24, y + 122 + i * 21, l, 15 if not mobile else 16, C['soft'])
            if key == 'certs':
                for k, slug in enumerate(['googlegemini', 'googleads', 'hubspot', 'google']):
                    b += icon(slug, x + 24 + k * 30, y + th - 40, 20, ['#A78BFA', '#4285F4', '#FF7A59', '#fff'][k])
            if key == 'stack':
                for k, slug in enumerate(['swift', 'typescript', 'nextdotjs', 'postgresql', 'discord']):
                    b += icon(slug, x + 24 + k * 30, y + th - 40, 20, ['#F05138', '#3178C6', '#fff', '#4F7BFF', '#7C8BFF'][k])
            if key == 'loc':
                bx_, bw_ = x + 24, tw - 48
                total = 42630
                for c, n in [('#F1E05A', 17759), ('#F05138', 15103), ('#3178C6', 5446), ('#E38C00', 3346), ('#8B8FB0', 976)]:
                    seg = bw_ * n / total
                    b += f'<rect x="{bx_:.1f}" y="{y + th - 34}" width="{seg:.1f}" height="8" fill="{c}"/>'
                    bx_ += seg
    b += '</g>'
    desc = (f"{t['bid'][1]}: {t['bid'][2]} {', '.join(t['bid'][3])}. {t['police'][1]}: {t['police'][2]} {t['tlr'][1]}: {t['tlr'][2]} "
            f"{t['loc'][0]} {t['loc'][1]}. {t['certs'][0]} {t['certs'][1]}. {t['stack'][0]} {t['stack'][1]}. {t['hire'][0]} {t['hire'][1]}: {t['hire'][2]}.")
    return document(w, h, t['title'], desc, b, defs, motion)


# ---------------------------------------------------------------- services
SERVICES = json.loads((ROOT / 'data/services.json').read_text())
SV = {'en': {'kicker': 'SERVICES · WHAT YOU CAN HIRE ME FOR', 'title': 'Services'},
      'bg': {'kicker': 'УСЛУГИ · ЗА КАКВО МОЖЕТЕ ДА МЕ НАЕМЕТЕ', 'title': 'Услуги'}}
SERVICE_COLORS = [(C['cyan'], C['violet']), (C['violet'], C['pink']), ('#7C8BFF', C['cyan']),
                  (C['pink'], C['amber']), (C['mint'], C['cyan']), (C['amber'], C['mint'])]


def services(lang, mobile):
    items = SERVICES[lang]
    w = 600 if mobile else 1200
    pad, gap = 32, 16
    cols = 1 if mobile else 3
    cw = (w - 2 * pad - (cols - 1) * gap) / cols
    ch = 268 if mobile else 312
    top = 84
    rows = math.ceil(len(items) / cols)
    h = int(top + rows * ch + (rows - 1) * gap + 32)
    defs = (linear('bg', [(0, C['night']), (.55, '#150F40'), (1, C['deep'])], x2=1, y2=1)
            + radial('au1', C['violet'], .38) + radial('au2', C['cyan'], .26)
            + linear('shine', [(0, '#fff', 0), (.5, '#fff', .12), (1, '#fff', 0)]))
    n = len(items)
    motion = ('.aur{animation:aur 30s ease-in-out infinite}@keyframes aur{50%{transform:translate(-70px,30px)}}'
              f'.shine{{animation:shine {n * 1.5:.1f}s ease-in-out infinite}}'
              f'@keyframes shine{{0%{{transform:translateX(0) skewX(-16deg)}}{100 / n * 1.3:.1f}%,100%{{transform:translateX({cw + 300:.0f}px) skewX(-16deg)}}}}')
    b = frame(w, h, 30) + '<g clip-path="url(#frame)">'
    b += f'<g class="aur"><circle cx="{w * .85:.0f}" cy="{h * .1:.0f}" r="{w * .5:.0f}" fill="url(#au1)"/></g><circle cx="{w * .1:.0f}" cy="{h:.0f}" r="{w * .45:.0f}" fill="url(#au2)"/>'
    for i, line in enumerate(wrap(SV[lang]['kicker'], 34) if mobile else [SV[lang]['kicker']]):
        b += text(pad, 52 + i * 22, line, 16 if mobile else 13, C['lilac2'], 800, spacing=2.2)
    if mobile:
        top += 18
        h += 18
    for i, item in enumerate(items):
        a1, a2 = SERVICE_COLORS[i]
        r_, c_ = divmod(i, cols)
        x, y = pad + c_ * (cw + gap), top + r_ * (ch + gap)
        gid = f'sv{i}'
        b += (f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a1}" stop-opacity=".2"/>'
              f'<stop offset=".55" stop-color="#0E0B2C" stop-opacity=".9"/><stop offset="1" stop-color="{a2}" stop-opacity=".12"/></linearGradient>'
              f'<rect x="{x}" y="{y}" width="{cw:.0f}" height="{ch}" rx="24" fill="url(#{gid})" stroke="{a1}" stroke-opacity=".45"/>'
              f'<rect x="{x + 22}" y="{y}" width="{cw - 44:.0f}" height="3" rx="1.5" fill="{a1}"/>')
        b += display(f'{i + 1:02d}', x + 22, y + 52, 26, 'none', extra=f'stroke="{a1}" stroke-width="1.4"')
        tl = wrap(item['title'], 22 if not mobile else 30)
        fs = min(fit(l, 21 if not mobile else 23, cw - 44) for l in tl)
        for k, l in enumerate(tl):
            b += display(l, x + 22, y + 92 + k * fs * 1.3, fs, C['text'])
        dy = y + 92 + len(tl) * fs * 1.3 + 8
        for k, l in enumerate(wrap(item['desc'], 44 if not mobile else 54)[:4]):
            b += text(x + 22, dy + k * 21, l, 14.5 if not mobile else 16, C['soft'])
        for k, l in enumerate(wrap(item['tags'], 46 if not mobile else 56)[:2]):
            b += text(x + 22, y + ch - 22 - (len(wrap(item['tags'], 46 if not mobile else 56)[:2]) - 1 - k) * 18, l, 12.5 if not mobile else 14, a1, 700)
        b += (f'<g class="live"><clipPath id="sc{i}"><rect x="{x}" y="{y}" width="{cw:.0f}" height="{ch}" rx="24"/></clipPath><g clip-path="url(#sc{i})">'
              f'<rect class="shine" style="animation-delay:{i * 1.5:.1f}s" x="{x - 160}" y="{y - 40}" width="110" height="{ch + 80}" fill="url(#shine)"/></g></g>')
    b += '</g>'
    desc = ' '.join(f"{it['title']}: {it['desc']} ({it['tags']})." for it in items)
    return document(w, int(h), SV[lang]['title'], desc, b, defs, motion)


# ---------------------------------------------------------------- main
def main():
    count = 0
    for lang in ('en', 'bg'):
        for mobile in (False, True):
            sfx = f'{lang}{"-mobile" if mobile else ""}.svg'
            files = {f'hero-{sfx}': hero(lang, mobile), f'arch-bid-{sfx}': arch_bid(lang, mobile),
                     f'arch-tlr-{sfx}': arch_tlr(lang, mobile), f'stack-used-{sfx}': stack_used(lang, mobile),
                     f'process-{sfx}': process(lang, mobile), f'finale-{sfx}': finale(lang, mobile), f'footer-{sfx}': footer(lang, mobile)}
            for i in range(len(DIVIDERS)):
                files[f'divider-{i + 1:02d}-{sfx}'] = divider(i, lang, mobile)
            for key in PROJECTS:
                files[f'project-{key}-{sfx}'] = project_marker(key, lang, mobile)
            for v, group in enumerate(GROUPS):
                files[f'stack-{group}-{sfx}'] = stack_group(group, v, lang, mobile)
            if not mobile:
                for key in SCENES:
                    files[f'scene-{key}-{lang}.svg'] = scene(key, lang)
            files[f'under-hood-{sfx}'] = under_hood(lang, mobile)
            files[f'bento-{sfx}'] = bento(lang, mobile)
            files[f'services-{sfx}'] = services(lang, mobile)
            files[f'arch-whitelist-{sfx}'] = arch_whitelist(lang, mobile)
            files[f'certificates-{sfx}'] = certificates(lang, mobile)
            files[f'lessons-{sfx}'] = lessons_panel(lang, mobile)
            if not mobile:
                for kind in BUTTONS:
                    files[f'contact-{kind}-{lang}.svg'] = contact_button(kind, lang)
            for name, content in files.items():
                write(name, content)
                count += 1
    shown = sum(1 for i in TECH['technologies'])
    assert shown == 68, shown
    print(f'{count} files written to {OUT.relative_to(ROOT)}; technologies: {shown}')


if __name__ == '__main__':
    main()
