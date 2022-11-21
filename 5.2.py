# Напишите программу, которая используя методы csv.reader() и csv.writer() 
# считывает данные data.csv файла и обрабатывает данные:
# -редактирует годы в третьем столбце: 91, 95, 83 преобразует в 1991, 1995, 1983.
# -редактирует написание первой колонки, преобразует написание названий языков в написание большими буквами.
# -добавьте данные о языке javascript: JAVASCRIPT, Brendan Eich, 1995, .js, C#, Microsoft, 2000, .сs
# -вывести результат в консоль. 
# Должен получиться подобно:
# [[Programming language, Designed by, Appeared, Extension],
# [PYTHON, Guido van Rossum, 1991, .py],
# [JAVA, James Gosling, 1995, .java],
# [C++, Bjarne Stroustrup, 1983, .cpp],
# [JAVASCRIPT, Brendan Eich, 1995, .js],
# [С#, Microsoft, 2000, .сs]]
# -Запишите данные в новый файл: data_change_1.csv

import csv
from csv import writer


# редактирует годы в третьем столбце: 91, 95, 83 преобразует в 1991, 1995, 1983.
file_reader = csv.reader(open('data.csv'), skipinitialspace=True)
lines = list(file_reader)
lines[1][2] = '1991'
lines[2][2] = '1983'
lines[3][2] = '1997'

# -редактирует написание первой колонки, преобразует написание названий языков в написание большими буквами.

lines[1][0] = 'PYTHON'
lines[2][0] = 'JAVA'
lines[4][0] = 'JAVASCRIPT'

writer = csv.writer(open('data_1.csv', 'w'), skipinitialspace=True)
writer.writerows(lines)

# -добавьте данные о языке javascript: JAVASCRIPT, Brendan Eich, 1995, .js, C#, Microsoft, 2000, .сs

# list = ['JAVASCRIPT', 'Brendan Eich', '1995', '.js']
# list_2 = ['C#', 'Microsoft', '2000', '.cs']

# with open('data.csv', 'a', newline='') as file_csv:
#     writer_file = writer(file_csv)
#     writer_file.writerow(list)
#     writer_file.writerow(list_2)
#     file_csv.close()
    