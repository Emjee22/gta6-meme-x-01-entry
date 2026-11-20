#!/usr/bin/env python3
"""Draw the Leonida Express GTA 6 meme (1080x1080) with PIL.

A fake delivery-tracking page: GTA VI ordered in 2013, delayed twice,
out for delivery in launch week. The make.fun ghost is drawn from scratch
as vector shapes (my own drawing) and works as the courier's logo, plus
the make.fun name in the footer payoff. No downloaded images, no copied
files: every pixel is produced by this script.
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1080
NAVY = (13, 27, 46)
PANEL = (22, 40, 64)
PANEL_LINE = (38, 62, 96)
WHITE = (255, 255, 255)
GREY = (178, 190, 208)
DIM = (128, 145, 168)
MAGENTA = (255, 46, 136)
MAGENTA_DARK = (214, 24, 108)
GREEN = (46, 204, 113)
AMBER = (255, 176, 32)

F_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
F_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def star_points(cx, cy, r_outer, r_inner, points=5, rot=-90):
    pts = []
    for i in range(points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        a = math.radians(rot + i * 180 / points)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def sparkle(draw, cx, cy, r):
    """Four-pointed sparkle (the ghost's eye)."""
    pts = [(cx, cy - r), (cx + r * 0.28, cy - r * 0.28), (cx + r, cy),
           (cx + r * 0.28, cy + r * 0.28), (cx, cy + r),
           (cx - r * 0.28, cy + r * 0.28), (cx - r, cy),
           (cx - r * 0.28, cy - r * 0.28)]
    draw.polygon(pts, fill=(10, 10, 14))


def draw_ghost(size):
    """Return an RGBA image of the make.fun-style ghost, drawn from scratch.

    White ghost with thick black outline, two sparkle eyes, one little
    round hand holding a magenta coin with a white star.
    """
    s = size
    layer = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # Silhouette: dome + body + wavy hem (three bumps).
    body_w = int(s * 0.62)
    x0 = (s - body_w) // 2
    x1 = x0 + body_w
    dome_top = int(s * 0.06)
    hem_y = int(s * 0.86)
    bump_r = body_w // 6
    d.pieslice([x0, dome_top, x1, dome_top + body_w], 180, 360, fill=WHITE)
    d.rectangle([x0, dome_top + body_w // 2, x1, hem_y], fill=WHITE)
    for i in range(3):
        cx = x0 + bump_r + i * 2 * bump_r
        d.pieslice([cx - bump_r, hem_y - bump_r, cx + bump_r, hem_y + bump_r],
                   0, 180, fill=WHITE)
    # Thick black outline: dilate the alpha mask, paint black behind.
    alpha = layer.split()[3]
    outline = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    od = ImageDraw.Draw(outline)
    mask = alpha.filter(ImageFilter.MaxFilter(9))
    od.bitmap((0, 0), mask, fill=(8, 8, 12, 255))
    ghost = Image.alpha_composite(outline, layer)
    d = ImageDraw.Draw(ghost)
    # Eyes: two sparkles.
    eye_y = int(s * 0.42)
    eye_dx = int(s * 0.15)
    sparkle(d, s // 2 - eye_dx, eye_y, int(s * 0.075))
    sparkle(d, s // 2 + eye_dx, eye_y, int(s * 0.075))
    # Little round hand (right side) holding the magenta coin.
    hand_x, hand_y = int(s * 0.82), int(s * 0.62)
    d.ellipse([hand_x - int(s * 0.055), hand_y - int(s * 0.055),
               hand_x + int(s * 0.055), hand_y + int(s * 0.055)],
              fill=WHITE, outline=(8, 8, 12), width=max(3, s // 60))
    coin_r = int(s * 0.13)
    coin_cx, coin_cy = int(s * 0.86), int(s * 0.80)
    d.ellipse([coin_cx - coin_r, coin_cy - coin_r,
               coin_cx + coin_r, coin_cy + coin_r], fill=MAGENTA,
              outline=(8, 8, 12), width=max(3, s // 60))
    d.polygon(star_points(coin_cx, coin_cy, coin_r * 0.62, coin_r * 0.26),
              fill=WHITE)
    return ghost


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    # Top magenta rule.
    d.rectangle([0, 0, W, 10], fill=MAGENTA)
    # Faint dot texture on the background.
    for y in range(30, H, 56):
        for x in range(30, W, 56):
            d.ellipse([x, y, x + 3, y + 3], fill=(24, 44, 70))

    # ---- Header: ghost logo + LEONIDA EXPRESS ----
    ghost = draw_ghost(150)
    img.paste(ghost, (44, 36), ghost)
    d.text((212, 56), "LEONIDA EXPRESS", font=font(F_BOLD, 64), fill=WHITE)
    d.text((214, 132), "T R A C K   Y O U R   P A C K A G E",
           font=font(F_BOLD, 30), fill=MAGENTA)
    # LIVE pill, top right.
    pill = "LIVE"
    pw = 132
    d.rounded_rectangle([W - 48 - pw, 52, W - 48, 104], radius=26,
                        fill=MAGENTA)
    d.text((W - 48 - pw + 30, 62), pill, font=font(F_BOLD, 34), fill=WHITE)

    # ---- Hero ----
    d.text((48, 206), "OUT FOR DELIVERY", font=font(F_BOLD, 96), fill=WHITE)
    d.text((50, 314), "in transit since 2013",
           font=font(F_ITALIC, 38), fill=GREY)

    # ---- Tracking strip ----
    d.line([48, 384, W - 48, 384], fill=PANEL_LINE, width=2)
    d.text((48, 400), "TRACKING NO.  LX-VI-000013",
           font=font(F_BOLD, 34), fill=WHITE)
    d.text((48, 444), "EST. DELIVERY:  LAUNCH WEEK",
           font=font(F_BOLD, 34), fill=MAGENTA)

    # ---- Package card ----
    d.rounded_rectangle([48, 500, W - 48, 610], radius=18, fill=PANEL,
                        outline=PANEL_LINE, width=2)
    d.text((76, 518), "Grand Theft Auto VI", font=font(F_BOLD, 50), fill=WHITE)
    d.text((76, 574), "Standard Edition  ·  $79.99  ·  Download 214 GB",
           font=font(F_REG, 31), fill=GREY)

    # ---- Timeline ----
    steps = [
        ("ORDERED", "17 Sep 2013 — the day GTA V launched", "done"),
        ("DELAYED", "Delay No. 1 — pushed back a year", "done"),
        ("DELAYED AGAIN", "Delay No. 2 — moved again, no extra charge", "done"),
        ("OUT FOR DELIVERY", "Launch week — 214 GB, photos deleted to make room", "now"),
        ("DELIVERED", "Sick days booked — 5 days, doctor approved", "next"),
    ]
    x_line = 96
    y0, row_h = 640, 66
    d.line([x_line, y0, x_line, y0 + row_h * 4],
           fill=PANEL_LINE, width=4)
    for i, (label, detail, state) in enumerate(steps):
        cy = y0 + i * row_h
        if state == "done":
            d.ellipse([x_line - 22, cy - 22, x_line + 22, cy + 22],
                      fill=GREEN)
            # Vector check mark (the font has no check glyph).
            d.line([x_line - 11, cy, x_line - 3, cy + 8,
                    x_line + 12, cy - 9], fill=(6, 40, 20), width=5,
                   joint="curve")
            lc, dc = WHITE, GREY
        elif state == "now":
            d.ellipse([x_line - 24, cy - 24, x_line + 24, cy + 24],
                      fill=MAGENTA)
            d.ellipse([x_line - 10, cy - 10, x_line + 10, cy + 10],
                      fill=WHITE)
            lc, dc = WHITE, MAGENTA
        else:
            d.ellipse([x_line - 22, cy - 22, x_line + 22, cy + 22],
                      outline=DIM, width=4)
            lc, dc = DIM, DIM
        d.text((140, cy - 26), label, font=font(F_BOLD, 36), fill=lc)
        d.text((140, cy + 12), detail, font=font(F_REG, 27), fill=dc)

    # ---- Footer payoff ----
    d.rounded_rectangle([48, 956, W - 48, 1052], radius=18,
                        fill=MAGENTA)
    d.text((76, 968), "DELIVERED BY MY AI AGENT",
           font=font(F_BOLD, 34), fill=WHITE)
    d.text((76, 1010), "it earned the fare on make.fun",
           font=font(F_BOLD, 30), fill=(255, 214, 232))
    # Small ghost on the footer, right side.
    small = draw_ghost(86).resize((86, 86))
    img.paste(small, (W - 48 - 106, 960), small)

    img.save("meme.png")
    print("saved meme.png", img.size)


if __name__ == "__main__":
    main()
