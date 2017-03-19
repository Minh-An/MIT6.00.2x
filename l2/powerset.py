#generate power set of items 
def powerSet(items):
    N = len(items)
    #enumerate through all possible combinations of 2**N 
    for i in range(2**N):
        combo = []
        for j in range(N):
            #test the jth bit of integer i, i >> j is equal to i // (2**j)
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
#for combo in powerSet(['a','b','c']):
#    print(combo)

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    #enumerate through all possible combinations of 3**N 
    for i in range(3**N):
        combo = ([],[])
        for j in range(N):
            if (i // (3**j)) % 3 == 1:
                combo[0].append(items[j])
            elif (i // (3**j)) % 3 == 2:
                combo[1].append(items[j])
        yield combo

def toBaseN(decimal, base):
    l = []
    n = decimal
    while n != 0:
        l.append(n % base)
        n = n // base
    return l

def yieldAllCombos2(items):
    N = len(items)
    for i in range(3**N):
        base3 = toBaseN(i, 3)
        bag1, bag2 = [], []
        counter = 0
        for item in items:
            if counter == len(base3):
                break
            elif base3[counter] == 1:
                bag1.append(item)
            elif base3[counter] == 2:
                bag2.append(item)
            counter += 1
        yield (bag1, bag2)

#
#for combo in yieldAllCombos(['a', 'b']):
#    print(combo)