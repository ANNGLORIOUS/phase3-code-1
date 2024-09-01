def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

"""test the function"""  
print(calculate_factorial(5))
print(calculate_factorial(10))
print(calculate_factorial(-5))  