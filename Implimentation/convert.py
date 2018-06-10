#python

from PIL import Image

img = Image.open("stego06_0512.png")

pixels = list(img.getdata())

print len(pixels)**.5

#for i in pixels:
#	print i
