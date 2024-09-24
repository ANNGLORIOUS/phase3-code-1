def sort_by_age(people):
    """Sort a list of tuples (name, age) by age in ascending order"""
    
    sorted_people = sorted(people, key=lambda person: person[1])
    return sorted_people

# Example usage
people_list = [('Alice', 25), ('Bob', 30), ('Charlie', 22), ('David', 28)]
print(sort_by_age(people_list))
