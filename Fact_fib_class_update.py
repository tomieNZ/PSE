class MathSeries:
    # No self, no staticmethod

    def __init__(self,n):
        #self is the object instance, n is the argument passed to the method
        # every time the method is called, a new object instance is created
        # edge case: negative numbers
        if n<0:
            raise ValueError("Factorial is not defined for negative numbers.")
        #self.n is the attribute of the object instance
        self.n = n

    def factorial_recursive(self):
        if self.n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if self.n in (0, 1):
            return 1
        # Attention: the object instance is created inside the method
        # Because if dont set the object instance, the method will not be able to access the attribute of the object instance
        # that is not very graceful
        # we can use @staticmethod to avoid creating a new object instance inside the method
        temp_obj = MathSeries(self.n - 1)
        return self.n * temp_obj.factorial_recursive()

    def fibonacci_recursive(self):
        if self.n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if self.n == 0:
            return 0
        if self.n == 1:
            return 1
        # must create a new object instance inside the method
        # Before returning the result, you must create a new object instance
        temp_obj = MathSeries(self.n - 1)
        temp_obj2 = MathSeries(self.n - 2)
        return (temp_obj.fibonacci_recursive() +
                temp_obj2.fibonacci_recursive())

    # New method to print all Fibonacci values up to n
    def fibonacci_series(self):
        series = []
        for i in range(self.n + 1):
            # must create a new object instance inside the method
            temp_obj = MathSeries(i)
            series.append(temp_obj.fibonacci_recursive())
        return series


if __name__ == "__main__":
    n = 5

    # Create an object
    obj1 = MathSeries(n)
    # print the attribute of the object instance
    print(obj1.n)
    # Call using the object (works because no self is expected)
    # ATTENTION: NO ARGUMENT IS PASSED TO THE METHOD
    print("Factorial (recursive):", obj1.factorial_recursive())
    print("Fibonacci (recursive):", obj1.fibonacci_recursive())

    # Print the entire Fibonacci series
    print(f"Fibonacci series (0 to {n}):", obj1.fibonacci_series())