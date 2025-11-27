"""
Part1 - Develop a Python program that uses functions to generate an N-length Fibonacci series and compute the factorial of N. Do not use any external packages in this version. Include clear inline comments to show your understanding, then upload your code to GitHub and share the link.
 
Part2 - For the second version, update your program by using built-in packages such as "Math" to enhance or simplify your calculations. Upload this updated version to GitHub as well.
"""

# ============================================================================
# PART 1: Manual calculation without external packages
# ============================================================================

def fibonacci_manual(n):
    """
    Generate a Fibonacci series of length N using manual calculation.
    
    Args:
        n (int): The length of the Fibonacci series to generate
        
    Returns:
        list: A list containing the Fibonacci series
    """
    # Handle edge cases: return empty list for invalid input
    if n <= 0:
        return []
    # First number in Fibonacci series is 0
    elif n == 1:
        return [0]
    # First two numbers in Fibonacci series are 0 and 1
    elif n == 2:
        return [0, 1]
    
    # Initialize the Fibonacci series with the first two numbers
    fibonacci_series = [0, 1]
    
    # Loop through to calculate subsequent numbers
    # Each number is the sum of the previous two numbers
    for i in range(2, n):
        next_number = fibonacci_series[i-1] + fibonacci_series[i-2]
        fibonacci_series.append(next_number)
    
    return fibonacci_series


def factorial_manual(n):
    """
    Calculate the factorial of N using manual calculation.
    Factorial of n (n!) = n * (n-1) * (n-2) * ... * 2 * 1
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    """
    # Handle edge cases: factorial of 0 or negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    # Factorial of 0 is 1 by mathematical definition
    elif n == 0 or n == 1:
        return 1
    
    # Initialize result to 1
    result = 1
    
    # Multiply each number from 2 to n
    for i in range(2, n + 1):
        result *= i
    
    return result


# ============================================================================
# PART 2: Enhanced version using built-in math package
# ============================================================================

import math


def factorial_math(n):
    """
    Calculate the factorial of N using the built-in math library.
    This simplifies the calculation by using math.factorial().
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    """
    # Use built-in math.factorial for cleaner and potentially optimized calculation
    return math.factorial(n)


# Note: Fibonacci series cannot be directly simplified using math library,
# but we can use math library for other enhancements if needed.
# For example, we can use math.sqrt() for Binet's formula (optional advanced approach)


if __name__ == "__main__":
    # Test Part 1: Manual calculations
    print("=" * 60)
    print("PART 1: Manual Calculations (No External Packages)")
    print("=" * 60)
    
    # Test Fibonacci series generation
    n_fib = 10
    print(f"\nFibonacci series of length {n_fib}:")
    fib_series = fibonacci_manual(n_fib)
    print(fib_series)
    
    # Test factorial calculation
    n_fact = 5
    print(f"\nFactorial of {n_fact} (manual calculation):")
    fact_result = factorial_manual(n_fact)
    print(f"{n_fact}! = {fact_result}")
    
    # Test Part 2: Using math library
    print("\n" + "=" * 60)
    print("PART 2: Using Math Library")
    print("=" * 60)
    
    # Test factorial using math library
    n_fact2 = 5
    print(f"\nFactorial of {n_fact2} (using math library):")
    fact_result2 = factorial_math(n_fact2)
    print(f"{n_fact2}! = {fact_result2}")