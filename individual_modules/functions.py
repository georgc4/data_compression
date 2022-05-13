import math
def km(c):
    return sum([1/(2**len(i)) for i in c]) 


found_words = []
c_inf = set()
sets = ''
# recursive function to generate the next set in the sequence


def generate_cn(c, n):
    global sets
    if n == 0:
        return set(c)
    else:
        # create a set to hold our new elements
        cn = set()

        # generate c_(n-1)
        cn_minus_1 = generate_cn(c, n-1)

        for u in c:
            for v in cn_minus_1:
                if (len(u) > len(v)) and u.find(v) == 0 and u[len(v):] not in found_words:
                    cn.add(u[len(v):])
                    found_words.append(u[len(v):])
        for u in cn_minus_1:
            for v in c:
                if len(u) > len(v) and u.find(v) == 0 and u[len(v):] not in found_words:
                    cn.add(u[len(v):])
                    found_words.append(u[len(v):])
        if(len(cn_minus_1) > 0):
            sets += 'S'+str(n) + ' ' + str(cn)+'\n'
        c_inf.update(cn)
        return cn


def sardinas(c):
    global sets
    global found_words
    global c_inf
    sets = ''
    c_inf = set()
    found_words = []
    n = sum(len(i) for i in c)
    generate_cn(c, n)
    message ='If ' + str(c) + ' and ' + str(c_inf) + ' have no common elements, then the code is uniquely decodeable\n'

    if(c.isdisjoint(c_inf)):
        message +='\nThe code ' + str(c) + ' is uniquely decodeable; The intersection between the alphabet and the union of all the suffix sets is the empty set\n'
    else:
        message += '\nThe code ' + str(c) + ' is not uniquely decodeable: The alphabet shares element(s) ' + str(c.intersection(c_inf)) + ' with the union of all the suffix sets\n'
    return message,sets



class HuffTreeNode:
    def __init__(self, prob, symbol, left = None, right = None):
        self.prob = prob

        self.symbol = symbol

        self.left = left
        
        self.right = right

        self.code = ''
    def __repr__(self):
        return str(self.symbol) + ': ' +'{:0.3f}'.format(self.prob)

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
        # print(node.symbol + ': Up (1)') 
        makeCodes(node.left, newVal)
    if(node.right):
        # print(node.symbol + ': Down (0)')
        makeCodes(node.right, newVal)
    #base case where we've reached a leaf   
    if(not node.left and not node.right):
        codes[node.symbol] = newVal
        # print(node.symbol + ': ' + newVal +'\n')
    return codes

#create the tree
def ConstructHuffmanTree(symbols):
    global codes
    codes = dict()
    nodes = []
    for i in range(len(symbols)):
        nodes.append(HuffTreeNode(symbols[i][1], symbols[i][0]))
    #construct binary tree
    while len(nodes) >1:

        #sort the list
        nodes = sortCodebook(nodes)

        #show steps
        # for i in range(len(nodes)):
            # print(nodes[i].symbol + ': ' + str(nodes[i].prob))
        # print()

        #choose smallest two probabilities
        right = nodes[len(nodes)-1]
        left = nodes[len(nodes)-2]

        #assign codes to branches
        right.code = '1'
        left.code = '0'

        #make a new node of the combined two
        newHuffTreeNode = HuffTreeNode(round(left.prob+right.prob, 3), left.symbol+right.symbol, left, right)

        #replace the smallest two with the new combined one
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newHuffTreeNode)

        #repeat until we have one root node

    # print(nodes[0].symbol + ': ' + str(nodes[0].prob) + '\n')
    # makeCodes(nodes[0])    
    return nodes[0]
def getMaxWidth(root):
    maxWidth = 0
    h = maxDepth(root)
    # Get width of each level and compare the
    # width with maximum width so far
    for i in range(1, h+1):
        width = getWidth(root, i)
        if (width > maxWidth):
            maxWidth = width
    return maxWidth
 
# Get width of a given level
 
 
def getWidth(root, level):
    if root is None:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return (getWidth(root.left, level-1) +
                getWidth(root.right, level-1))
def maxDepth(root):
  # Null node has 0 depth.
  if root == None:
    return 0

  # Get the depth of the left and right subtree 
  # using recursion.
  leftDepth = maxDepth(root.left)
  rightDepth = maxDepth(root.right)

  # Choose the larger one and add the root to it.
  if leftDepth > rightDepth:
    return leftDepth + 1
  else:
    return rightDepth + 1


