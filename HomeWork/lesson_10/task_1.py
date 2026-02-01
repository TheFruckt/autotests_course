# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    while True:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        len_1 = random.randint(1, 15)
        len_2 = random.randint(1, 15)

        word_1 = ''.join(random.choice(alphabet) for _ in range(len_1))
        word_2 = ''.join(random.choice(alphabet) for _ in range(len_2))

        yield f'{word_1} {word_2}'
