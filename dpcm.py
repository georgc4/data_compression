def dpcm(quantizer, original):
    predict = []
    error = []
    quantized_error = []
    decoded = []
    mse = []

    for i, num in enumerate(original):
        if i == 0: 
            predict.append( 'x')
            error.append( 'x')
            quantized_error.append( 'x')
            decoded.append( num)
            
        else:
            predict.append( decoded[i-1])
            error.append( original[i]-predict[i])
            quantized_error.append( quantizer[error[i]])
            decoded.append( predict[i] + quantized_error[i])
        mse.append( (decoded[i] - original[i]) **2)
    return predict,error,quantized_error,decoded,mse

quantizer = {}
for i in range(-11,-7): quantizer[i] = -9
for i in range(-7, -2): quantizer[i] = -5
for i in range(-2,0): quantizer[i] = -1

for i in range(0,2): quantizer[i] = 1
for i in range(2,7): quantizer[i] = 5
for i in range(7,12): quantizer[i] = 9

original = [2,3,2,7,9,11,6,2]

p,e,q_e,d,mse = dpcm(quantizer, original)
print('Original\tPredict\tError\tQuantized Error\tDecoded\tMSE')

for i in range(len(original)):
    print(original[i],'\t\t',p[i],'\t',e[i],'\t',q_e[i],'\t\t',d[i],'\t',mse[i])

