'''Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
TIP: isupper() function'''


def capital_indexes(string):
    list_of_indexes = []
    for i in range(len(string)):
        if string[i].isupper():
            list_of_indexes.append(i)
    return list_of_indexes


# oneliner


def capital_indexes(string):
    return [i for i, j in enumerate(string) if j.isupper()]
