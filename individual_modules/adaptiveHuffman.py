class Node:
    #Class definition for nodes
    def __init__(self, number, weight= 0, symbol=None, parent=None, left = None, right = None):
        self.weight = weight

        self.symbol = symbol

        self.number = number

        self.parent = parent

        self.left = left
        
        self.right = right

    def __repr__(self):
        return "Node: " +str(self.number) + " weight: " +str(self.weight) + " symbol: " +str(self.symbol)

COUNT =[15]
def print2DUtil(root, space) :
 
    # Base case
    if (root == None) :
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(str(root.number) + ' (' + str(root.weight) + ') ' + str(root.symbol))
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
def print2D(root) :
     
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)
    print('--------------------------------------------------------------------')


def update(node):
    
    #Finding max node in block
    block = []
    for x in tree:
        if x.weight == node.weight and ((x.symbol is None and node.symbol is None) or (x.symbol is not None and node.symbol is not None)): 
            #print(x)
            block.append(x)
    max_Node = None
    for x in block:
        if max_Node is None or x.number > max_Node.number:
            max_Node = x

    #Swapping node with max node and incrementing        
    #print("Block for: " + str(node) + " is " + str(block) + " and max_Node is " + str(max_Node)) #Uncomment to see the block for each node
    if node is not max_Node:
        node, max_Node = max_Node, node
        #print("After Swapping... max node is " + str(max_Node) + ' and node is ' + str(node))
        node.weight+=1
        node.symbol, max_Node.symbol, = max_Node.symbol, node.symbol
        # max_Node.weight, node.weight = node.weight, max_Node.weight
    else: node.weight+= 1
    
    
    #If not root node, continue with parent node
    if node.parent is not None: update(node.parent)
    return

#Function that creates two new nodes when a letter is not seen
def giveBirth(node, letter):
    if node is None:
        return
    
    if node.symbol == 'NYT':
        node.symbol = None
        node.weight += 1
        node.left = Node(node.number-2, parent=node, symbol='NYT') #New NYT on the left
        node.right = Node(node.number-1, parent=node, symbol=letter, weight = 1) #External node on the right
        tree.extend([node.left, node.right])
        
        if node.parent is not None: update(node.parent)
        return
    else:
        #Recursively finding NYT
        giveBirth(node.left, letter)
        giveBirth(node.right, letter)

#Traverse tree to find path to create codewords
def getCode(letter,root, val=''):
    global encoded_sequence
    if root.left is not None or root.right is not None:
        getCode(letter, root.left, val +'0')
        getCode(letter, root.right, val +'1')


    if letter == root.symbol:
        print("Letter " + letter + " was found. Sending " + val) 
        encoded_sequence += val
    elif root.symbol == 'NYT' and letter not in seen:
        print("Letter " + letter + " was not found. Sending " + val + " for NYT, and " + format(asciiDict[letter], "08b") + " from ASCII dictionary" )
        encoded_sequence += val + format(asciiDict[letter], "08b")

#Send each symbol through the process
def adaptiveHuffman(sequence):
    n = len(set(sequence))
    number = 2*n - 1
    root = Node(number, symbol='NYT')
    tree.append(root)
    
    for letter in sequence:
        
        getCode(letter, root)
        if letter in seen:
            for x in tree:
                if x.symbol == letter:
            
                    update(x)
        else:
            seen.add(letter)
            giveBirth(root, letter)
        print("Encoded sequence is now: " + encoded_sequence + "  Length: " + str(len(encoded_sequence)))
        print2D(root)
        print()



seen = set() #conveniently holds all seen symbols
sequence = 'ababbcc' #our sequence to encode
encoded_sequence = '' #memory for our encoded sequence
asciiDict = {chr(i): i for i in range(128)} #initialize ascii dictionary

tree = [] #list of nodes to search easier
original_message = '' 
for letter in sequence:
    original_message += format(asciiDict[letter], "08b") #encoding message using ASCII dictionary

#Output
print('\n')
adaptiveHuffman(sequence)
print('\n\nASCII encoded message: ' + str(original_message) + " - Length: " + str(len(original_message)))
print('Adaptive Huffman message: ' + str(encoded_sequence) + " - Length: " + str(len(encoded_sequence)))
print('Compression Ratio = ' + str(len(original_message)/len(encoded_sequence)))




