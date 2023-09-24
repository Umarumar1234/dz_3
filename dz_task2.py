# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата

# num = int(input('Введите число в десятичной системе: '))
# print(f'Встроенная функция hex -> \t\t{hex(num)}')


# 7 # base 10 (0, 1, 2, ..., 9)
# 4

# 111 # base 2 (7)
# 100 # base 2 (4)

# # base 2
# 100 4
# 101 5
# 110 6
# 111 7
# 1000 8
# 1001 9
# 1010 10
# 1011

# # base 16
# # 0, 1, 2, 3, 9, a (10), b (11), c (12), d (13), e (14), f (15)

# # 15 -> f
# # 16 -> 10

# # 135 (base 2)
# 135 | 2 (1)
#  67 | 2 (1)
#  33 | 2 (1)
#  16 | 2 (0)
#   8 | 2 (0)
#   4 | 2 (0)
#   2 | 2 (0)
#   1 | 2 (1)

# 135 -> 10000111

# # 135 (base 16)
# 135 | 16 (7)
#   8 | 16 (8)
#   0 | 16 (0)

# 135 -> 87

# ... + 8 * 16^1 + 7 * 16^0

# def to_hex(num: int) -> str:
#     alphabet = '0123456789abcdef'
#     result = ''
#     while num != 0:
#         index = num % 16
#         num //= 16
#         result = alphabet[index] + result
#     return result

# user_num = int(input('Введите целое неотрицательное число: '))

# print(to_hex(user_num))

# print((hex(user_num)[2:]))

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

# 4/6
# 11/12

# Sum: 4/6 + 11/12 = 8/12 + 11/12 = 19/12
# Mul: 4/6 * 11/12 = 4 * 11 / 6 * 12 = 44/72 = 11/18


# from math import gcd


# Fraction = tuple[int, int]

# def reduce(fract: Fraction) -> Fraction:
    # НОД (GCD - Greatest Common Divisor)
    # Euclidian Algorithm
    # div = gcd(*fract)
    # return fract[0] // div, fract[1] // div

# https://skysmart.ru/articles/mathematic/slozhenie-drobej

# def summ(a: Fraction, b: Fraction) -> Fraction:
#     if a[1] == b[1]:
#         return reduce((a[0] + b[0], b[1]))
#     return reduce(((a[0] * b[1]) + (b[0] * a[1]), a[1] * b[1]))

# def mult(a: Fraction, b: Fraction) -> Fraction:
#     return reduce((a[0] * b[0], a[1] * b[1]))

# user_fract1 = input('дробь вида “a/b”').split('/')
# user_fract2 = input('дробь вида “a/b”').split('/')

# fract1 = tuple([int(num) for num in user_fract1])
# fract2 = tuple([int(num) for num in user_fract2])

# print(summ(fract1, fract2), mult(fract1, fract2))

# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# bank = 0
# count = 0
# percent_take = 0.015
# percent_add = 0.03
# percent_tax = 0.01


# def add_bank(cash: float) -> None:
#     global bank
#     global count
#     bank += cash
#     count += 1
#     if count % 3 == 0:
#         bank = bank + percent_add * bank
#         print("начислены проценты в размере: ", percent_add * bank)

# def take_bank(cash: float) -> None:
#     global bank
#     global count
#     bank -= cash
#     count += 1

#     if cash*percent_take < 30:
#         bank -= 30
#         print("списаны проценты за cash: ", 30)
#     elif cash*percent_take > 600:
#         bank -= 600
#         print("списаны проценты за cash: ", 600)
#     else:
#         bank -= cash * percent_take
#         print("списаны проценты за cash: ", cash * percent_take)
#     if count % 3 == 0:
#         bank = bank + percent_add * bank
#         print("начислены проценты в размере: ", percent_add * bank)


# def exit_bank():
#     print("Рады вас видетеь снова!\n")
#     exit()

# def check_bank() -> int:
#     while True:
#         cash = int(input("Введите сумму опреации кратно 50\n"))
#         if cash % 50 == 0:

#             return cash


# while True:
#     action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 -выйти\n")

#     if action == '1':
#         if bank > 5_000_000:
#             bank = bank - bank * percent_tax
#             print ("списан налог на богатство: ", bank * percent_tax)
#         cash = check_bank()
#         if cash < bank:
#             take_bank(cash)
#         else:
#             print("no money\n")
#         if bank > 5_000_000:
#             bank = bank - bank * percent_tax
#             print ("списан налог на богатство: ", bank * percent_tax)
#         print("Баланс = ", bank)
#     elif action == '2':
#         add_bank(check_bank())
#         if bank > 5_000_000:
#             bank = bank - bank * percent_tax
#             print ("списан налог на богатство: ", bank * percent_tax)
#         print("Баланс = ", bank)
#     elif action == '3':
#         print("Баланс = ", bank)
#     else:
#         exit_bank()