# 6.2[32]: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


# Input:
# -5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7- рассматриваемый список
# 2 - начало диапазона
# 10 - конец
# Output:
# 1(9), 3(3), 7(4), 9(10), 10(2), 13(8), 14(10), 19(7)'''

# collect = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] #создаем генератор с произвольным кол-во чисел.
# range_min, range_max = int(input()), int(input())#начало и конец диапазона.
# print(*[f'{i}({collect[i]})' for i in range(len(collect)) if range_min <= collect[i] <= range_max], sep=', ')
# #отбираем по условию