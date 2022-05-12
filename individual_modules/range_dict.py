import bisect

def boundaries(num, breakpoints=[-3, 2], result=[-4,0,4]):
    i = bisect.bisect(breakpoints, num-1)
    return result[i]
for i in range (-20,20):
    print (i,boundaries(i))

def bindigits(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

print (bindigits(-9, 5))
