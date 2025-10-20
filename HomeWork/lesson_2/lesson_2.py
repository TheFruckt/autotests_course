"""
Задание 1

Дано 1 число - сторона квадрата. Напишите программу, которая рассчитает 3 значения:
периметр квадрата, площадь квадрата и диагональ квадрата.
"""


def operations_square(side):
    square = side ** 2
    perimeter = side * 4
    diagonal = side * 2 ** 0.5
    print(f'Площадь квадрата со стороной {side} равна {square}')
    print(f'Периметр квадрата со стороной {side} равен {perimeter}')
    print(f'Диагональ квадрата со стороной {side} равна {diagonal}')


operations_square(12)

"""
Задание 2

Дано квадратное уравнение x^2+bx+c=0.
Дискриминант уравнения должен быть больше 0. 
Напишите программу, которая найдет корни квадратного уравнения и округлит их до 2 знаков после запятой.
"""


def quadratic_equation(b, c, a=1):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (- b + d ** 0.5) / (2 * a)
        x2 = (- b - d ** 0.5) / (2 * a)
        print(f'Корни уравнения {a}*X^2+{b}*X+{c}=0: \nx1 ={x1:.2f} \nx2 ={x2:.2f}\n')
    elif d == 0:
        print(f'Дискриминант равен 0')
    else:
        print(f'Дискриминант = {d} < 0')


quadratic_equation(2, 11)

"""
Задание 3

Дано 2 строки. Напишите программу, которая объединит эти две строки в одну и разделит их 
пробелом, а также поменяет местами первые два символа первой строки на первые два символа 
второй строки и наоборот.
"""


def string_swap(string1, string2):
    string1 = str(string1)
    string2 = str(string2)
    result = f'{string2[0:2]}{string1[2:]} {string1[0:2]}{string2[2:]}'
    print(result)


string_swap('5634', '1278')

"""
Задание 4

Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и корневую папку.
"""


def path_file(path):
    path_part = path.split('\\')
    disc_name = path_part[0]
    file_name = path_part[-1]
    print(f'Имя диска - {disc_name[0]}')
    print(f'Корневой каталог - {path_part[0]}')
    print(f'Имя файла без расширения - {file_name.split(".")[0]}')


path_file(r'C:\Users\pa.remizov\PycharmProjects\AutoTest\lesson_2.py')

"""
Задание 5

Дано 2 числа a и b. Используя форматирование строк, выведите на экран их сумму и произведение 
в форматах ’a + b = c’ и ’a*b = c’.
"""


def formula(a, b):
    c1 = a + b
    c2 = a * b
    print(f'{a} + {b} = {c1}\n{a}*{b} = {c2}')


formula(12, 21)

"""
Задание 6

Дана строка. Напишите программу удаления символов, которые имеют нечетные значения индекса заданной строки.
"""


def symbol(string):
    string = str(string)
    string = string[1::2]
    print(string)


symbol('1234567890')

"""
Задание 7

Дано 2 строки из неповторяющихся символов: первая строка длиной 3 символа, вторая точно 
содержит символы первой строки в любом порядке. Напишите программу, не используя циклы и условия, которая находит 
срез минимальной длины во второй строке, который будет содержать все символы первой строки. Например,
first_string = ‘wtf’ и second_string = ‘brick quz
jmpy veldt whangs fox’, срез минимальной длины: ‘t whangs f’
"""


def find_matches(str1, str2):
    str1 = str(str1)
    str2 = str(str2)

    positions = [str2.find(str1[0])]
    positions += [str2.find(str1[1])]
    positions += [str2.find(str1[2])]

    pos_1 = min(positions)
    pos_2 = max(positions)

    print(str2[pos_1:pos_2+1])


find_matches(123, 'lgk3ru eckm m212dale o1bdaw')
