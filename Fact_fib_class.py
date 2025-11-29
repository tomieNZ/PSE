class MathSeries:
    # @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)

    #generate the series
    #@staticmethod
    def series(n):
        #handle the edge cases
        if n < 0:
            raise ValueError("Series is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        #use a list to store the series
        series = [0,1]
        #loop through the series and generate the next number
        for i in range(2, n):
            next_number = series[i-1] + series[i-2]
            #append the next number to the series
            #for example: [0,1] => after appending 1, it becomes [0,1,1]
            series.append(next_number)
        #return the series
        return series

    # @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2))


if __name__ == "__main__":
    n = 5

    #print("Factorial (recursive):", MathSeries.factorial_recursive(n))
    #print("Fibonacci (recursive):", MathSeries.fibonacci_recursive(n))
    #instantiate the class
    obj = MathSeries()
    print("Fibonacci (recursive):", obj.fibonacci_recursive(n))
    #print the series
    print("Series (recursive):", obj.series(n))