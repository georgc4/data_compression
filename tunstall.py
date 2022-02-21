import math
#node class definition
class Node:
    def __init__(self, symbol, prob):
        self.prob = prob
        self.symbol = symbol
        self.n = '(' + str(self.prob) + ') ' + self.symbol + ' '
        self.children = []
        self.code = ''

#print N-ary tree utility function -- courtesy of geeksforgeeks
def printNTree(x,flag,depth,isLast):
    # Condition when node is None
    if x == None:
        return
       
    # Loop to print the depths of the
    # current node
    for i in range(1, depth):
        # Condition when the depth is exploring
        if flag[i]:
            print("| ","", "", "", end = "")
           
        # Otherwise print the blank spaces
        else:
            print(" ", "", "", "", end = "")
       
    # Condition when the current node is the root node
    if depth == 0:
        print()
       
    # Condition when the node is the last node of the exploring depth
    elif isLast:
        if x.children == []:
            print("+---", '\033[92m' ,x.n, x.code, '\033[0m') #modified to make leaves green
        else:
            print("+---", x.n)   
        # No more childrens turn it to the non-exploring depth
        flag[depth] = False
    else:
        if x.children == []:
            print("+---", '\033[92m' ,x.n, x.code, '\033[0m') #modified to make leaves green
        else:
            print("+---", x.n) 
   
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
leaves = []
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
    root = Node('',0) #create a root

    #add original symbols as leaves 
    for word in dictionary:
        root.children.append(Node(word, dictionary[word]))
        
       
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
                    maximum.children.append(Node(maximum.symbol + letter, maximum.prob * dictionary[letter]))
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
    print("Average Length per Symbol = " + str(round(avgLength,2)))


#create original dictionary
alphabet = ['a', 'b','c']
probs = [0.6, 0.3, 0.1]
dictionary = dict()
for i in range(len(alphabet)):
    dictionary[alphabet[i]] = probs[i]


m = 8 # parameter
formAndPrintTree(dictionary, m)