# Write a function that checks if a string is a palindrome.

from string import punctuation as pct


def if_string_is_palindrome(string: str = input('Podaj ciąg liter i/lub cyfr, który chcesz sprawdzić: ')):
    for i in string[::-1]:
        if i in pct:
            string = string.replace(i, '')
    rev_string: str = string[::-1]
    if string == '':
        return 'String jest pusty.'
    else:
        return 'Podany ciąg liter jest palindromem.'\
            if rev_string.lower() == string.lower()\
            else 'Podany ciąg liter nie jest palindromem.'


print(if_string_is_palindrome())