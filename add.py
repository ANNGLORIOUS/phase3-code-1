"""Function to calculate the sum of two numbers"""
def add_numbers(num1, num2):
    """Add numbers"""
    return num1 + num2

"""users input"""
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

"""calculate total sum"""
total_sum = add_numbers(num1, num2)

"""print result"""
print(f"The sum of {num1} and {num2} is: {total_sum}")