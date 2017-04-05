import pylab as plt

mySample = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySample.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
#x label: sample points; y label: ___ function; title: function name
#ylim() = y limit parameters: minimum and maximum of the range
#plt.clf() to clear plots

        
        
        
#string chooses color & style for line:
    #first character is color: b for blue, r for red, o-orange, g - green
    #second character for style, - for line,  -- for dash, ^ for triangle, o for circle
#yscale for the scale: ex. log scale
#subplot: 3 arguments: # of rows, # of columns, and location to use
#label for legend, color, linewidth(in pixels)

#==============================================================================
# Example 1
#==============================================================================
#plt.figure('quad expo')
#plt.clf()
#plt.plot(mySample, myQuadratic, label = 'quadratic') 
#plt.plot(mySample, myExponential, label = 'exponential')
#plt.ylim(0,2000)
#plt.legend(loc = 'upper left') #loc is location for the legend
#plt.title('Quadratic vs. Exponential')

plt.figure('lin quad')
plt.clf()
plt.plot