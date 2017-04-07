import random

def rollDie():
    return random.randint(1,6)

def runSim(goal, trials):
    total = 0
    for i in range(trials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    actualProbability = round(1/(6**len(goal)), 8)
    print('Actual Probability: ' + str(actualProbability))
    estimatedProbability = round(total/trials, 8)
    print('Estimated Probability: ' + str(estimatedProbability))
    
runSim('2222', 5000000)