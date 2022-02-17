from bitarray import bitarray
from isHuff import *
# code = {
#     '01' : 'a1', 
#     '11' : 'a2', 
#     '00' : 'a3', 
#     '101': 'a4', 
#     '100': 'a5' 
#}
code = {
    '1' : bitarray('01'),
    '2' : bitarray('11'),
    '3' : bitarray('00'),
    '4' : bitarray('101'),
    '5' : bitarray('100')
}

if isHuff(code): print("The code is a Huffman code")
a = bitarray()
a.encode(code, '3123334531233345')
print(a)
dec = bitarray('000111000000101100000111000000101100').decode(code)
dec_error = bitarray('100111000000101100000111000000101100').decode(code)
print(dec)
print(dec_error)
