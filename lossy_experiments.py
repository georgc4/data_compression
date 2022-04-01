from PIL import Image
from intervaltree import Interval, IntervalTree
import csv
import numpy as np
def quantize2(im):
    rd = IntervalTree()
    # rd[0:64] = 32
    # rd[64:128] = 96
    # rd[128:196] = 160
    # rd[196:256] = 224
    rd[0:128] = 64
    rd[128:256] = 196
    print(rd[0].pop().data)
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            im[x,y] = rd[im[x,y]].pop().data
            
    return im           

# print( rd[65].pop().data)

im = Image.open('lena.jpg')
grayIm = im.convert('L')
grayImArr = np.array(grayIm)
twobitGray = Image.fromarray(quantize2(grayImArr))


twobitGray.show() 
