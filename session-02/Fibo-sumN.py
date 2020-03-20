#Write a function called fibosum(n) that calculates the sum of the n first fibonacci terms

def fibosum(n):
    a, b = 0, 1
    sum = 0
    for i in range(n):
        a, b= b, a + b
        sum = a + b
    return sum

print("sum of the first 5 terms of the fibonacci series", fibosum(5))
print("sum of the first 10 terms of the fibonacci series", fibosum(10))

#####lo de soria

def fibosum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n)


def fibonacci(n):
    fibo1 = 0
    fibo2 = 1
    summing = 1
    for i in range(0, n - 1):
        count = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = count
        summing = summing + count
    return summing


print("Sum of the first 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series: ", fibosum(10))