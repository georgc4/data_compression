from tkinter import * # Import tkinter
import math
#node class definition
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
    makeCodes(nodes[0])    
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
# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root)
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
 
# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = maxDepth(root)
    
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
 


################################################################
## 'Main' function
## Edit symbols list and run to get huffman encoding and relevant statistics


#symbols = [('a1',0.4), ('a2',0.2), ('a3',0.2), ('a4',0.1), ('a5',0.1)] #Example from modules
symbols = [('a', 0.4), ('b', 0.2), ('c',0.1), ('d', 0.1), ('e', 0.09), ('f',0.09), ('g', 0.01), ('h', 0.01)]
root = ConstructHuffmanTree(symbols)
printLevelOrder(root)
print(maxDepth(root))
class Main:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Recursive Tree") # Set a title
        self.root = root
        self.width = 20* 2**maxDepth(root)
        self.height = 800
        self.canvas = Canvas(window, 
        width = self.width, height = self.height,bg="white")
        self.canvas.pack()
        self.angleFactor = math.pi/3
        self.sizeFactor = .6
        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()

        Label(frame1, 
            text = "Enter the depth: ").pack(side = LEFT)
        self.depth = StringVar()
        Entry(frame1, textvariable = self.depth, 
            justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Display Recursive Tree", 
            command = self.display).pack(side = LEFT)

        

        window.mainloop() # Create an event loop

    def drawLine(self, x1,y1, x2,y2,root):
        self.canvas.create_line(x1,y1, x2,y2, tags = "line")    
        self.canvas.create_text(x2+5,y2, text=str(root),anchor='w')

    def display(self):
        self.canvas.delete("line")
        self.maxDepth = maxDepth(root)
        x = self.width/2
        y = 20
        length = self.height/2
        angle = math.pi/2
        
        
        self.paintBranch(1,x,y,x,y,self.root)
            
           
            


    def paintBranch(self, depth,x1, y1, x2,y2,root):
        
        
        # print("paintBranch: depth:", depth, "x1:", x1, "y1:", y1, 'x2:', x2, 'y2:', y2)
        if depth == self.maxDepth+1: return
        self.drawLine(x1,y1, x2,y2,root)
        leftX = x2- ((0.5/(depth+1))*(self.width)/depth)
        rightX = x2+((0.5/(depth+1))*(self.width)/depth)
            # Draw the left branch
        
        if root.left is not None:
            self.paintBranch(depth+1, x2, y2, leftX,y2+100,root.left )
            self.canvas.create_text((x2+leftX)/2,y2+45, text='1',anchor='w')
            # Draw the right branch
        
        if root.right is not None:
            self.paintBranch(depth+1, x2, y2, rightX,y2+100,root.right )        
            self.canvas.create_text((x2+rightX)/2,y2+45, text='0',anchor='w')       


Main()