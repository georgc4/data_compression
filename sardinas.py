found_words = []
c_inf = set()

# recursive function to generate the next set in the sequence


def generate_cn(c, n):
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
            print('S'+str(n) + ' ' + str(cn))
        c_inf.update(cn)
        return cn


def sardinas(c):
    n = sum(len(i) for i in c)
    generate_cn(c, n)
    print('\nIf ' + str(c) + ' and ' + str(c_inf) +
          ' \nhave no common elements, then the code is uniquely decodeable')

    if(c.isdisjoint(c_inf)):
        print('\nThe code ' + str(c) +
              ' is uniquely decodeable; The intersection between the alphabet and the union of all the suffix sets is the empty set')
    else:
        print('\nThe code ' + str(c) +
              ' is not uniquely decodeable: \nThe alphabet shares element(s) ' + str(c.intersection(c_inf)) + ' with the union of all the suffix sets')


#c = set(['0', '1'])
#c = set(['0', '01', '11'])

c = set(['1100', '11010', '00','100','110110', '110111', '01', '101'])
#c = set(['1001', '1011', '111', '10', '1110'])
#c = set(['1', '01', '0110', '01001', '10001'])
#c = set(['011','010','110','01111','01011','101110'])
print('\nThe alphabet is' + str(c) + '\n')
sardinas(c)
