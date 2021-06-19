"""
Домашнее задание №1
Функции и структуры данных
"""


# def power_numbers(*args):
#     list_of_square = []
#     for num in args:
#         list_of_square.append(num ** 2)
#     return list_of_square
#
# power_numbers(1, 2, 3)
#
# #     """
# #     функция, которая принимает N целых чисел,
# #     и возвращает список квадратов этих чисел
# #     >>> power_numbers(1, 2, 5, 7)
# #     <<< [1, 4, 25, 49]
# #     """
# #
# #
# #
# # filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(list_of_numbers):
        list_of_primes =[]
        for i in set(list_of_numbers):
            print("i==",i)
            d = 2
            while i % d != 0:
                print('d=',d)
                print("end",i)
                d+=1
                if i == d:
                    list_of_primes.append(i)
        return list(list_of_primes)

def filter_numbers(list_of_numb, choi):
        if choi == ODD:
                odds = (num for num in list_of_numb if num % 2 == 0)
                return list(odds)
        if choi == EVEN:
                evens = (num for num in list_of_numb if num % 2 != 0)
                return list(evens)
        if choi == PRIME:
                prime = is_prime(list_of_numb)
                return list(prime)

print(filter_numbers([7, 8, 11, 12, 27, 11, 99], "prime"))



#     """
#     функция, которая на вход принимает список из целых чисел,
#     и возвращает только чётные/нечётные/простые числа
#     (выбор производится передачей дополнительного аргумента)
#
#     >>> filter_numbers([1, 2, 3], ODD)
#     <<< [1, 3]
#     >>> filter_numbers([2, 3, 4, 5], EVEN)
#     <<< [2, 4]
#     """
