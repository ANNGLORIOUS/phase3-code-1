def apply_decorator( func ):
    def wrapper(): 
        print("Decorator Applied")
        func() 
    return wrapper

@apply_decorator 
def decorator_func(): 
    print("I am now Called!")

# Calling the Function
decorator_func()