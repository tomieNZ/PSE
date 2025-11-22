"""
This file is used to calculate a Fibonacci series by manual calculation and by math library.
"""

#Fist, I will use the manual calculation to calculate the Fibonacci series.
def fibonacci_manual(n):
    if n <=0:
        return []
    elif n == 1:
        return [0]
    elif n ==2:
        return [0,1]
    # Initialize the Fibonacci series with the first two numbers
    fibonacci_series = [0,1]
    # Loop through the series to calculate the next number
    for i in range(2,n):
        fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
    return fibonacci_series


import math
#Second, I will use the math library to calculate the Fibonacci series.
def fibonacci_math_by_library(n):
    if n <= 0:
        return []
    
    #Calculate the square root of 5
    # Phi is the golden ratio, which is the ratio of the two consecutive numbers in the Fibonacci series
    # Psi is the negative golden ratio, which is the ratio of the two consecutive numbers in the Fibonacci series
    # Actually, I ask AI the formula, called Binet's formula
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    # Calculate the Fibonacci series using the formula
    fibonacci_series = [0,1]
    # Loop through the series to calculate the next number
    for i in range(2,n):
        fibonacci_series.append(int((phi**i - psi**i) / sqrt5))
    # Return the Fibonacci series
    return fibonacci_series

if __name__ == "__main__":
    #test the manual calculation
    print(fibonacci_manual(10))
    #test the math library calculation
    print(fibonacci_math_by_library(10))