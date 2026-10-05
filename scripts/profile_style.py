"""Shared visual language for every generated profile SVG.

Palette: deep indigo base; electric violet, pink, cyan and mint accents; warm amber
where a composition needs heat. Every file is self-contained (no scripts, remote
fonts or external images) so GitHub can serve it as an <img>.

Motion rule used everywhere: the default render is a complete static composition.
Animation is added only inside `@media (prefers-reduced-motion: no-preference)`.
Elements that exist only for motion carry class `live`; their static stand-ins
carry class `still`.
"""
from html import escape

FONT = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,'SF Mono','Cascadia Mono',Menlo,Consolas,monospace"

C = {
    'night': '#08061A', 'ink': '#0D0A26', 'indigo': '#151040', 'indigo2': '#1D1752', 'deep': '#071B2B',
    'violet': '#8B5CF6', 'lilac': '#A78BFA', 'lilac2': '#C4B5FD',
    'pink': '#F472B6', 'magenta': '#EC4899',
    'cyan': '#22D3EE', 'sky': '#38BDF8',
    'mint': '#34D399', 'mint2': '#5EEAD4',
    'amber': '#FBBF24', 'amber2': '#F59E0B',
    'text': '#F7F5FF', 'soft': '#DCD6FF', 'muted': '#ADA6DA', 'line': '#3B3378', 'glass': '#1A1548',
}

ACCENTS = {
    'violet': (C['violet'], C['cyan']),
    'pink': (C['pink'], C['amber']),
    'cyan': (C['cyan'], C['mint']),
    'mint': (C['mint'], C['lilac']),
    'amber': (C['amber'], C['pink']),
}


def esc(value):
    return escape(str(value), quote=True)


def text(x, y, value, size=20, fill=None, weight=400, anchor=None, extra='', mono=False, spacing=None, cls=None):
    attrs = [f'x="{x:g}"' if isinstance(x, (int, float)) else f'x="{x}"', f'y="{y:g}"', f'font-size="{size}"',
             f'fill="{fill or C["text"]}"']
    if weight != 400:
        attrs.append(f'font-weight="{weight}"')
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    if spacing:
        attrs.append(f'letter-spacing="{spacing}"')
    if mono:
        attrs.append('class="mono"' if not cls else f'class="mono {cls}"')
    elif cls:
        attrs.append(f'class="{cls}"')
    if extra:
        attrs.append(extra)
    return f'<text {" ".join(attrs)}>{esc(value)}</text>'


def linear(id_, stops, x2=1, y2=0, x1=0, y1=0):
    body = ''
    for stop in stops:
        offset, color = stop[0], stop[1]
        opacity = f' stop-opacity="{stop[2]}"' if len(stop) > 2 else ''
        body += f'<stop offset="{offset}" stop-color="{color}"{opacity}/>'
    return f'<linearGradient id="{id_}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{body}</linearGradient>'


def radial(id_, color, opacity=0.5):
    return (f'<radialGradient id="{id_}"><stop offset="0" stop-color="{color}" stop-opacity="{opacity}"/>'
            f'<stop offset=".55" stop-color="{color}" stop-opacity="{opacity * .35:.3f}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>')


def document(width, height, title, desc, body, defs='', motion='', css=''):
    """Wrap content in a standalone, accessible SVG with the shared motion contract."""
    style = (f'text{{font-family:{FONT}}}.mono{{font-family:{MONO}}}.live{{display:none}}{css}'
             f'@media (prefers-reduced-motion:no-preference){{.live{{display:inline}}.still{{display:none}}{motion}}}')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
            f'role="img" aria-labelledby="title desc"><title id="title">{esc(title)}</title><desc id="desc">{esc(desc)}</desc>'
            f'<defs>{defs}</defs><style>{style}</style>{body}</svg>\n')


def wrap(value, limit):
    """Greedy word wrap by character count (good enough for the fixed system fonts)."""
    lines, line = [], ''
    for word in str(value).split():
        candidate = f'{line} {word}'.strip()
        if len(candidate) > limit and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines
