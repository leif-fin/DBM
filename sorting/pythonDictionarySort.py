my_dict = {'banana': 3, 'apple': 2, 'pear': 1, 'orange': 4}

# key
sorted_dict_by_key = dict(sorted(my_dict.items()))
print(sorted_dict_by_key)

# value
sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict_by_value)
