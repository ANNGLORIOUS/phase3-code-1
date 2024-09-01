def is_even(num):
    """Check if a number is even and return True if it is and False if otherwise"""
    if num % 2 == 0:
      return True
    else:
      return False
    
"""users input"""
num = int(input("Enter a number:"))

"""check if number is even"""
if is_even(num):
  print("true")
else:
  print("false")
