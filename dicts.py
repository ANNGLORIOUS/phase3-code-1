def merge_dicts():
    """merges two dictionaries into a single dictionary. If there are any common keys, their values should be summed up.
"""
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 4, 'c': 6, 'd': 6}

    merged_dict = {**dict1, **dict2}

    for key in merged_dict.keys():
        if key in dict1 and key in dict2:
            merged_dict[key] = dict1[key] + dict2[key]
            
            return merged_dict

merge_dicts()
        
"""test function"""
print(merge_dicts())
