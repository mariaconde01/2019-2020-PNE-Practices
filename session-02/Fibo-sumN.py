#Ex 3
#Write a function called fibosum(n) that calculates the sum of the n first fibonacci terms.
#The main program should call this function twices, with the arguments n=5 and n=10.

def fibosum(n):
    n1=0
    n2=1

    counter = 0
    for i in range(2, n+1):
        counter += i
    return counter


print("Sum of first 5 terms of the Fibonacci series is: ", fibosum(5))
print("Sum of first 10 terms of the Fibonaci series is: ", fibosum(10))


