#Ex 3
#Write a function called fibosum(n) that calculates the sum of the n first fibonacci terms.
#The main program should call this function twices, with the arguments n=5 and n=10.

def fibosum(n):
    n1= 0
    n2= 1
    finalterm=n1+n2
    for i in range(2, n+1):
        term =n1+n2
        n1 =n2
        n2=term
        finalterm=term+finalterm
    return finalterm
print("Sum of the 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the 10 terms of the Fibonacci series: ", fibosum(10))