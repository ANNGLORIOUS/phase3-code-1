def sort_by_age():
    """Sort a list of tuples (age,name) by age in ascending order"""

    people = [('Alice', 25), ('Bob', 30), ('Charlie', 22), ('David', 28)]


    sorted_people = sorted(people, key=lambda person: person[1])
    return sorted_people

# Test the function
print(sort_by_age())