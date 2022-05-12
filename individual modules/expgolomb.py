import math
def remap(num):
    if num <=0:
        return 2*abs(num)
    else:
        return 2*num -1
def expgolomb(num, signed=False):
    if signed: num = remap(num)
    if num == 0: return '1' 
    m = math.floor(math.log2(num+1))
    info = num + 1 - 2**m
    codeword = '0'*m + '1' + format(info, '0'+str(m)+'b')
    return codeword

#print(expgolomb(-7,True))

alphabet = [16,24,32]
probs = [0.6, 0.3, 0.1]
dictionary = dict()
for i in range(len(alphabet)):
    dictionary[expgolomb(alphabet[i],False)] = probs[i]
averageLength = 0
for word in dictionary:
    averageLength += len(word)* dictionary[word]
print("EXP Golomb")
for letter in alphabet:
    print(str(letter) + ': ' + expgolomb(letter,False))    
print("Average Length = " + str(round(averageLength,2)))