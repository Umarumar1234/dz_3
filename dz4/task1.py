# # 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# a = int(input('Введите сторону а: '))
# b = int(input('Введите сторону b: '))
# c = int(input('Введите сторону с: '))

# def side_compare(x, y, z):
#     if (x + y > z) and (x + z > y) and (y + z > x):
#         return True
#     else:
#         return False
# def triangle_type(x, y, z):
#     if x == y and x == z and z == y:
#         return 1
#     elif x == y or x == z or z == y:
#         return 0
#     else:
#         return False

# if not side_compare(a, b, c):
#     print('Такой треугольник не существует: ')
# else:
#     print('Такой треугольник существует')

# if triangle_type(a, b, c) == 1:
#     print('Треугольник равносторонний')
# if triangle_type(a, b, c) == 0:
#     print('Треугольник равнобедренный ')

# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# def is_prime(number):
#     count = 0
#     for num in range(1, number + 1):
#         if number % num == 0:
#             count += 1
#     if count == 2:
#         return True
# flag = True    
# while flag:
#     user_num = int(input('Введите число от 1 до 100000: '))
#     if 100000 > user_num > 0:
#         flag = False
#     else:
#         print('Ошибка! Введено неверное число')
# if is_prime(user_num):
#     print('Число простое')
# else:
#     print('Число составное')


# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


# from random import randint

# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000
# attempts = 10

# Загадываем случайное число
# secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

# print("Привет! Я загадал число от 0 до 1000. Попробуй угадать его за 10 попыток!")

# for attempt in range(1, attempts + 1):
#     guess = int(input(f"Попытка {attempt}. Введите вашу догадку: "))
    
#     if guess < secret_number:
#         print("Загаданное число больше.")
#     elif guess > secret_number:
#         print("Загаданное число меньше.")
#     else:
#         print(f"Поздравляю! Вы угадали число {secret_number} за {attempt} попыток.")
#         break

# if secret_number != guess:
#     print(f"Извините, вы исчерпали все попытки. Загаданное число было {secret_number}.")
