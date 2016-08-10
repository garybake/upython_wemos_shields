import numpy as np
import Image
import sys

"""
Converts a png image to an array.
Requires numpy
"""

# 1bit-logo.png was taken from the micropython repo
# https://github.com/micropython/micropython/tree/master/logo
img = Image.open('1bit-logo.png').convert('RGBA')  # Red, Green, Blue, Alpha
arr = np.array(img)

# record the original shape
# shape = arr.shape  # 48px x 48px x 4rgba

pic = []
# Remove the alpha an reduce to 1s and 0s
for row in arr:
    out_row = []
    for pixel in row:
        val = 0
        if pixel[0] > 0:
            val = 1
        out_row.append(val)
    pic.append(out_row)

# I couldn't paste the whole array of arrays into upython 
# so here we compress to use a single array with a string.
# TODO we can probably reduce this further to a 48bit value
pic_out = []
for x, row in enumerate(pic):
    col_str = ''
    for y, col in enumerate(row):
        col_str += str(str(col))
    pic_out.append(col_str)

# Pretty print
print "pic=["
print ',\n'.join(pic_out)
print "]"     
