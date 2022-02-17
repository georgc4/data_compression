import math
#node class definition
class Node:
    def __init__(self, prob, symbol, left = None, right = None):
        self.prob = prob

        self.symbol = symbol

        self.left = left
        
        self.right = right

        self.code = ''

#sort nodes in descending order, putting combined nodes first in case of same probability
def sortCodebook(codebook):
     # getting length of list of codebook
    lst = len(codebook) 
    for i in range(0, lst): 
          
        for j in range(0, lst-i-1): 

            #descending order
            if (codebook[j].prob < codebook[j + 1].prob): 
                temp = codebook[j] 
                codebook[j]= codebook[j + 1] 
                codebook[j + 1]= temp 
            
            #same probability case
            if (codebook[j].prob == codebook[j + 1].prob and len(codebook[j].symbol) < len(codebook[j+1].symbol)):
                temp = codebook[j] 
                codebook[j]= codebook[j + 1] 
                codebook[j + 1]= temp
    return codebook 

codes = dict()
def makeCodes(node, val=''):
    #Create codewords as a dictionary by traversing binary tree
    
    #append 1 or 0 depending on which way we went
    newVal = val + str(node.code)

    #traversing
    if(node.left):
        print(node.symbol + ': Up (1)') 
        makeCodes(node.left, newVal)
    if(node.right):
        print(node.symbol + ': Down (0)')
        makeCodes(node.right, newVal)
    #base case where we've reached a leaf   
    if(not node.left and not node.right):
        codes[node.symbol] = newVal
        print(node.symbol + ': ' + newVal +'\n')
    return codes

#create the tree
def ConstructHuffmanTree(symbols):
    nodes = []
    for i in range(len(symbols)):
        nodes.append(Node(symbols[i][1], symbols[i][0]))
    #construct binary tree
    while len(nodes) >1:

        #sort the list
        nodes = sortCodebook(nodes)

        #show steps
        for i in range(len(nodes)):
            print(nodes[i].symbol + ': ' + str(nodes[i].prob))
        print()

        #choose smallest two probabilities
        right = nodes[len(nodes)-1]
        left = nodes[len(nodes)-2]

        #assign codes to branches
        right.code = '0'
        left.code = '1'

        #make a new node of the combined two
        newNode = Node(round(left.prob+right.prob, 4), left.symbol+right.symbol, left, right)

        #replace the smallest two with the new combined one
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

        #repeat until we have one root node

    print(nodes[0].symbol + ': ' + str(nodes[0].prob) + '\n')
    makeCodes(nodes[0])    




################################################################
## 'Main' function
## Edit symbols list and run to get huffman encoding and relevant statistics


#symbols = [('a1',0.4), ('a2',0.2), ('a3',0.2), ('a4',0.1), ('a5',0.1)] #Example from modules
symbols = [('a', 0.4), ('b', 0.2), ('c',0.1), ('d', 0.1), ('e', 0.09), ('f',0.09), ('g', 0.01), ('h', 0.01)]
ConstructHuffmanTree(symbols)


H = round(-sum(symbols[i][1] * math.log(symbols[i][1],2) for i in range(len(symbols))),4)
Lav = round(sum(symbols[i][1]*len(codes.get(symbols[i][0])) for i in range(len(symbols))),4)
Var = round(sum(symbols[i][1]* (len(codes.get(symbols[i][0]))-Lav)**2 for i in range(len(symbols))),4)
R = round(abs(H-Lav),4)

print()
print('Codebook: ' + str(codes))
print('Entropy: ' + str(H))
print('Average Length ' + str(Lav))
print('Variance: ' +str(Var))
print('Redundancy: ' +str(R))