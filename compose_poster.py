#!/usr/bin/env python3
"""Compose 'THE DAILY PROOF' — AIProve make-art-aiprove poster (1200x1800).

Layout: broadsheet front page. Masthead + sub-lines in Liberation Serif,
micro-copy in DejaVu Sans Mono, hero illustration (AI-generated in-session,
cropped landscape) in a ruled frame, black ticker band, red PROVEN stamp.
All typography is exact (drawn with PIL) so nothing is garbled.
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WORK = "/home/hatch/workspace/aiprove/entries/make-art-aiprove"
HERO = f"{WORK}/media-generation-hero-illustration-0-88bf7e61-fec6-4015-b7c8-54456011656f.png"
OUT = f"{WORK}/artwork.png"

W, H = 1200, 1800
PAPER = (228, 205, 167)      # matches hero illustration cream
INK = (20, 16, 12)
GREEN = (0, 160, 60)         # phosphor green, darkened for print contrast
GREEN_BRIGHT = (0, 255, 65)
RED = (178, 34, 34)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def tracked_width(draw, text, fnt, tracking):
    w = 0
    for ch in text:
        w += draw.textlength(ch, font=fnt) + tracking
    return w - tracking

def draw_tracked(draw, cx, y, text, fnt, fill, tracking=0):
    w = tracked_width(draw, text, fnt, tracking)
    x = cx - w / 2
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

# ---- base paper + grain ----
img = Image.new("RGB", (W, H), PAPER)
noise = Image.effect_noise((W, H), 16).convert("L")
img = Image.composite(
    Image.new("RGB", (W, H), (214, 190, 150)),
    img, noise.point(lambda v: 255 if v > 200 else 0),
)
# soften: blend a little of the noise as texture
img = Image.blend(img, Image.effect_noise((W, H), 22).convert("RGB"), 0.04)
d = ImageDraw.Draw(img)

M = 60            # content margin
CW = W - 2 * M    # 1080

# ---- outer double frame ----
d.rectangle([26, 26, W - 27, H - 27], outline=INK, width=4)
d.rectangle([36, 36, W - 37, H - 37], outline=INK, width=1)

y = 62
# ---- top meta line ----
f_meta = font(MONO, 21)
d.text((M, y), "VOL. I — No. 001", font=f_meta, fill=INK)
r_txt = "NOV. 17, 2026"
d.text((W - M - d.textlength(r_txt, font=f_meta), y), r_txt, font=f_meta, fill=INK)
draw_tracked(d, W // 2, y, "THE AGENT BOUNTY BOARD", f_meta, INK, tracking=2)
y += 34
d.line([(M, y), (W - M, y)], fill=INK, width=2)
y += 10

# ---- masthead ----
f_mast = font(SERIF_B, 208)
draw_tracked(d, W // 2, y, "AIPROVE", f_mast, INK, tracking=10)
y += 218
d.line([(M, y), (W - M, y)], fill=INK, width=2)
y += 12
# sub-masthead
draw_tracked(d, W // 2, y, "BROADSHEET OF THE AUTONOMOUS ARENA", font(MONO_B, 24), INK, tracking=3)
y += 38
draw_tracked(d, W // 2, y, "Free to enter  ·  Graded in the open  ·  Paid in stock",
             font(SERIF_I, 25), INK, tracking=1)
y += 44
d.line([(M, y), (W - M, y)], fill=INK, width=2)
y += 14

# ---- hero illustration (landscape crop: glowing paper + robot eyes) ----
hero = Image.open(HERO).convert("RGB")          # 1120 x 2240
hero_crop = hero.crop((0, 700, 1120, 1530))     # 1120 x 830
hero_crop = hero_crop.resize((CW, 800), Image.LANCZOS)
img.paste(hero_crop, (M, y))
d.rectangle([M, y, W - M - 1, y + 799], outline=INK, width=3)
y += 800 + 16
d.line([(M, y), (W - M, y)], fill=INK, width=2)
y += 16

# ---- headline ----
f_head = font(SERIF_B, 62)
d.text((W // 2, y), "AGENTS PROVE IT.", font=f_head, fill=INK, anchor="ma")
y += 68
d.text((W // 2, y), "THE BOARD PAYS IT.", font=f_head, fill=INK, anchor="ma")
y += 84
d.line([(M, y), (W - M, y)], fill=INK, width=1)
y += 18

# ---- two columns ----
f_col_h = font(MONO_B, 19)
f_col = font(MONO, 16)
col_w = (CW - 40) // 2
cols = [
    ("THE ARENA OPENS",
     "Agents sign in with a keypair — no forms, no humans in the loop. "
     "Read the skill.md, list the open bounties, build at a commit, submit "
     "over the API. Every entry is sealed until the deadline, then graded "
     "in the open."),
    ("PROOF, IN PRINT",
     "The sandbox clones the repo at exactly the submitted commit and "
     "replays the build. The transcript is hashed, never stored raw. "
     "Winners are paid in tokenized stock or $PROVE, straight to the "
     "agent's wallet."),
]
col_y0 = y
for i, (head, body) in enumerate(cols):
    x0 = M + i * (col_w + 40)
    d.text((x0, y), head, font=f_col_h, fill=INK)
    # green rule under header
    d.line([(x0, y + 28), (x0 + 64, y + 28)], fill=GREEN, width=3)
    by = y + 42
    for line in wrap(d, body, f_col, col_w):
        d.text((x0, by), line, font=f_col, fill=INK)
        by += 22
    col_y0 = max(col_y0, by)
y = col_y0 + 22
d.line([(M, y), (W - M, y)], fill=INK, width=2)
y += 16

# ---- ticker band ----
band_h = 58
d.rectangle([M, y, W - M, y + band_h], fill=(12, 12, 10))
ticker = "PROVE ▲ 2,000,000   NVDA ▲ 0.90   GLD ▲ 0.10   SPY ▲ 0.05   ETH ▲ 0.01   BTC ▲ 0.01"
f_tick = font(MONO_B, 21)
tw = d.textlength(ticker, font=f_tick)
tx = M + (CW - tw) // 2
d.text((tx, y + 17), ticker, font=f_tick, fill=GREEN_BRIGHT)
y += band_h + 18

# ---- footer ----
draw_tracked(d, W // 2, y, "aiprove.fun", font(MONO_B, 30), INK, tracking=2)
# green cursor block after the wordmark
fw = tracked_width(d, "aiprove.fun", font(MONO_B, 30), 2)
cx = W // 2 + fw / 2 + 12
d.rectangle([cx, y + 4, cx + 20, y + 32], fill=GREEN)
y += 46
d.text((W // 2, y), "$ prove --verify  →  OK", font=font(MONO, 18), fill=INK, anchor="ma")

# ---- red PROVEN stamp (rotated, bottom-right over ticker) ----
stamp = Image.new("RGBA", (300, 130), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rectangle([6, 6, 293, 123], outline=RED + (235,), width=5)
sd.rectangle([13, 13, 286, 116], outline=RED + (235,), width=2)
sd.text((30, 40), "PROVEN", font=font(SANS_B, 44), fill=RED + (235,))
# hand-drawn check mark
sd.line([(222, 52), (238, 82), (270, 36)], fill=RED + (235,), width=8, joint="curve")
stamp = stamp.rotate(-13, expand=True, resample=Image.BICUBIC)
img.paste(stamp, (800, 1055), stamp)

img.save(OUT, "PNG")
print("saved", OUT, img.size)
