import math
def unary(num):
    return '1'*num + '0'

def isPowerOfTwo(num):
    return (math.ceil(math.log2(num) == math.floor(math.log2(num))))

def golomb(n,m):
    q = math.floor(n/m)
    r = n - q*m
    codeword = unary(q)
    if isPowerOfTwo(m):
        b = str(int(math.log2(m)))
        codeword = codeword + format(r,'0'+b+'b')
    else:
        b = math.floor(math.log2(m))
        if r < ((2**(b+1)) - m):
            codeword = codeword + format(r,'0'+str(b)+'b')
        else:
            r = r + (2**(b+1)) - m
            codeword = codeword + format(r,'0'+str(b+1)+'b')
    return codeword
m = 8
alphabet = [16,24,32]
probs = [0.6, 0.3, 0.1]
dictionary = dict()
for i in range(len(alphabet)):
    dictionary[golomb(alphabet[i],m)] = probs[i]
averageLength = 0
for word in dictionary:
    averageLength += len(word)* dictionary[word]
print("Golomb")
for letter in alphabet:
    print(str(letter) + ': ' + golomb(letter,m))    
print("Average Length = " + str(round(averageLength,2)))
