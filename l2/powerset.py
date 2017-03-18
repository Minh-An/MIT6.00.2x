#generate power set of items 
def powerSet(items):
    N = len(items)
    for i in range(2**N):
        combo = []
        for j in range(N):
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
for combo in powerSet(['a','b','c']):
    print(combo)