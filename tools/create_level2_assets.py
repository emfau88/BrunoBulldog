from pathlib import Path
from PIL import Image, ImageDraw


OUT = Path("assets/props")
OUT.mkdir(parents=True, exist_ok=True)


SCALE = 4
SIZE = 128


def canvas():
    return Image.new("RGBA", (SIZE * SCALE, SIZE * SCALE), (0, 0, 0, 0))


def save(img, name):
    img = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    img.save(OUT / name)


def shadow(draw, cx, cy, rx, ry):
    draw.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=(45, 32, 23, 54))


def rounded(draw, box, r, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def cat():
    img = canvas()
    d = ImageDraw.Draw(img)
    shadow(d, 64 * SCALE, 91 * SCALE, 30 * SCALE, 9 * SCALE)
    p = SCALE
    # Tail behind body.
    d.line([(82*p, 68*p), (102*p, 54*p), (105*p, 39*p)], fill=(52, 53, 58, 255), width=9*p)
    d.line([(82*p, 68*p), (102*p, 54*p), (105*p, 39*p)], fill=(83, 84, 91, 255), width=5*p)
    # Body and head.
    d.ellipse((38*p, 49*p, 90*p, 94*p), fill=(62, 63, 69, 255), outline=(39, 35, 34, 255), width=2*p)
    d.ellipse((36*p, 24*p, 92*p, 70*p), fill=(74, 75, 82, 255), outline=(39, 35, 34, 255), width=2*p)
    # Ears.
    d.polygon([(43*p, 31*p), (49*p, 11*p), (59*p, 33*p)], fill=(69, 70, 77, 255), outline=(39, 35, 34, 255))
    d.polygon([(85*p, 31*p), (79*p, 11*p), (69*p, 33*p)], fill=(69, 70, 77, 255), outline=(39, 35, 34, 255))
    d.polygon([(48*p, 29*p), (50*p, 20*p), (55*p, 31*p)], fill=(222, 141, 145, 255))
    d.polygon([(80*p, 29*p), (78*p, 20*p), (73*p, 31*p)], fill=(222, 141, 145, 255))
    # White muzzle/chest.
    d.ellipse((50*p, 45*p, 78*p, 66*p), fill=(235, 228, 209, 255))
    d.ellipse((54*p, 64*p, 75*p, 91*p), fill=(235, 228, 209, 230))
    # Face.
    d.ellipse((49*p, 39*p, 55*p, 45*p), fill=(245, 217, 86, 255))
    d.ellipse((73*p, 39*p, 79*p, 45*p), fill=(245, 217, 86, 255))
    d.rectangle((51*p, 41*p, 54*p, 45*p), fill=(37, 31, 31, 255))
    d.rectangle((75*p, 41*p, 78*p, 45*p), fill=(37, 31, 31, 255))
    d.polygon([(64*p, 50*p), (59*p, 55*p), (69*p, 55*p)], fill=(48, 34, 34, 255))
    d.line([(54*p, 57*p), (38*p, 53*p)], fill=(60, 45, 40, 255), width=1*p)
    d.line([(54*p, 60*p), (39*p, 62*p)], fill=(60, 45, 40, 255), width=1*p)
    d.line([(74*p, 57*p), (90*p, 53*p)], fill=(60, 45, 40, 255), width=1*p)
    d.line([(74*p, 60*p), (89*p, 62*p)], fill=(60, 45, 40, 255), width=1*p)
    # Paws.
    d.ellipse((42*p, 86*p, 55*p, 99*p), fill=(235, 228, 209, 255))
    d.ellipse((73*p, 86*p, 86*p, 99*p), fill=(235, 228, 209, 255))
    save(img, "cat-blocker.png")


def fish():
    img = canvas()
    d = ImageDraw.Draw(img)
    p = SCALE
    shadow(d, 64*p, 82*p, 30*p, 7*p)
    d.ellipse((32*p, 48*p, 91*p, 78*p), fill=(91, 163, 190, 255), outline=(42, 91, 115, 255), width=2*p)
    d.polygon([(88*p, 63*p), (111*p, 45*p), (107*p, 63*p), (111*p, 81*p)], fill=(66, 134, 166, 255), outline=(42, 91, 115, 255))
    d.polygon([(50*p, 48*p), (63*p, 32*p), (69*p, 52*p)], fill=(105, 180, 204, 255), outline=(42, 91, 115, 255))
    d.polygon([(55*p, 77*p), (67*p, 94*p), (72*p, 75*p)], fill=(71, 139, 166, 255), outline=(42, 91, 115, 255))
    d.ellipse((41*p, 57*p, 48*p, 64*p), fill=(30, 34, 39, 255))
    d.arc((32*p, 53*p, 52*p, 73*p), 115, 245, fill=(231, 241, 235, 255), width=2*p)
    for x in (59, 69, 79):
        d.arc((x*p, 52*p, (x+12)*p, 76*p), 105, 255, fill=(51, 105, 128, 180), width=1*p)
    save(img, "fish-treat.png")


def box():
    img = canvas()
    d = ImageDraw.Draw(img)
    p = SCALE
    shadow(d, 64*p, 91*p, 34*p, 9*p)
    d.polygon([(27*p, 43*p), (64*p, 28*p), (101*p, 43*p), (64*p, 58*p)], fill=(213, 154, 83, 255), outline=(103, 68, 40, 255))
    d.polygon([(27*p, 43*p), (64*p, 58*p), (64*p, 98*p), (27*p, 78*p)], fill=(177, 116, 65, 255), outline=(103, 68, 40, 255))
    d.polygon([(101*p, 43*p), (64*p, 58*p), (64*p, 98*p), (101*p, 78*p)], fill=(194, 130, 71, 255), outline=(103, 68, 40, 255))
    d.polygon([(27*p, 43*p), (47*p, 22*p), (64*p, 28*p), (45*p, 51*p)], fill=(224, 166, 96, 255), outline=(103, 68, 40, 255))
    d.polygon([(101*p, 43*p), (81*p, 22*p), (64*p, 28*p), (83*p, 51*p)], fill=(224, 166, 96, 255), outline=(103, 68, 40, 255))
    d.line([(64*p, 58*p), (64*p, 97*p)], fill=(106, 70, 42, 255), width=2*p)
    d.line([(40*p, 61*p), (52*p, 68*p)], fill=(135, 86, 50, 255), width=2*p)
    d.line([(80*p, 63*p), (91*p, 57*p)], fill=(135, 86, 50, 255), width=2*p)
    save(img, "cardboard-box.png")


def bell():
    img = canvas()
    d = ImageDraw.Draw(img)
    p = SCALE
    shadow(d, 64*p, 90*p, 24*p, 7*p)
    d.line([(43*p, 73*p), (30*p, 85*p)], fill=(108, 70, 43, 255), width=5*p)
    d.line([(85*p, 73*p), (98*p, 85*p)], fill=(108, 70, 43, 255), width=5*p)
    d.ellipse((36*p, 33*p, 92*p, 86*p), fill=(235, 190, 68, 255), outline=(128, 82, 38, 255), width=3*p)
    d.rectangle((38*p, 63*p, 90*p, 83*p), fill=(237, 180, 55, 255))
    d.arc((36*p, 33*p, 92*p, 86*p), 185, 355, fill=(255, 226, 111, 255), width=4*p)
    d.ellipse((56*p, 75*p, 72*p, 92*p), fill=(125, 77, 36, 255), outline=(80, 52, 33, 255), width=1*p)
    d.rectangle((57*p, 22*p, 71*p, 37*p), fill=(214, 158, 57, 255), outline=(128, 82, 38, 255), width=2*p)
    d.arc((50*p, 16*p, 78*p, 43*p), 205, 335, fill=(128, 82, 38, 255), width=4*p)
    save(img, "bell-toy.png")


def cat_meeting():
    img = canvas()
    d = ImageDraw.Draw(img)
    p = SCALE
    shadow(d, 64*p, 89*p, 36*p, 8*p)
    d.ellipse((35*p, 49*p, 93*p, 93*p), fill=(231, 209, 147, 255), outline=(122, 82, 45, 255), width=2*p)
    d.ellipse((44*p, 56*p, 58*p, 70*p), fill=(68, 70, 76, 255))
    d.ellipse((68*p, 54*p, 83*p, 69*p), fill=(178, 119, 74, 255))
    d.ellipse((55*p, 69*p, 72*p, 85*p), fill=(238, 232, 214, 255))
    d.rectangle((30*p, 82*p, 98*p, 91*p), fill=(172, 113, 62, 255))
    d.line([(39*p, 83*p), (39*p, 92*p)], fill=(105, 68, 41, 255), width=2*p)
    d.line([(64*p, 83*p), (64*p, 92*p)], fill=(105, 68, 41, 255), width=2*p)
    d.line([(89*p, 83*p), (89*p, 92*p)], fill=(105, 68, 41, 255), width=2*p)
    save(img, "cat-meeting.png")


cat()
fish()
box()
bell()
cat_meeting()
print("created level 2 assets")
