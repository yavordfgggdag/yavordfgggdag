#!/usr/bin/env python3
"""Re-frame the genuine interface captures with a per-project colour accent.

The original files in assets/screens/ stay untouched. Their presentation frame
(caption above, note below) is removed so the README heading is not repeated,
and the unmodified interface area is placed on a coloured stage.
Requires Pillow; run manually, not in the public workflow.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'assets/screens'
OUT = SRC / 'framed'

# Accent pairs follow the project colours used in assets/motion/.
ACCENTS = {
    'bid': ('#A78BFA', '#22D3EE'),
    'police': ('#22D3EE', '#34D399'),
    'client': ('#FBBF24', '#F472B6'),
    'community': ('#34D399', '#A78BFA'),
}
SHOTS = {
    'before-i-deploy.jpg': 'bid', 'bid-mission-control.jpg': 'bid', 'bid-command-palette.jpg': 'bid',
    'police-dashboard.jpg': 'police', 'police-employees.jpg': 'police',
    'police-ranks.jpg': 'police', 'police-handbook.jpg': 'police',
    'client-education.jpg': 'client', 'client-education-faq.jpg': 'client',
    'community-platform.jpg': 'community', 'community-rules.jpg': 'community',
}
STAGE = (13, 10, 34)
PAD = 34
RADIUS = 18


def hex_rgb(value):
    value = value.lstrip('#')
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def inner_area(image):
    """Find the captured interface inside the original presentation frame."""
    grey = image.convert('L')
    width, height = grey.size
    background = grey.getpixel((10, height // 2))
    bottom = 106
    while bottom < height and grey.getpixel((28, bottom)) > background + 18:
        bottom += 1
    return (29, 106, width - 29, bottom - 1)


def gradient(size, start, end):
    width, height = size
    a, b = hex_rgb(start), hex_rgb(end)
    strip = Image.new('RGB', (width, 1))
    for x in range(width):
        t = x / max(width - 1, 1)
        strip.putpixel((x, 0), tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3)))
    return strip.resize(size)


def frame(name, accent):
    original = Image.open(SRC / name).convert('RGB')
    shot = original.crop(inner_area(original))
    width, height = shot.size
    canvas_size = (width + PAD * 2, height + PAD * 2)
    start, end = ACCENTS[accent]

    stage = Image.new('RGB', canvas_size, STAGE)
    glow = Image.new('L', canvas_size, 0)
    ImageDraw.Draw(glow).rounded_rectangle((PAD - 6, PAD - 6, PAD + width + 6, PAD + height + 6), RADIUS + 6, fill=150)
    glow = glow.filter(ImageFilter.GaussianBlur(22))
    stage = Image.composite(gradient(canvas_size, start, end), stage, glow)

    border = Image.new('L', canvas_size, 0)
    ImageDraw.Draw(border).rounded_rectangle((PAD - 2, PAD - 2, PAD + width + 1, PAD + height + 1), RADIUS + 2, fill=255)
    stage = Image.composite(gradient(canvas_size, start, end), stage, border)

    mask = Image.new('L', shot.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, width - 1, height - 1), RADIUS, fill=255)
    stage.paste(shot, (PAD, PAD), mask)
    OUT.mkdir(exist_ok=True)
    stage.save(OUT / name, quality=84, optimize=True, progressive=True)
    return stage.size


if __name__ == '__main__':
    for file_name, accent_name in SHOTS.items():
        print(file_name, frame(file_name, accent_name))
