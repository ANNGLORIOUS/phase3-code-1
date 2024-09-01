def count_vowels(str):
   """returns the count of vowels (a, e, i, o, u) in the string. Ignore case sensitivity """
   vowels = 'aeiouAEIOU'
   return sum(1 for char in str if char in vowels)