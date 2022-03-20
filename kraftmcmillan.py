
c = ['0','111','111','1','11','11']
print([len(i)for i in c])
if sum([1/(2**len(i)) for i in c]) <= 1: print ("Kraft-McMillan inequality holds")
else: print("Kraft-McMillan inequality does not hold")
