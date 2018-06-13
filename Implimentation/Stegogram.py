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
j = 0
for i in pixels:
    j += 1
    if j % int(sideLength) == 0:
        string += '\n'
	string += "," + str(i)
print string[1:]
