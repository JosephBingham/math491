#python

from PIL import Image

img = Image.open("stego06_0512.png")

pixels = list(img.getdata())

sideLength =  len(pixels)**.5

if sideLength != int(sideLength):
	raise Exception('THIS IS NOT A SQUARE, WHAT DO I DO WITH THIS??')

print int(sideLength)

print

string = ""

for i in pixels:
	string += "," + str(i)
print string[1:]
