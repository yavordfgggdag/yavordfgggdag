"""Structural checks for the bilingual profile README.

Run from the repository root: python3 scripts/test_profile.py
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = (ROOT / 'README.md').read_text()
BG = (ROOT / 'README.bg.md').read_text()
ASSET = re.compile(r'(?:src|srcset)="([^"]+)"')


def local_assets(markdown):
    return [a for a in ASSET.findall(markdown) if not a.startswith('http')]


def neutral(path):
    return re.sub(r'(?<=[-/])(en|bg)(?=[-.])', 'XX', path)


class ProfileTests(unittest.TestCase):
    def test_every_local_image_exists(self):
        for markdown in (EN, BG):
            for path in local_assets(markdown):
                self.assertTrue((ROOT / path).is_file(), path)

    def test_languages_have_the_same_visual_scope(self):
        en = [neutral(a) for a in local_assets(EN)]
        bg = [neutral(a) for a in local_assets(BG)]
        self.assertEqual(en, bg)

    def test_same_sections_galleries_and_links(self):
        for token in ('<details>', '<picture>', '](mailto:', 'pomoshtotpriyatel.com', 'instagram.com/y.yakowvw.sales'):
            self.assertEqual(EN.count(token), BG.count(token), token)

    def test_all_68_technologies_are_rendered(self):
        tech = json.loads((ROOT / 'data/technologies.json').read_text())['technologies']
        self.assertEqual(len(tech), 68)
        for item in tech:
            for lang in ('en', 'bg'):
                for suffix in ('', '-mobile'):
                    svg = (ROOT / f'assets/motion/stack-{item["group"]}-{lang}{suffix}.svg').read_text()
                    self.assertIn(item['name'].replace('&', '&amp;'), svg, (item['name'], lang, suffix))

    def test_certificates_section(self):
        data = json.loads((ROOT / 'data/certificates.json').read_text())
        lessons = data['collections'][0]['lessons']
        for markdown in (EN, BG):
            for item in data['featured']:
                self.assertIn(item['title'], markdown)
            for lesson in lessons:
                self.assertIn(lesson['title'], markdown)

    def test_contacts_present_in_both(self):
        for markdown in (EN, BG):
            for value in ('Fraisbg1@gmail.com', 'Fraisbg', '@y.yakowvw.sales'):
                self.assertIn(value, markdown)

    def test_phone_number_is_not_published(self):
        for path in [ROOT / 'README.md', ROOT / 'README.bg.md', *(ROOT / 'assets').rglob('*.svg')]:
            text = path.read_text()
            self.assertIsNone(re.search(r'898.?634.?678|359898634678', text), path)

    def test_no_private_repository_names_or_remote_widgets(self):
        for markdown in (EN, BG):
            for banned in ('chillrp-website', 'fraisbg1`', 'tihagranica', 'visitor-badge', 'img.shields.io'):
                self.assertNotIn(banned, markdown)

    def test_motion_assets_are_self_contained_and_respect_reduced_motion(self):
        for svg in (ROOT / 'assets/motion').glob('*.svg'):
            content = svg.read_text()
            for banned in ('<script', 'foreignObject', 'href="http', '@import', '<image'):
                self.assertNotIn(banned, content, svg.name)
            if '@keyframes' in content or '<animate' in content:
                self.assertIn('prefers-reduced-motion:no-preference', content, svg.name)


if __name__ == '__main__':
    unittest.main()
