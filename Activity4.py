import math
"""
Part1 - Develop a Python program that uses functions to generate an N-length Fibonacci series and compute the factorial of N. Do not use any external packages in this version. Include clear inline comments to show your understanding, then upload your code to GitHub and share the link.
 
Part2 - For the second version, update your program by using built-in packages such as "Math" to enhance or simplify your calculations. Upload this updated version to GitHub as well.
"""

class fibonacci:
    #initialize the class with the length of the Fibonacci series
    def __init__(self,n):
        self.n = n
    #generate the Fibonacci series
    def series(self):
        if self.n <= 0:
            return []
        elif self.n == 1:
            return [0]
        
        elif self.n == 2:
            return [0,1]
        
        fibonacci_series = [0,1]

        for i in range(2, self.n):
            next_number = fibonacci_series[i-1] + fibonacci_series[i-2]
            fibonacci_series.append(next_number)
        
        return fibonacci_series
    
    #calculate the factorial of the number using the math library
    def factorial(self):
        return math.factorial(self.n)
    
    #calculate the factorial of the number using the manual calculation
    def factorial_manual(self,n):
        if n < 0:
            return []
        elif n == 0 or n == 1:
            return 1
        else:
            par = (n - 1)
            return n * self.factorial_manual(par)


if __name__ == "__main__":
    print("=" * 60)
    print("PART 1: Manual Calculations (No External Packages)")
    print("=" * 60)
    input = int(input("Enter the length of the Fibonacci series: "))
    fib = fibonacci(input)
    print(f"Fibonacci series of length {input}:")
    print(fib.series())
    print(f"Factorial of {input}:")
    print(fib.factorial())
    print(f"Factorial of {input} (manual calculation):")
    print(fib.factorial_manual(input))