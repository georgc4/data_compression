import numpy as np
import math
CSVData = open("x_data.csv")
x_data = np.loadtxt(CSVData, delimiter="\t")
# x_data -= 128

CSVData = open("88dct.csv")
dct = np.loadtxt(CSVData, delimiter="\t")
dct_t = dct.transpose()

CSVData = open("quant9.csv")
quant = np.loadtxt(CSVData, delimiter="\t")



a_x = np.matmul(dct, x_data)

y = np.matmul(a_x, dct_t)

quant_c = np.round(y/quant)

rows,columns = np.shape(quant_c)

zigzag=[[] for i in range(rows+columns-1)]
 
for i in range(rows):
    for j in range(columns):
        sum=i+j
        if(sum%2 ==0):
 
            #add at beginning
            zigzag[sum].insert(0,quant_c[i][j])
        else:
 
            #add at end of the list
            zigzag[sum].append(quant_c[i][j])
seq = []
for i in zigzag:
    for j in i:
        seq.append(j)
      
print(x_data,dct,a_x,y, seq)

