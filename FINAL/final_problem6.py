
#greedy
#def find_combination(choices, total):
#    """
#    choices: a non-empty list of ints
#    total: a positive int
# 
#    Returns result, a numpy.array of length len(choices) 
#    such that
#        * each element of result is 0 or 1
#        * sum(result*choices) == total
#        * sum(result) is as small as possible
#    In case of ties, returns any result that works.
#    If there is no result that gives the exact total, 
#    pick the one that gives sum(result*choices) closest 
#    to total without going over.
#    """
#    duplicate = choices
#    result = [0 for i in range(len(choices))]
#    remainingTotal = total
#    sortedChoices = sorted(choices, reverse = True)
#    for n in sortedChoices:
#        index = duplicate.index(n)
#        result[index] = int(remainingTotal - n >= 0)
#        if result[index] == 1:
#            remainingTotal -= n
#        duplicate[index] = 0
#    return np.array(result)

import numpy as np

#brute force
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    margin = 0
    formatString = '0' + str(len(choices)) +'b'
    combos = [[int(i) for i in format(k, formatString)] for k in range(2**len(choices))]
    result = None
    while result == None:
        for combo in combos:
            if np.dot(combo, choices) == total-margin:
                if result == None or sum(combo) < sum(result):
                    result = combo
        margin += 1
    return result

print(find_combination([1,1,1,9], 4))