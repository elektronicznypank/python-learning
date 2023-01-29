'''Napisz funkcję, której argumentem będą imię/imiona i nazwisko, a która zwracać będzie samo imię/imiona. Załóżmy, że mogą być maksymalnie 3 imiona, czyli gdy się poda A B, to funkcja zwróci A; gdy się poda A B C, funkcja zwróci A B etc. Przyjmijmy, że nazwisko składa się z jednego wyrazu. Cały argument = jeden string.

Napisz drugą, analogiczną funkcję, podającą samo nazwisko. Przyjmij, że każde nazwisko jest jednym słowem.'''


def show_first_name(a):
    name = a[0:a.index(' ')]
    return name


# to powyżej zadziała tylko z jednym imieniem, poniżej wersja dopasowana do wielu imion:


def show_multiple_first_names(c):
    rev_name = c[::-1]
    surname_in_rev_name = rev_name[0:rev_name.index(' ')]
    surname = surname_in_rev_name[::-1]
    return c.removesuffix(f' {surname}')


# a tutaj wersja podawająca nazwisko:


def show_surname(b):
    rev_name = b[::-1]
    surname_in_rev_name = rev_name[0:rev_name.index(' ')]
    return surname_in_rev_name[::-1]


# to co powyżej, tylko dużo krócej i bardziej pro


def show_surname(d):
    return d.split(' ')[-1]
