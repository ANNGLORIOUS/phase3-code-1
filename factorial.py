def calculate_factorial(n):
    """Calculate the factorial of a given number n"""
    factorial = 1
    if n < 0:
        print(f"Invalid!! Enter a Positive Integer.")
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range (2, n +1):
            factorial *= i
        return factorial

"""test the function"""  
print(calculate_factorial(5))
print(calculate_factorial(10))
print(calculate_factorial(-5))  