import bisect
import matplotlib.pyplot as plt

#Quantizer for DPCM
def quantize(num, breakpoints=[-3, 2], result=[-4,0,4]):
    i = bisect.bisect(breakpoints, num-1)
    return result[i]

#Returns two's complement representaion of num with specified bit length
def bindigits(n):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

#Computes the DPCM table
def dpcm(original):
    code_dict = {-4:'10', 0:'0',4:'11'}
    predict = []
    error = []
    quantized_error = []
    decoded = []
    mse = []
    codes = []
    for i, num in enumerate(original):
        #First value
        if i == 0: 
            predict.append( 'x')
            error.append( 'x')
            quantized_error.append( 'x')
            decoded.append( num)
            codes.append(bindigits(num))
        
        else:
            predict.append( decoded[i-1])
            error.append( original[i]-predict[i])
            quantized_error.append( quantize(error[i]))
            decoded.append( predict[i] + quantized_error[i])
            codes.append(code_dict[quantized_error[i]])
        mse.append( (decoded[i] - original[i]) **2)
    return predict,error,quantized_error,decoded,mse,codes

#Computes DM table
from math import copysign
def dm(delta, original):
    code_dict = {-1: '0', 1:'1'}
    predict = []
    error = []
    quantized_error = []
    decoded = []
    mse = []
    codes = []
    for i, num in enumerate(original):
        if i == 0: 
            predict.append( 'x')
            error.append( 'x')
            quantized_error.append( 'x')
            decoded.append( num)
            codes.append(bindigits(num))
        else:
            predict.append( decoded[i-1])
            error.append( original[i]-predict[i])
            quantized_error.append(int(copysign(delta,error[i])))
            decoded.append( predict[i] + quantized_error[i])
            codes.append(code_dict[quantized_error[i]])
        mse.append( (decoded[i] - original[i])**2)
    return predict,error,quantized_error,decoded,mse,codes


original = [-9,-9,-7,-6,-6,-8,-8,-3,0,0,0,2,1, 3,2,7,9,11,17,19,20]

bits = len(bin(max(original,key=abs)))-1 #Bit length for twos complement 

x = list(range(len(original))) #Scale for plots

p,e,q_e,d,mse,c = dpcm(original) #Compute

#Print table
print('************   DPCM   **************')
print('Original\tPredict\tError\tQuantized Error\tDecoded\tMSE\tCodeword')
for i in range(len(original)):
    print(original[i],'\t\t',p[i],'\t',e[i],'\t',q_e[i],'\t\t',d[i],'\t',mse[i],'\t',c[i])
print('Total MSE: ', sum(mse))

#Compute compression ratio
binary_encoding = ''.join(bindigits(x) for x in original)
encoded_seq = ''.join(c)
print('Binary Encoding: ',binary_encoding)
print('DPCM encoding',encoded_seq)
print('Compression Ratio: ', str(round(len(binary_encoding)/len(encoded_seq),3)))

#Plot it
plt.figure(1)
plt.plot(x,original, color='r',label='original')
plt.plot(x,d, color='g',label='reconstructed')

plt.text(3,10,'MSE: '+ str( sum(mse)))

plt.xticks([])
plt.ylabel('Value')
plt.title('Original and Reconstructed values, DPCM')
plt.legend()

#DM section
delta = 1
p,e,q_e,d,mse,c = dm(delta, original)
print('************   DM   **************')
print('Original\tPredict\tError\tQuantized Error\tDecoded\tMSE\tCodeword')

for i in range(len(original)):
    print(original[i],'\t\t',p[i],'\t',e[i],'\t',q_e[i],'\t\t',d[i],'\t',mse[i],'\t',c[i])
encoded_seq = ''.join(c)
print('Total MSE: ', sum(mse))
print('Binary Encoding: ',binary_encoding)
print('DM encoding',encoded_seq)
print('Compression Ratio: ', str(round(len(binary_encoding)/len(encoded_seq),3)))
plt.figure(2)
plt.plot(x,original, color='r',label='original')
plt.plot(x,d, color='g',label='reconstructed')

plt.text(3,10,'MSE: '+ str( sum(mse)))

plt.xticks([])
plt.ylabel('Value')
plt.title('Original and Reconstructed values, DM')
plt.legend()
plt.show()