import math

def E3(l,u):
    #If second MSB of u is 0 and second MSB of l is 1 then E3 Holds
    if u[1] == '0' and l[1] == '1': return True
    else: return False

#Initializing data structures
sequence = 'ac'
A = ['a','b','c']
counts = [8,2,2]
n_i = dict()
Cum_Count = dict()
Cum_Count[chr(ord(A[0])-1)] = 0 #Cum_Count[a-1] = 0
i = 0
for letter in A:
    n_i[letter] = counts[i]
    i += 1

s = 0
for letter in A:
    s += n_i[letter]
    Cum_Count[letter] = s
Total_Count = s

n_tag = math.ceil(math.log2(4*Total_Count))

l = []
u = []
l.append('0'*n_tag)
u.append('1'*n_tag)

print("\nInitializing encoding procedure...")
print("Alphabet:count = " + str(n_i))
print("Cum_Count = " + str(Cum_Count))
print("Total_Count = " + str(Total_Count))
print("Tag length = " + str(n_tag))
print("l(0) = " + l[0])
print("u(0) = " + u[0])

i = 1
code = ''
Scale3 = 0
for letter in sequence:
    code_per_letter =''
    print("\nReceived symbol: " + letter)
    ############### l(n-1)       + floor(         u(n-1)        -      l(n-1)   + 1) x Cum_Count(xn -1)                /Total Count
    new_l = format(int(l[i-1],2) + math.floor( ( (int(u[i-1],2) - int(l[i-1],2) + 1) * Cum_Count[chr(ord(letter)-1)] ) /Total_Count), '0' + str(n_tag) + 'b')   
    new_u = format(int(l[i-1],2) + math.floor( ( (int(u[i-1],2) - int(l[i-1],2) + 1) * Cum_Count[chr(ord(letter))])    /Total_Count) - 1, '0' + str(n_tag) + 'b')
    l.append(new_l)   
    u.append(new_u)
    print("l(" +str(i) + "): " + l[i])
    print("u(" +str(i) + "): " + u[i])
    #Algorithm
    while l[i][0] == u[i][0] or E3(l[i], u[i]): #while(MSB of u and l are both equal to b or E3 condition holds)
        if l[i][0] == u[i][0]: #if MSB of u and l are both equal to b
            b = l[i][0] 
            code += b #send b
            code_per_letter += b #store code per letter for output
            l[i] = l[i][1:] + '0' #shift l to the left by 1 bit and shift 0 into LSB
            u[i] = u[i][1:] + '1' #shift u to the left by 1 bit and shift 1 into LSB
            
            while(Scale3 > 0): 
                
                if b == '0': 
                    code += '1' #Send complement of b
                    code_per_letter += '1' #Store what we sent for output
                else: 
                    code += '0'
                    code_per_letter += '0' #Store what we sent for output
                Scale3 -= 1 #decrement Scale3

        if E3(l[i], u[i]): #if E3 condition holds
            l[i] = l[i][1:] + '0' #shift l to the left by 1 bit and shift 0 into LSB
            u[i] = u[i][1:] + '1' #shift u to the left by 1 bit and shift 1 into LSB

            #Complement (new) MSB of l and u
            if l[i][0] == '0': l[i] = '1' + l[i][1:] 
            else:              l[i] = '0' + l[i][1:]
            
            if u[i][0] == '0': u[i] = '1' + u[i][1:]
            else:              u[i] = '0' + u[i][1:]

            
            Scale3 += 1 #increment Scale3
            print("E3 Counter = " + str(Scale3))
    print("We sent: " + code_per_letter)
    i=i+1

#Termination of code
#To terminate the code, we send the value of l(i)
#unless Scale3 > 0, then we send the complement of b after sending b,
#then we send the rest of l(i)
print("\nTerminating the code...")
i -=1 #go to last element
b = l[i][0] #store MSB of l(i)
print("l(" +str(i) + ") : " + l[i])
if Scale3 > 0: #Send l(i)_MSB + complement of b + rest of l(i) 
    print("Since Scale3 = " + str(Scale3) + ", we send MSB of l(i), then complement of MSB of l(i), then rest of l(i)")
    if b == '0': 
        code += b + '1' + l[i][1:]
        print("We sent: " + b + '1' + l[i][1:])
    else:        
        code += b + '0' + l[i][1:]
        print("We sent: " + b + '0' + l[i][1:])

#Send l(i)
else:            
    print("Since Scale3 < 0, we simply send l(i)")
    code += l[i]
    print("We sent: " + l[i])

print("\nThe final result is: " + code)