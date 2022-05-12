from collections import OrderedDict

#sequence = 'wabba_wabba_wabba_wabba_woo_woo_woo' #Sequence to encode from example
#charDict = OrderedDict.fromkeys(sorted(dict.fromkeys(sequence))) #Initialize dictionary structure sorted by lexicographical order

sequence = 'hill_billie_bill_'

hw6_given_dict = ['_', 'b', 'h', 'i', 'l', 'e'] #Custom order dictionary from hw6
print(list(set(sequence)))
charDict = OrderedDict.fromkeys(hw6_given_dict) #Initialize dictionary from hw6_given_dict

encoded = '' #initialize encoded message

#Output message
print("Sequence to encode is: " + sequence + "\nStarting dictionary is: " + str(list(charDict.keys())))

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
        ind = str(list(charDict.keys()).index(lastKnownKey))
        encoded += ind + ' ' #add index of last known key to encoded sequence
        print("Step " + str(step) + ": \"" + lastKnownKey + "\": send " + ind + ", add \"" + pattern +"\"")
    step += 1
    charDict[pattern] = None #add new pattern to our dictionary
    i += len(lastKnownKey) #traverse by size of last known key
    if i >=len(sequence):break

print("Final dictionary is: " + str(list(enumerate(charDict.keys()))) + "\nEncoded message is: " + encoded) #Output message  

