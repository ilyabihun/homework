"""
написать функцию определяющая функцию является ли слово паллиндромом
найти сумму в списке чисел реккурсивно
найти реккурсивно отрицательные цифры
вводим число и найти сумму цифр
является ли чило простым (рекурсивно)
проверка является ли число замечательным (73)
возведение числа в степень рекурсивно
из десятичного и двоичного и обратно рекурсивно """
import string
def palindrome(text):
    whitelist = set(string.ascii_lowercase)
    text = text.lower()
    text = ''.join([char for char in text if char in whitelist])
    return text == text[::-1]

def print_palidrome():
    phrase = input('Enter text')
    if palindrome(phrase):
        print('This string is a palindrome')
    else:
        print('Is not palindrome')
    return True
def wonderfuel_number(perfect):
    if prime_number(perfect) and sum_numbers(perfect) == 10 and perfect > 40:
        print('да рабоатет не так как юы хотелось, но работает )))')

def print_sheldon_number():
    number = int(input('Enter number'))
    wonderfuel_number(number)
    return True

def prime_number(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number

def print_prime_number():
    number = int(input('Enter number'))
    if prime_number(number):
        print('This number is prime')
    else:
        print('This number not prime')
    return True
def sum_numbers(num):
    sum_in_def = 0
    while num > 0:
        digit = num % 10
        sum_in_def += digit
        num = num//10
    return sum_in_def

def print_sum_number():
    number = int(input('Enter number'))
    print('This sum your number', sum_numbers(number))


def negative_number(number):
    for elem in number:
        if elem > 0:
            return negative_number
def print_negative_number():
    print('None')
    return True
def print_sum_list_numbers():
    print('None')
    return True
def print_up_number():
    print('None')
    return True
def print_decimal_number():
    print('None')
    return True
def task_exit():
    print('Bye')
if __name__ == "__main__":
    choices = {
        "1": print_palidrome,
        "2": print_sum_list_numbers,
        "3": print_negative_number,
        "4": print_sum_number,
        "5": print_prime_number,
        "6": print_sheldon_number,
        "7": print_up_number,
        "8": print_decimal_number,
        "0": task_exit,
    }

    menu = """
Choose menu option:\n
1. Palidrome
2. Sum list numbers
3. Negative number
4. Sum number
5. Prime number
6. Sheldon(wonderfuel number)
7. Exponentiation
8. Decimal number
0. Exit
    """
    while True:
        menu_number = input(f'{menu}\nEnter menu number - ')
        choice = choices.get(menu_number)
        if not choice:
            print('Enter again')
            continue
        choice()
