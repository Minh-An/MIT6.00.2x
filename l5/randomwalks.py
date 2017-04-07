import random

def randomWalk(steps):
    (x, y) = (0,0)
    for step in range(steps):
        r = random.randint(1,4)
        if r == 1:
            x += 1
        elif r == 2:
            x -= 1
        elif r == 3:
            y+= 1
        else:
            y -= 1
    return x, y

def averageDistance(tests, steps):
    (avgX,avgY) = (0,0)
    for test in range(tests):
        (x,y) = randomWalk(steps)
        avgX += x
        avgY += y
    return avgX/tests, avgY/tests

def averageDistance2(tests, steps):
    walks = [randomWalk(steps) for i in range(tests)]
    avgX = sum(walks[i][0] for i in range(tests))/tests
    avgY = sum(walks[i][1] for i in range(tests))/tests
    return avgX, avgY

print(randomWalk(100000))