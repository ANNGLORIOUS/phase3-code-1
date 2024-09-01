def count_vowels(str):
   """returns the count of vowels (a, e, i, o, u) in the string. Ignore case sensitivity """
   vowels = 'aeiouAEIOU'
   return sum(1 for char in str if char in vowels)

"""test the function"""
print(count_vowels('Hello World'))
print(count_vowels('Python'))  
print(count_vowels('coding challenge')) 
print(count_vowels('AnnGlorious mueni'))  
print(count_vowels('éxamplë'))  
print(count_vowels(''))  