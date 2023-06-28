# define function that compares two dictionaries and return true if they're identical and false if they're not

def deep_equal(dictionary1: dict, dictionary2: dict) -> bool:
    return dictionary1.items() == dictionary2.items()


# tests

test_cases = [
    [{5: 2}, {5: 2}, True],
    [{'5': 2}, {5: '2'}, False],
    [{'5': '2'}, {' 5': '2 '}, False],
    [{'Random key': 'Random value'}, {5: 2, '': ''}, False],
    [{'True': True}, {'True': 'True'}, False],
    [{True: True, False: False}, {True: True, False: False}, True]
]

for index, test_case in enumerate(test_cases):
    print(f'Testing case nr {index + 1}...')
    assert deep_equal(test_case[0], test_case[1]) == test_case[2]
    print(f'Success!')
else:
    print('All tests passed!')