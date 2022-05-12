def isHuff(c):
    return sum([1/(2**len(i)) for i in c]) ==1
# c = ['01','00', '11','101', '100']
#c = ['1100', '11010', '00','100','110110', '110111', '01', '101']
#print(isHuff(c))
# print(sum([1/(2**len(i)) for i in c]))
# if sum([1/(2**len(i)) for i in c]) != 1: print ("The code is not a Huffman code")
# else: print("The code may be a Huffman code")
