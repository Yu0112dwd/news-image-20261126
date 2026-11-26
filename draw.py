"""Draw the news-image-20261126 entry: a one-page newspaper front page
summing up Thursday 26 November 2026. Pure Pillow, no network, no fonts
beyond the DejaVu family shipped with the system. Output: entry.png,
1024 x 1024, well under 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (24, 24, 24)
RED = (178, 34, 34)
BLUE = (28, 68, 120)
TEAL = (14, 110, 110)
GOLD = (176, 124, 18)
GREY = (90, 88, 82)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, x, y, w, h, accent, tag, headline, caption, icon):
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=2)
    draw.rectangle([x, y, x + w, y + 30], fill=accent)
    draw.text((x + 10, y + 6), tag, font=font(BOLD, 17), fill=(255, 255, 255))
    icon(x + 10, y + 42, w - 20, 108, draw)
    ty = y + 158
    for line in wrap(draw, headline, font(BOLD, 23), w - 20):
        draw.text((x + 10, ty), line, font=font(BOLD, 23), fill=INK)
        ty += 28
    for line in wrap(draw, caption, font(REG, 17), w - 20):
        draw.text((x + 10, ty), line, font=font(REG, 17), fill=GREY)
        ty += 22


def icon_tariffs(x, y, w, h, d):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    bars = [(36, 46), (48, 62), (28, 34), (56, 78), (40, 52)]
    cols = [BLUE, RED, GOLD, TEAL, (120, 60, 140)]
    bw = 52
    for i, (bh, _) in enumerate([(b, 0) for b, _ in bars]):
        pass
    for i, (bh, col) in enumerate(zip([b for b, _ in bars], cols)):
        xx = x + 24 + i * 84
        d.rectangle([xx, y + h - 12 - bh, xx + bw, y + h - 12], fill=col)
    d.line([x + 10, y + h - 12, x + w - 10, y + h - 12], fill=INK, width=2)
    d.text((x + 24, y + 8), "14 PARTNERS", font=font(BOLD, 22), fill=RED)


def icon_fire(x, y, w, h, d):
    d.rectangle([x, y, x + w, y + h], fill=(40, 32, 28))
    d.rectangle([x + 40, y + 66, x + w - 40, y + 88], fill=(150, 150, 150))
    d.ellipse([x + 60, y + 88, x + 90, y + 104], fill=INK)
    d.ellipse([x + w - 90, y + 88, x + w - 60, y + 104], fill=INK)
    cx = x + w // 2
    d.polygon([(cx - 70, y + 66), (cx - 30, y + 6), (cx - 6, y + 40),
               (cx + 14, y + 2), (cx + 34, y + 34), (cx + 70, y + 66)],
              fill=(255, 120, 0))
    d.polygon([(cx - 34, y + 66), (cx - 12, y + 26), (cx + 4, y + 48),
               (cx + 20, y + 30), (cx + 34, y + 66)], fill=(255, 200, 40))


def icon_satellite(x, y, w, h, d):
    d.rectangle([x, y, x + w, y + h], fill=(16, 24, 48))
    for sx, sy in [(x + 60, y + 20), (x + 180, y + 44), (x + 300, y + 16), (x + 380, y + 60)]:
        d.ellipse([sx, sy, sx + 5, sy + 5], fill=(255, 255, 255))
    cx, cy = x + w // 2, y + h // 2
    d.rectangle([cx - 90, cy - 26, cx - 30, cy + 26], fill=(70, 130, 200))
    d.rectangle([cx + 30, cy - 26, cx + 90, cy + 26], fill=(70, 130, 200))
    for i in range(3):
        d.line([cx - 90, cy - 26 + i * 26, cx - 30, cy - 26 + i * 26], fill=(200, 220, 240), width=2)
        d.line([cx + 30, cy - 26 + i * 26, cx + 90, cy - 26 + i * 26], fill=(200, 220, 240), width=2)
    d.rectangle([cx - 30, cy - 18, cx + 30, cy + 18], fill=(230, 230, 235))
    d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=GOLD)
    d.text((x + 20, y + 6), "1,000,000", font=font(BOLD, 22), fill=(255, 210, 60))


def icon_plane(x, y, w, h, d):
    d.rectangle([x, y, x + w, y + h], fill=(200, 225, 245))
    d.ellipse([x + 30, y + 70, x + 110, y + 96], fill=(255, 255, 255))
    d.ellipse([x + 260, y + 30, x + 330, y + 52], fill=(255, 255, 255))
    cx, cy = x + w // 2, y + h // 2 + 6
    d.polygon([(cx - 90, cy), (cx - 30, cy - 14), (cx + 60, cy - 14),
               (cx + 110, cy), (cx + 60, cy + 14), (cx - 30, cy + 14)], fill=(230, 230, 235))
    d.polygon([(cx - 10, cy - 14), (cx + 10, cy - 44), (cx + 26, cy - 14)], fill=RED)
    d.polygon([(cx - 10, cy + 14), (cx + 10, cy + 44), (cx + 26, cy + 14)], fill=RED)
    d.ellipse([cx + 76, cy - 6, cx + 92, cy + 6], fill=BLUE)
    d.line([x + 10, y + h - 8, x + w - 10, y + h - 8], fill=(90, 120, 60), width=4)


def icon_flag(x, y, w, h, d):
    d.rectangle([x, y, x + w, y + h], fill=(245, 245, 245))
    d.rectangle([x + 24, y + 12, x + 30, y + h - 10], fill=INK)
    d.rectangle([x + 30, y + 14, x + w - 60, y + 66], fill=RED)
    d.ellipse([x + 70, y + 26, x + 130, y + 54], fill=(255, 255, 255))
    d.ellipse([x + 92, y + 32, x + 108, y + 48], fill=RED)
    d.text((x + w - 150, y + 76), "48 HOURS", font=font(BOLD, 22), fill=INK)


def icon_scales(x, y, w, h, d):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    cx, cy = x + w // 2, y + 14
    d.rectangle([cx - 3, cy, cx + 3, cy + 78], fill=INK)
    d.polygon([(cx - 14, cy), (cx + 14, cy), (cx, cy - 12)], fill=GOLD)
    d.line([cx - 70, cy + 10, cx + 70, cy + 10], fill=INK, width=3)
    d.line([cx - 70, cy + 10, cx - 90, cy + 52], fill=INK, width=2)
    d.line([cx + 70, cy + 10, cx + 90, cy + 52], fill=INK, width=2)
    d.line([cx - 70, cy + 10, cx - 50, cy + 52], fill=INK, width=2)
    d.line([cx + 70, cy + 10, cx + 50, cy + 52], fill=INK, width=2)
    d.ellipse([cx - 100, cy + 48, cx - 40, cy + 62], fill=GOLD)
    d.ellipse([cx + 40, cy + 48, cx + 100, cy + 62], fill=GOLD)
    d.rectangle([cx - 70, cy + 84, cx + 70, cy + 92], fill=INK)


PANELS = [
    (RED, "WASHINGTON", "US proposes tariffs on 14 trading partners",
     "China, the EU, Japan and India among the economies named.", icon_tariffs),
    ((120, 30, 20), "CAIRO", "Fuel tanker fire kills at least 31 on ring road",
     "Tanker overturns and bursts into flames; 21 hurt.", icon_fire),
    ((16, 24, 48), "SPACE", "SpaceX cleared for a million satellites",
     "FCC approves orbital data centres, the Starmind plan.", icon_satellite),
    (BLUE, "POLAND", "Poland plans no-fly zone by Ukraine border",
     "Move follows repeated airspace incursions.", icon_plane),
    (TEAL, "PYONGYANG", "North Korea expels Swiss diplomat",
     "Envoy told to leave in 48 hours; Kim widens nuclear call.", icon_flag),
    (GOLD, "JERUSALEM", "Judges urge dropping Netanyahu bribery case",
     "Court sees little chance of conviction in Case 4000.", icon_scales),
]

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Masthead
d.rectangle([0, 0, W, 118], fill=INK)
d.text((24, 12), "THE WORLD  •  ONE DAY  •  ONE PAGE", font=font(BOLD, 22), fill=(255, 210, 60))
d.text((24, 42), "THURSDAY 26 NOVEMBER 2026", font=font(BOLD, 46), fill=(255, 255, 255))
d.text((24, 94), "The day's news, in one image", font=font(REG, 20), fill=(200, 200, 200))

# Grid: 2 columns x 3 rows
gx, gy = 16, 134
pw, ph = (W - 3 * 16) // 2, 272
gap = 16
for i, (accent, tag, head, cap, icon) in enumerate(PANELS):
    x = gx + (i % 2) * (pw + gap)
    y = gy + (i // 2) * (ph + gap)
    draw_panel(d, x, y, pw, ph, accent, tag, head, cap, icon)

# Footer
fy = gy + 3 * ph + 2 * gap + 8
d.line([16, fy, W - 16, fy], fill=INK, width=2)
d.text((16, fy + 8), "Washington  •  Cairo  •  Space  •  Poland  •  Pyongyang  •  Jerusalem  —  26 November 2026",
       font=font(REG, 18), fill=GREY)

img.save("entry.png", optimize=True)
print("saved", img.size)
