from PIL import Image
from intervaltree import Interval, IntervalTree
import csv
import matplotlib.pyplot as plt
import numpy as np

def calc_distortion(pdf,x,y,M):
    distortion = 0
    X = min(pdf)
    for i in range(1,M+1):
        for j in range(x[i-1], x[i]):
            distortion += (X-y[i-1])**2 *pdf[X]
            X+=1
  
    return distortion      
        

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def uniform_quantize(pdf,M):
    x=[]
    x.append(min(pdf.keys()))
    for i in range(M):
        x.append(list(split(list(pdf.keys()),M))[i][-1])

    return x

def centroid(pdf,y,M):
    x = []
    x.append(min(pdf.keys()))
    for i in range(1,M):
        x.append(round((y[i]+y[i-1])/2))
    x.append(max(pdf)+1)
    return x


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
        new_x.append(max(pdf)+1)
        x= new_x
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
y_i = [-9,-3,3,9]

with open('HW_7.csv') as infile:
    reader = csv.reader(infile)
    pdf = {int(rows[0]):float(rows[1]) for rows in reader}

x=uniform_quantize(pdf,M)

x=centroid(pdf,y_i,M)

y = y_i
y.append(max(y))



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