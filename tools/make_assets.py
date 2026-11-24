#!/usr/bin/env python3
"""브라보실버 대표 이미지(og-image.png) 생성 스크립트."""
from PIL import Image, ImageDraw, ImageFont

GREEN = (29, 77, 59)
GREEN_900 = (16, 40, 31)
IVORY = (250, 247, 242)
AMBER = (217, 130, 43)
AMBER_SOFT = (251, 239, 224)

FONT = "/usr/share/fonts/pickle-hwp/NotoSansCJKkr-Regular.otf"
W, H = 1200, 630


def font(size):
    return ImageFont.truetype(FONT, size)


def text(draw, xy, s, size, fill, anchor="la", bold=False):
    f = font(size)
    if bold:
        # stroke 로 굵기 표현
        draw.text(xy, s, font=f, fill=fill, anchor=anchor, stroke_width=max(1, size // 34), stroke_fill=fill)
    else:
        draw.text(xy, s, font=f, fill=fill, anchor=anchor)


img = Image.new("RGB", (W, H), GREEN)
d = ImageDraw.Draw(img, "RGBA")

# --- 배경: 오른쪽 아래로 짙어지는 그라데이션 ---
grad = Image.new("L", (W, H), 0)
gd = ImageDraw.Draw(grad)
for y in range(H):
    gd.line([(0, y), (W, y)], fill=int(120 * (y / H) ** 1.4))
img.paste(Image.new("RGB", (W, H), GREEN_900), (0, 0), grad)

# --- 장식 원 ---
d.ellipse([880, -180, 1420, 360], fill=(250, 247, 242, 14))
d.ellipse([960, 250, 1320, 610], outline=(250, 247, 242, 26), width=2)
d.ellipse([-140, 430, 240, 810], outline=(250, 247, 242, 20), width=2)

# --- 좌측 액센트 바 ---
d.rounded_rectangle([72, 96, 82, 534], radius=5, fill=AMBER)

# --- 브랜드 마크 (둥근 사각형 + 하트) ---
mx, my, ms = 132, 96, 96
d.rounded_rectangle([mx, my, mx + ms, my + ms], radius=28, fill=IVORY)
cx, cy = mx + ms / 2, my + ms / 2
d.pieslice([cx - 26, cy - 20, cx, cy + 6], 180, 360, fill=AMBER)
d.pieslice([cx, cy - 20, cx + 26, cy + 6], 180, 360, fill=AMBER)
d.polygon([(cx - 26, cy - 4), (cx + 26, cy - 4), (cx, cy + 30)], fill=AMBER)

# --- 텍스트 ---
text(d, (132, 236), "시니어 맞춤형 수업 전문교육기관", 30, AMBER, bold=True)
text(d, (128, 282), "브라보실버", 96, IVORY, bold=True)
text(d, (132, 418), "주간보호센터 · 요양시설 · 복지관 · 경로당 출강", 40, IVORY)
text(d, (132, 476), "찾아가는 강사 파견 · 무료공연 · 생일상·현수막 무료 대여", 30, AMBER_SOFT)

# --- 하단 구분선 + 전화번호 ---
d.line([(132, 544), (1068, 544)], fill=(250, 247, 242, 60), width=2)
text(d, (132, 560), "상담 010-3287-1007", 34, IVORY, bold=True)
text(d, (1068, 568), "hbs652927-cmyk.github.io/bravo-silver", 24, (250, 247, 242, 150), anchor="ra")

img.save("/workspace/bravo-silver/og-image.png", optimize=True)
print("saved og-image.png", img.size)
