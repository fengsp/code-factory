"""
PIL stuff
"""
import os, sys
from PIL import Image


im = Image.open("/Users/fsp/Pictures/yihuan.jpg")
print im.format, im.size, im.mode
print sys.argv[0]
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + '.png'
    print outfile
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "cannot convert", infile


# Create JPEG Thumbnails
size = 128, 128
for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for", infile


# Identify Image Files
for infile in sys.argv[1:]:
    try:
        im = Image.open(infile)
        print infile, im.format, "%dx%d" % im.size, im.mode
    except IOError:
        pass


for infile in sys.argv[1:]:
    try:
        im = Image.open(infile)
        box = (100, 100, 400, 400)
        region = im.crop(box)
        region = region.transpose(Image.ROTATE_180)
        im.paste(region, box)
        fpath, ext = os.path.splitext(infile)
        outfile = fpath + "_rotated" + ext
        im.save(outfile)
    except IOError:
        pass


# Splitting and merging bands
""" something wrong
File "/Library/Python/2.7/site-packages/PIL/Image.py", line 1497, in split
    if self.im.bands == 1:
    AttributeError: 'NoneType' object has no attribute 'bands'

From StackOverFlow
With googling I found this comment on SO, stating that PIL is sometimes 'lazy' and 'forgets' to load after opening. So you have to do it like this:
import Image
img = Image.open('IMG_0007.jpg')
img.load()
img.split()
"""
for infile in sys.argv[1:]:
    try:
        im = Image.open(infile)
        im.load()
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
        fpath, ext = os.path.splitext(infile)
        outfile = fpath + "_split_and_merge" + ext
        im.save(outfile)
    except IOError:
        pass


# Rolling an image
def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image
    
    part1path = "/Users/fsp/Pictures/part1.jpg"
    part2path = "/Users/fsp/Pictures/part2.jpg"
    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    # this line of code is needed for part2 is retrieved when it is used
    part1.save(part1path)
    part2.save(part2path)
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image


for infile in sys.argv[1:]:
    fpath, ext = os.path.splitext(infile)
    outfile = fpath + "_roll" + ext
    try:
        image = Image.open(infile)
        roll(image, 512)
        image.save(outfile)
    except IOError:
        pass


"""
import Image
im = Image.open("animation.gif")
im.seek(1)
try:
    while 1:
        im.seek(im.tell()+1)
except EOFError:
    pass

class ImageSequence:
    def __init__(self, im):
        self.im = im
    def __getitem__(self, ix):
        try:
            if ix:
                self.im.seek(ix)
            return self.im
        except EOFError:
            raise IndexError

for frame in ImageSequence(im):
    # do something
"""



