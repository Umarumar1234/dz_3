# Напишите функцию группового переименования файлов. Она должна:
# принимать путь
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. 

# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

# 2.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


# // source
# abcd.png
# fasgasg.py
# 1421af.py

# // out
# func(directory='', name='test', digits=3, extension='.py', out_extension='.txt', save=(2, 4))

# abcd.png
# asgtest001.txt
# 421test002.txt

import os
 # Jupyter - скачать!
def rename(directory: str, name: str, digits: int, extension: str, out_extension: str, range_file_name: tuple[int, int]):
    # 1. Получить список файлов в дериктории
    # 1.2 Отфильтровать только файлы
    # 1.3 Отфильтровать по расширению (заданному)
    # 2. Сформировать желаемое имя:
    #       <range_name>[<name>]<digits>.<out_extension> 
   
    files = os.listdir(directory) # список названий файлов и папок в директории

    # for file in files:
    #     file_path = os.path.join(directory, file) # путь к файлу или папке
    #     if os.path.isfile(os.path.join(directory, file)): #проверка файл или папка (передаем путь к файлу)
    #         if os.path.splitext(file_path)[1] == extension:
    
    files = [file for file in files if os.path.isfile(os.path.join(directory, file)) and  os.path.splitext(file)[1] == extension] #список имен файлов

    for number, file in enumerate(files,1): # x, y = (1, 2)
        start, end = range_file_name
        new_file_name = os.path.splitext(file)[0][start-1:end] # формируем имя нового файла
        new_file_name += name
        new_file_name += f'{number:>0{digits}}' # Формирование нужного номера файла
        new_file_name += out_extension
        file_path = os.path.join(directory,file) # путь к файлу(изначальному)
        new_file_path = os.path.join(directory,new_file_name)
        os.rename(file_path, new_file_path) #передаем старый путь к файлу и путь к нофому файлу(с новым именем)
    

                
        

rename('hw_seminar7/rename', 'test', 3, '.txt', '.py', (1,3))