def drawLine(self, x1,y1, x2,y2,root):
        self.canvas.create_line(x1,y1, x2,y2, tags = "line")    
        txt = self.canvas.create_text(x2+5,y2, text=str(root),anchor='w')
        if root.left is None and root.right is None: self.canvas.itemconfig(txt,anchor='n')
def display(self,adaptive):
        self.canvas.delete("line")
        self.maxDepth = maxDepth(self.root)
        x = self.width/2
        y = 20
        if adaptive == True: x = self.width *0.8
        
        
        paintBranch(self,1,x,y,x,y,self.root,adaptive)
            
           
            


def paintBranch(self, depth,x1, y1, x2,y2,root,adaptive):
        
        
        # print("paintBranch: depth:", depth, "x1:", x1, "y1:", y1, 'x2:', x2, 'y2:', y2)
        if depth == self.maxDepth+1: return
        
        drawLine(self,x1,y1, x2,y2,root)
        if adaptive == False:
            leftX = x2- ((0.5/(depth))*(0.9*self.width)/(depth))
            rightX = x2+((0.5/(depth))*(0.9*self.width)/(depth))
            newY = y2 + 80
        else: 
            leftX = x2- 50
            rightX = x2+50
            newY = y2 + 80
            # Draw the left branch
        
        if root.left is not None:
            if depth == 1 and adaptive == False:leftX += 0.3*(abs(leftX -x2))
            paintBranch(self,depth+1, x2, y2, leftX,newY,root.left,adaptive )
            self.canvas.create_text(((x2+leftX)/2)-10,y2+45, text='0',anchor='w')
            # Draw the right branch
        
        if root.right is not None:
            if depth ==1 and adaptive ==False: rightX -= 0.3*(abs(rightX -x2))
            paintBranch(self,depth+1, x2, y2, rightX,newY,root.right, adaptive)        
            self.canvas.create_text(((x2+rightX)/2)+10,y2+45, text='1',anchor='w')       

class AdaptNode:
    #Class definition for nodes
    def __init__(self, number, weight= 0, symbol=None, parent=None, left = None, right = None):
        self.weight = weight

        self.symbol = symbol

        self.number = number

        self.parent = parent

        self.left = left
        
        self.right = right

    def __repr__(self):
        if self.symbol is not None: return "#" +str(self.number) + "\nweight:" +str(self.weight) + "\nsym:" +str(self.symbol)
        else: return "#" +str(self.number) + "\nweight:" +str(self.weight)

def update(self,node):
    
    #Finding max node in block
    block = []
    for x in self.tree:
        if x.weight == node.weight and ((x.symbol is None and node.symbol is None) or (x.symbol is not None and node.symbol is not None)): 
            #print(x)
            block.append(x)
    max_AdaptNode = None
    for x in block:
        if max_AdaptNode is None or x.number > max_AdaptNode.number:
            max_AdaptNode = x

    #Swapping node with max node and incrementing        
    #print("Block for: " + str(node) + " is " + str(block) + " and max_AdaptNode is " + str(max_AdaptNode)) #Uncomment to see the block for each node
    if node is not max_AdaptNode:
        node, max_AdaptNode = max_AdaptNode, node
        #print("After Swapping... max node is " + str(max_AdaptNode) + ' and node is ' + str(node))
        node.weight+=1
        node.symbol, max_AdaptNode.symbol, = max_AdaptNode.symbol, node.symbol
        # max_AdaptNode.weight, node.weight = node.weight, max_AdaptNode.weight
    else: node.weight+= 1
    
    
    #If not root node, continue with parent node
    if node.parent is not None: update(self,node.parent)
    return

#Function that creates two new nodes when a letter is not seen
def giveBirth(self,node, letter):
    if node is None:
        return
    
    if node.symbol == 'NYT':
        node.symbol = None
        node.weight += 1
        node.left = AdaptNode(node.number-2, parent=node, symbol='NYT') #New NYT on the left
        node.right = AdaptNode(node.number-1, parent=node, symbol=letter, weight = 1) #External node on the right
        self.tree.extend([node.left, node.right])
        
        if node.parent is not None: update(self,node.parent)
        return
    else:
        #Recursively finding NYT
        giveBirth(self,node.left, letter)
        giveBirth(self,node.right, letter)

#Traverse tree to find path to create codewords
def getCode(self,letter,root, val=''):
    global encoded_sequence
    if root.left is not None or root.right is not None:
        getCode(self,letter, root.left, val +'0')
        getCode(self,letter, root.right, val +'1')


    if letter == root.symbol:
        # print("Letter " + letter + " was found. Sending " + val) 
        self.encoded_sequence += val
    elif root.symbol == 'NYT' and letter not in self.seen:
        # print("Letter " + letter + " was not found. Sending " + val + " for NYT, and " + format(asciiDict[letter], "08b") + " from ASCII dictionary" )
        self.encoded_sequence += val + format(asciiDict[letter], "08b")

