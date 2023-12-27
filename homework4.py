my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}

print("Последний элемент кортежа:", my_dict['tuple'][-1])

my_dict['list'].append('new_item')
del my_dict['list'][1]

my_dict['dict'][('i am a tuple')] = 'new_value'
key_to_delete = next(iter(my_dict['dict']))
del my_dict['dict'][key_to_delete]

my_dict['set'].add('new_set_item')
my_dict['set'].discard(next(iter(my_dict['set'])))

print("Измененный словарь", my_dict)