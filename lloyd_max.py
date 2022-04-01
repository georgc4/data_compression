from PIL import Image
from intervaltree import Interval, IntervalTree
import csv
import matplotlib.pyplot as plt
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

# im = Image.open('lena.jpg')
# grayIm = im.convert('L')
# grayImArr = np.array(grayIm)
# twobitGray = Image.fromarray(quantize2(grayImArr))


# twobitGray.show()
# 
# 
#  
def calc_distortion(pdf,x,y,M):
    distortion = 0
    X = min(pdf)
    for i in range(1,M+1):
        for j in range(x[i-1], x[i]):
            distortion += (X-y[i-1])**2 *pdf[X]
            X+=1
    # i = M
    # distortion += (X-y[i-1])**2 *pdf[X]
    return distortion      
        
def uniformQuantize(pdf,y_i,M):
    X_max = max(pdf)
    stepSize = int(2 * X_max / M)
    b = min(pdf)
    x = []
    y = y_i
    rd = IntervalTree()
    for i in range(M-1):
        
        rd[b:b+stepSize] = y[i]
        x.append(b)
        b += stepSize
    rd[b:b+stepSize+1] = max(y)
    x.append(b)
    x.append(max(pdf))
    y.append(max(y))
    return x,y

def lloydMax(pdf,x,y,M,epsilon):
    distortion = 0
    numerator = 0
    denominator =0 
    distortion = calc_distortion(pdf,x,y,M)
    print('Initial distortion: ' +str(distortion))
    iteration = 0
    print('b{'+str(iteration)+'} = ' +str(x))
    print('y{'+str(iteration)+'} = ' +str(y[:-1]))
    print()
    while True:
        iteration +=1
        print("Iteration: " + str(iteration))
        new_y = []
        new_x = []
        #Calculate b(i)
        new_x.append(x[0])
        for i in range(1,M):
            new_x.append(round((y[i]+y[i-1])/2))
        new_x.append(max(pdf))
        #Calculate y(i)
        X = min(pdf)
        for i in range(1,M+1):
            numerator = 0
            denominator = 0
            for j in range(x[i-1], x[i]):
                numerator += X *pdf[X]
                denominator += pdf[X]
                X+=1
            if X == max(pdf):
                numerator += X *pdf[X]
                denominator += pdf[X]
            new_y.append(round(numerator/denominator))
        new_y.append(round(numerator/denominator))
        newDist = calc_distortion(pdf,new_x,new_y,M)
        if abs(newDist-distortion) <= epsilon:
            print('Terminating iterations: \u0394Distortion = ' + str(abs(newDist-distortion)))
            print('b{'+str(iteration)+'} = ' +str(new_x))
            print('y{'+str(iteration)+'} = ' +str(new_y[:-1]))
            print()
            break
        else:
            x,y = new_x,new_y
            distortion = newDist
            print('b{'+str(iteration)+'} = ' +str(new_x))
            print('y{'+str(iteration)+'} = ' +str(new_y[:-1]))
            print('distortion = ' +str(distortion))
            print()
    # while True:
    #     X = min(pdf)
    #     for i in range(1,M+1):
    #         for j in range(x[i-1], x[i]):
    #             numerator += X *pdf[X]
    #             denominator += pdf[X]
    #             X+=1
    #         new_y.append(numerator/denominator)
    #         new_x.append(int((new_y[i]+new_y[i-1])/2))
    #     new_distortion = calc_distortion(pdf,new_x,new_y,M) 
    #     if abs(new_distortion-distortion) <= 0.00001:
    #         break
    #     distortion = new_distortion
    #     x,y = new_x, new_y

    if(M%2 == 1): new_y[int(M/2)] = 0
    print('Final b values: ' +str(new_x))
    print('Final y values: ' +str(new_y[:-1]))
    print('Final distortion: ' +str(distortion))
    return new_x,new_y


        
        


#part a
# M=3
# y_i = [-10, 0, 10]

#part b
M=4
y_i = [-9,-6,3,11]

with open('HW_7.csv') as infile:
    reader = csv.reader(infile)
    pdf = {int(rows[0]):float(rows[1]) for rows in reader}

x,y = uniformQuantize(pdf,y_i,M)
plt.figure(1)
plt.title('Uniform Quantization')
plt.step(x,y,where='post')
# x,y = [-11,-4,4,11],[-8,0,7,7]

epsilon = 0.00001
plt.figure(2)
plt.title('Lloyd-Max Quantization')
x,y = lloydMax(pdf,x,y,M,epsilon)

plt.step(x,y, where='post')

plt.figure(3)
x,y = list(pdf.keys()), list(pdf.values())
plt.plot(x,y)
plt.title('PDF')
plt.show()