#Send each symbol through the process
def adaptiveHuffman(self,sequence):
    n = len(set(sequence))
    number = 2*n - 1
    root = AdaptNode(number, symbol='NYT')
    self.tree.append(root)
    
    for letter in sequence:
        
        getCode(self,letter, root)
        if letter in self.seen:
            for x in self.tree:
                if x.symbol == letter:
            
                    update(self,x)
        else:
            self.seen.add(letter)
            giveBirth(self,root, letter)
        # print("Encoded sequence is now: " + self.encoded_sequence + "  Length: " + str(len(self.encoded_sequence)))
        # print()
    
    return root,self.encoded_sequence


asciiDict = {chr(i): i for i in range(128)} #initialize ascii dictionary


def adrawLine(self, x1,y1, x2,y2):
    self.canvas.create_line(x1,y1, x2,y2, tags = "line")    
def adisplay(self):
    self.canvas.delete("line")
    depth = self.depth
    self.angle =math.pi/2
    apaintBranch(self,depth, self.width/1.1, 0, self.height/depth, self.angle,self.root)

def apaintBranch(self, depth, x1, y1, length, angle,root):
    if depth >= 0:
        depth -= 1
        x2 = x1 + int(math.cos(angle) * length)
        y2 = y1 + int(math.sin(angle) * length)
        # Draw the line

        if depth < self.depth-1: drawLine(self,x1,y1, x2,y2,root)
        else:
            y2 = y1 +40
            self.canvas.create_text(x2+5,y2, text=str(root),anchor='w')
        if root.left is not None:
             apaintBranch(self,depth, x2, y2, length * self.sizeFactor, self.angle + self.angleFactor,root.left )
            #  self.canvas.create_text(((x2+leftX)/2)-10,y2+45, text='0',anchor='w')
             # Draw the right branch

        if root.right is not None:
             apaintBranch(self,depth, x2, y2, length * self.sizeFactor, self.angle -self.angleFactor, root.right)        
            #  self.canvas.create_text(((x2+rightX)/2)+10,y2+45, text='1',anchor='w')           

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

def compGolomb(symbols,m):
    

    alphabet,probs = zip(*symbols)
    dictionary = dict()
    codebook = dict()
    for i in range(len(alphabet)):
        golombedSym = golomb(alphabet[i],m)
        codebook[chr(alphabet[i]+64)] = golombedSym 
        dictionary[golombedSym] = probs[i]
    averageLength = 0
    for word in dictionary:
        averageLength += len(word)* dictionary[word]
    return codebook, averageLength

s = ''

#node class definition
class TNode:
    def __init__(self, symbol, prob):
        self.prob = prob
        self.symbol = symbol
        self.n = '(' + '{:0.3f}'.format(self.prob) + ') ' + self.symbol + ' '
        self.children = []
        self.code = ''

#print N-ary tree utility function -- courtesy of geeksforgeeks
def printNTree(x,flag,depth,isLast):
    global s

    # Condition when node is None
    if x == None:
        return
       
    # Loop to print the depths of the
    # current node
    for i in range(1, depth):
        # Condition when the depth is exploring
        if flag[i]:
            # print("| ","", "", "", end = "", file=s)
            s += '|    '
        # Otherwise print the blank spaces
        else:
            # print(" ", "", "", "", end = "", file=s)
            s += '    '
       
    # Condition when the current node is the root node
    if depth == 0:
        s += '\n'
       
    # Condition when the node is the last node of the exploring depth
    elif isLast:
        if x.children == []:
            # print("+---", '\033[92m' ,x.n, x.code, '\033[0m', file=s) #modified to make leaves green
            s+= '+---  '+str(x.n)+str(x.code)+'\n'
        else:
            # print("+---", x.n,file=s)
            s+= '+--- ' + str(x.n) +'\n'   
        # No more childrens turn it to the non-exploring depth
        flag[depth] = False
    else:
        if x.children == []:
            # print("+---", '\033[92m' ,x.n, x.code, '\033[0m',file=s) #modified to make leaves green
            s+= '+--- '+str(x.n)+str(x.code)+'\n'
        else:
            # print("+---", x.n,file=s) 
            s+= '+--- ' + str(x.n) +'\n'   
   
    it = 0
    for i in x.children:
        it+=1 
        # Recursive call for the children nodes
        printNTree(i, flag, depth + 1, it == (len(x.children) - 1))
    flag[depth] = True


