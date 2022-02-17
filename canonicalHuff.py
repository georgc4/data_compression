#####################################################################################
#This script will produce a canonical huffman code for a given code
#based on the algorithm described by the wikipedia article: "Canonical Huffman Code"
#https://en.wikipedia.org/wiki/Canonical_Huffman_code
#####################################################################################
#Here is a summary of the algorithm

#To make the code a canonical Huffman code, the codes are renumbered. The bit lengths 
#stay the same with the code book being sorted first by codeword length and secondly by alphabetical value
#I use resortAlpha() to sort the codebook

#Each of the existing codes are replaced with a new one of the same length, using the following algorithm:

#The first symbol in the list gets assigned a codeword which is the same length as the symbol's original codeword but all zeros. 
# This will often be a single zero ('0').

#Each subsequent symbol is assigned the next binary number in sequence, ensuring that following codes are always higher in value.

#When you reach a longer codeword, then after incrementing, append zeros until the length of the new codeword is equal to the length of the old codeword. 
# This can be thought of as a left shift.
##############################################################################################################################

#Class to store the data
class Letter:
    def __init__(self, symbol, codeword):
        self.symbol = symbol
        self.codeword = codeword
        self.length = len(self.codeword)

#Helper function to sort according to algorithm
def resortAlpha(alphabet):
    lst = len(alphabet) 
    for i in range(0, lst): 
          
        for j in range(0, lst-i-1): 

            #ascending order by length
            if alphabet[j].length > alphabet[j+1].length: 
                temp = alphabet[j] 
                alphabet[j]= alphabet[j + 1] 
                alphabet[j + 1]= temp 
            
            #same length case
            if alphabet[j].length == alphabet[j+1].length and alphabet[j].symbol > alphabet[j+1].symbol:
                temp = alphabet[j] 
                alphabet[j]= alphabet[j + 1] 
                alphabet[j + 1]= temp
    return alphabet

def printCanonicalAlphabet(syms, codes):
   
    #Create array of Letter objects based on input lists
    if len(syms) == len(codes): #minimal input validation
        alphabet = [Letter(syms[i], codes[i]) for i in range(len(syms))] #list comprehension
        #print our list of Letter objects
        print("\nOriginal Alphabet")
        for letter in alphabet:
            print (letter.symbol + ': ' + letter.codeword)
        alphabet = resortAlpha(alphabet)

    #Show our sorted alphabet
    print("\nSorted Alphabet")
    for letter in alphabet:
        print (letter.symbol + ': ' + letter.codeword)

    #Allocate space for our new alphabet
    canonical_alphabet = []

    #Step one
    code = alphabet[0].length * '0'
    canonical_alphabet.append(Letter(alphabet[0].symbol,code))

    #Rest of the algorithm
    for i in range(1,len(alphabet)):
        #Next binary number in sequence
        code = format(int(code,2)+ 1, "0b")
        #If we reach a longer codeword
        if alphabet[i].length > alphabet[i-1].length:
            #Left shift
            code = format(int(code,2) << (alphabet[i].length - alphabet[i-1].length), "b") #append difference of length number of 0s
        
        #Maintain leading 0's for same length letters
        #the conversions can cause the number to lose leading 0's
        else:
            code = format(int(code,2), '0' + str(alphabet[i].length) +"b")
        
        #Add it to our alphabet
        newLetter = Letter(alphabet[i].symbol,code)
        canonical_alphabet.append(newLetter)

    #Show the result
    print("\nCanonical alphabet")
    for letter in canonical_alphabet:
        print (letter.symbol + ': ' + letter.codeword)

#Homework 2.2
syms = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
codes = ['1100', '11010', '00','100','110110', '110111', '01', '101']


#Alphabet from wikipedia article used for testing
#syms = ['a', 'b', 'c', 'd']
#codes = ['11', '0', '101','100']

printCanonicalAlphabet(syms, codes)

       
