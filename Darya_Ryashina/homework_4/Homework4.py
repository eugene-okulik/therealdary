my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'},
    'set': {1, 2, 3, 4, 5}
}

print("Последний элемент кортежа:", my_dict['tuple'][-1])

my_dict['list'].append(6)
del my_dict['list'][1]

my_dict['dict'][('i am a tuple',)] = "tuple value"
my_dict['dict'].pop('key1')


my_dict['set'].add(6)
my_dict['set'].remove(1)

print("Обновленный словарь:", my_dict)
