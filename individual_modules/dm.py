from math import copysign
def dm(delta, original):
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
            quantized_error.append(copysign(delta,error[i]))
            decoded.append( predict[i] + quantized_error[i])
        mse.append( (decoded[i] - original[i])**2)
    return predict,error,quantized_error,decoded,mse


delta = 2
original = [2,3,2,7,9,11,6,2]

p,e,q_e,d,mse = dm(delta, original)
print('Original\tPredict\tError\tQuantized Error\tDecoded\tMSE')

for i in range(len(original)):
    print(original[i],'\t\t',p[i],'\t',e[i],'\t',q_e[i],'\t\t',d[i],'\t',mse[i])

