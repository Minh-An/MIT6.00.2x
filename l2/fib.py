def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
#for n in range(50):
#    print(str(n) + ": " + str(fib(n)))
    
#compute fibonacci quickly using dynamic programming 
def ffib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else: 
            memo[n] = ffib(n-1, memo) + ffib(n-2, memo)
            return memo[n]
        
for n in range(151):
    print(str(n) + ": " + str(ffib(n)))
