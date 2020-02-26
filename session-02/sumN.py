# Function for calculating the sum of the
# N first integer numbers


def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

print("The sum of the first 20 numbers is:", sumn(20))
print("The sum of the first 100 numbers is: ", sumn(100))