#Convert the previous program into the function fibon(n)
# calculates the nth Fibonacci term and return it

def fibon(n):
    a, b = 0,1
    for n in range(n):

        a, b = b, a+b
    return a
print("5th fibonacci term is", fibon(5))
print("10th fibonacci term is", fibon(10))
print("15th fibonacci term is", fibon(15))

