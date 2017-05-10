import itertools
import random

#Problem 3-1
#bucket = ['R','R','R','R','G','G','G','G']
#outOfBucket = list(itertools.combinations(bucket, 3))
#print(len(outOfBucket))
#allSame = 0
#for combo in outOfBucket:
#    if len(set(combo)) == 1:
#        allSame += 1
#print(float(allSame)/len(outOfBucket))

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    bucket = ['R','R','R','R','G','G','G','G']
    allSame = 0
    for i in range(numTrials):
        if len(set(random.sample(bucket, 3))) == 1:
            allSame += 1
    return float(allSame)/numTrials
        
print(drawing_without_replacement_sim(100000))