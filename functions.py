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
        return str(self.symbol) + ': ' +str(self.prob) 

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
        nodes.append(HuffTreeNode(symbols[i][1], symbols[i][0]))
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
        newHuffTreeNode = HuffTreeNode(round(left.prob+right.prob, 4), left.symbol+right.symbol, left, right)

        #replace the smallest two with the new combined one
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newHuffTreeNode)

        #repeat until we have one root node

    print(nodes[0].symbol + ': ' + str(nodes[0].prob) + '\n')
    # makeCodes(nodes[0])    
    return nodes[0]

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
        self.canvas.create_text(x2+5,y2, text=str(root),anchor='w')

def display(self):
        self.canvas.delete("line")
        self.maxDepth = maxDepth(self.root)
        x = self.width/2
        y = 20
        length = self.height/2
        angle = math.pi/2
        
        
        paintBranch(self,1,x,y,x,y,self.root)
            
           
            


def paintBranch(self, depth,x1, y1, x2,y2,root):
        
        
        # print("paintBranch: depth:", depth, "x1:", x1, "y1:", y1, 'x2:', x2, 'y2:', y2)
        if depth == self.maxDepth+1: return
        drawLine(self,x1,y1, x2,y2,root)
        leftX = x2- ((0.5/(depth+1))*(self.width)/depth)
        rightX = x2+((0.5/(depth+1))*(self.width)/depth)
            # Draw the left branch
        
        if root.left is not None:
            paintBranch(self,depth+1, x2, y2, leftX,y2+100,root.left )
            self.canvas.create_text((x2+leftX)/2,y2+45, text='1',anchor='w')
            # Draw the right branch
        
        if root.right is not None:
            paintBranch(self,depth+1, x2, y2, rightX,y2+100,root.right )        
            self.canvas.create_text((x2+rightX)/2,y2+45, text='0',anchor='w')       