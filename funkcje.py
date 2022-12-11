from random import randint, sample
from string import printable, whitespace


def gen_strong_password():
    length = int(input('Jak długie ma być hasło (od 8 do 32 znaków): '))
    password = ''.join(sample(printable.replace(whitespace, ''), length))
    # password = ''.join(string.printable.replace(string.whitespace, '') for random.choice in range(length))
    return password


a = randint(1, 11)

print(a)


def format_number(num):
    num_index = 0
    num = str(num)
    rev_num = num[::-1]
    rev_formatted_num = ''
    for i in range(len(num)):
        if num_index % 3 == 0 and num_index != 0:
            rev_formatted_num += ','
        rev_formatted_num += rev_num[num_index]
        num_index += 1
    formatted_num = rev_formatted_num[::-1]
    return formatted_num


def format_number2(num):
    num = str(num)
    rev_num = num[::-1]
    rev_formatted_num = ''
    for i in range(len(num)):
        print(i)
        if i % 3 == 0 and i != 0:
            rev_formatted_num += ','
        rev_formatted_num += rev_num[i]
    formatted_num = rev_formatted_num[::-1]
    return formatted_num


print(format_number(1000000))
print(format_number2(100))


def silnia(n):
    if n > 1:
        return n * silnia(n-1)
    else:
        return 1


print(silnia(4))

d = [4, 4, 6, 8, 2, -1, 5, 5, 7]
print(d)
e = frozenset(d)
print(e)
print(e)
print(e)
f = list(e)
print(f)
print(sorted(f))
f.sort()
print(f)

for _ in range(1, 3):
    print(f'{_}...')
else:
    print('Wydrukowane!')

lista = [1, 2, 3]
tupp = tuple(lista)
print(tupp)

txt: str = '\100 \n tak\\'
print(txt)

for j in 'słowo':
    print(j)
word = "ta"
print(word)
print(len(word))
print('\nsłowo')
for k in range(len(word)):
    print(k)

if word == 'Słowo':
    print('narka')


