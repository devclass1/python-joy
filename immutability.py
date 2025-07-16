# Valid dictionary with immutable keys
valid_dict = {
    'name': 'Amit',       # string key (immutable)
    42: 'The Answer',      # integer key (immutable)
    (1, 2): 'Tuple key'    # tuple of immutables (immutable)
}

print("Valid dictionary:")
print(valid_dict)
print(valid_dict['name'])
print(valid_dict[42])
print(valid_dict[(1, 2)])

# Trying to use mutable types as keys will raise TypeError
try:
    invalid_dict = {
        ['list_key']: 'This will fail'  # list is mutable
    }
except TypeError as e:
    print("\nError when using list as key:")
    print(f"TypeError: {e}")

try:
    invalid_dict = {
        {'set_key'}: 'This will fail'  # set is mutable
    }
except TypeError as e:
    print("\nError when using set as key:")
    print(f"TypeError: {e}")

# However, dictionary VALUES can be mutable
dict_with_mutable_values = {
    'list_value': [1, 2, 3],
    'dict_value': {'a': 1, 'b': 2},
    'set_value': {4, 5, 6}
}

print("\nDictionary with mutable values:")
print(dict_with_mutable_values)
