from itertools import chain, combinations

#code from Martijn Pieters on stackoverflow
#http://stackoverflow.com/questions/18035595/powersets-in-python-using-itertools
def powerset(items):
    l = list(items)
    return chain.from_iterable(combinations(l, n) for n in range(len(items)+1))

results = powerset(['a','b','c'])
#results is a generator

for result in results:
    print(result)