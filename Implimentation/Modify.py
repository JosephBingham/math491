import re
buff = None
with open('Pixels.csv','r') as pf:
    buff = pf.read()

raw_lines = buff.split('\n')

img_size = int(raw_lines[0].strip())

pixels = raw_lines[2:]

for i in xrange(len(pixels) - 1):
    pixels[i] = pixels[i][1:]
    pixels[i] = [x for x in pixels[i].split(',')] 
    for j in xrange(len(pixels[i])):
        try:
            pixels[i][j] = int(pixels[i][j])
        except:
            print  i, j

pixels = pixels[:-1:]

pixel_string = '{'

for i in pixels:
    pixel_string += '{' + str(i)[1:-1] + '},'

pixel_string = pixel_string[:-1] + '};'
new_file = open('Stego.cpp', 'w+')
if not new_file:
    print 'oops'
with open('Stegogram.cpp', 'r+') as code:
    for line in code:
        if '/****/' in line:
            new_file.write(line[:-7] + str(img_size)  + '\n')
        elif '/*****/' in line:
#            print line[:-8] + pixel_string
            new_file.write(line[:-9] + pixel_string + '\n')
        else:
            new_file.write(line)

new_file.close()
