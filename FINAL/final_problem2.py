import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

#pylab.hist(tVals, bins=50)
#pylab.show()
#pylab.hist(xVals, bins=50)
#pylab.show()

#pylab.plot(xVals, zVals)
#pylab.show()
#pylab.plot(xVals, yVals)
#pylab.show()
#pylab.plot(xVals, sorted(yVals))
#pylab.show()
#pylab.plot(sorted(xVals), yVals)
#pylab.show()
#pylab.plot(sorted(xVals), sorted(yVals))
#pylab.show()