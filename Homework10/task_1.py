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
# Здесь пишем код
def generate_random_name():
    while True:
        name = ""
        for i in range(2):
            word = ""
            for j in range(random.randint(1, 15)):
                word += random.choice("abcdefghijklmnopqrstuvwxyz")
            name += word + " "
        yield name.strip()

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


