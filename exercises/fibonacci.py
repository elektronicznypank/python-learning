'''Write a program that asks the user how many Fibonacci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonacci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …) -> niech to będzie lista.'''


def fibonacci(amount: int = int(input('Ile liczb Fibonacciego chcesz wygenerować: '))):
    if amount < 1:
        err = 'Argument tej funkcji musi być większy od 0.'
        raise Exception(err)
    a, b = 0, 1  # ja wolę zaczynać od zera
    fibonacci_list = [a]
    for _ in range(amount - 1):
        fibonacci_list.append(b)
        a, b = b, a + b
    return fibonacci_list


print(fibonacci())
