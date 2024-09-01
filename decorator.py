def decorator_func(func):
    """
    This is a decorator function that will be applied to any function passed to it.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")

        """Call the original function with any arguments and keyword arguments"""
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def example_function():
    print("we have something inside")

# Call the decorated function
example_function()

# Test the decorator with a function 
@decorator_func
def add_numbers(a, b):
    return a + b

# Call the decorated function with arguments
result = add_numbers(3, 5)
print(f"The result of adding 3 and 5 is: {result}")
