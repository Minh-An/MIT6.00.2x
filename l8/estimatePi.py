import random

def estimatePi(numTrials):
    pointsInCircle = 0
    for i in range(numTrials):
        x, y = random.random(), random.random()
        if (x**2+y**2)**5 <= 1:
            pointsInCircle += 1
    return 4*(float(pointsInCircle)/numTrials)

print(estimatePi(1000000))