# Write a function that checks if string is palindrome.

def if_string_is_palindrome(string: str = input('Podaj ciąg znaków, które chcesz sprawdzić: ')):
    rev_string: str = string[::-1]
    if string == '':
        return 'String jest pusty.'
    else:
        return 'Podany ciąg znaków jest palindromem.' \
            if rev_string.lower().replace(' ', '').replace('.', '') == string.lower().replace(' ', '').replace('.', '')\
            else 'Podany ciąg znaków nie jest palindromem.'


print(if_string_is_palindrome())
