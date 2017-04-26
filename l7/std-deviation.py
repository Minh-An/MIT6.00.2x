def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L:
        lengths = [len(i) for i in L]
        mean = sum(lengths) / len(L)
        return (sum([(i-mean)**2 for i in lengths]) / len(L))**0.5
    return float('NaN')

print(stdDevOfLengths(['a','b','c']))
print(stdDevOfLengths(['apples','oranges','kiwis', 'pineapples']))

def stdDevOfLengthsNumpy(L):
    import numpy
    if L:
        return float(numpy.std([len(i) for i in L]))
    return float('NaN')

print(stdDevOfLengthsNumpy(['a','b','c']))
print(stdDevOfLengthsNumpy(['apples','oranges','kiwis', 'pineapples']))