#function that counts number of leaves in the tree
def countLeaves(node):
    numOfLeaves = 0
    for child in node.children:
        if child.children == []:
            numOfLeaves += 1
        else:
            numOfLeaves += countLeaves(child)
    return numOfLeaves

#function that adds all new symbols into a list    

def findLeaves(node):
    for child in node.children:
        if child.children == []:
            leaves.append(child)
        else:
            findLeaves(child)
    
#function that finds the largest probability leaf
def findlargest(root):
    global maximum
    # Base Case
    if (root == None):  return

    # If maximum is null, return the value of root node
    if ((maximum) == None): maximum = root

    # If value of the root is greater than maximum, update the maximum node
    elif (root.prob > maximum.prob) and root.children == []: maximum = root

    # Recursively call for all the children of the root node
    for i in range(len(root.children)): findlargest(root.children[i])



# Function to form the Tree and
# print it graphically
def formAndPrintTree(dictionary, m):
    global maximum
    global leaves
    leaves = []
    global s
    s=''
    root = TNode('',0) #create a root
    #add original symbols as leaves 
    for word in dictionary:
        root.children.append(TNode(word, dictionary[word]))
        
       
    # Array to keep track
    # of exploring depths
      
    flag = [True]*(m)
    # Tree Formation

    #algorithm is here
    while True: 
        if countLeaves(root) + len(dictionary) <= m: #if theres room for another iteration
            maximum = None
            findlargest(root) #get max leaf
            for letter in dictionary:
                    #add concatenated symbols to max node
                    maximum.children.append(TNode(maximum.symbol + letter, maximum.prob * dictionary[letter]))
        else: break #exit loop once limit is reached
    
   
    #encode new dictionary
    n = math.ceil(math.log2(m))
    findLeaves(root)
    
    leafSyms = [leaf.symbol for leaf in leaves]
    leafSyms.sort() #lexicographic sort
    i = 0
    for leaf in leaves:
        #bit binary encoding
        leaf.code = format(i, '0'+str(n)+'b') 
        i+=1

    printNTree(root, flag, 0, False) #print
    
    #Find average length per symbol
    avgLength = 0
    for leaf in leaves:
        avgLength += (len(leaf.code)/len(leaf.symbol))*leaf.prob 
    s+= "\nAverage Length per Symbol = " + str(round(avgLength,2))
    return s


from collections import OrderedDict
get_bin = lambda x, n: format(x, 'b').zfill(n)
def LZWEncode(sequence):

#sequence = 'wabba_wabba_wabba_wabba_woo_woo_woo' #Sequence to encode from example
#charDict = OrderedDict.fromkeys(sorted(dict.fromkeys(sequence))) #Initialize dictionary structure sorted by lexicographical order
    message = ''
    seq_dict = list(set(sequence))

    charDict = OrderedDict.fromkeys(seq_dict) #Initialize dictionary from hw6_given_dict

    encoded = []#initialize encoded message

    #Output message
    message += "Sequence to encode is: " + sequence + "\nStarting dictionary is: " + str(list(charDict.keys()))

    i = 0
    step = 1
    for k in range(len(sequence)):
        pattern = sequence[i] #grab current letter
        j =i #starting at current letter
        while pattern in charDict and j+1 < len(sequence):
            pattern += sequence[j+1] #concatenate next letter to current pattern while old pattern is in dictionary
            j+=1 #go to next letter

        if len(pattern) >1: lastKnownKey = pattern[0:-1] #last known key is the pattern minus the last letter
        else: lastKnownKey = pattern

        if lastKnownKey != '': 
            ind = list(charDict.keys()).index(lastKnownKey)
            encoded.append(ind) #add index of last known key to encoded sequence
            # print("Step " + str(step) + ": \"" + lastKnownKey + "\": send " + ind + ", add \"" + pattern +"\"")
        step += 1
        charDict[pattern] = None #add new pattern to our dictionary
        i += len(lastKnownKey) #traverse by size of last known key
        if i >=len(sequence):break
    mydict = dict((j,i) for i,j in enumerate(charDict.keys()))
    encodedmsg=''
    for i in encoded:
        encodedmsg += get_bin(i,math.ceil(math.log2(len(charDict.keys()))))
    message += "\nFinal dictionary is: " + str(mydict) + "\nEncoded message is: " + str(encodedmsg) #Output message  
    return message, mydict, encodedmsg

