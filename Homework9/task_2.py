# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime

# Здесь пишем код
def func_log(file_log='log.txt'):#определяет функцию-декоратор `func_log`, которая принимает необязательный аргумент `file_log` со значением по умолчанию `'log.txt'`
    def decorator(func):#определяет функцию-обёртку `decorator`, которая принимает функцию `func` в качестве аргумента.
        def wrapper(*args, **kwargs):#определяет функцию-обёртку `wrapper`, которая принимает любое количество позиционных и именованных аргументов.
            with open(file_log, 'a') as f:#открывает файл с именем, указанным в переменной `file_log`, в режиме добавления (`'a'`) и создаёт объект файла `f`.
                f.write(f"{func.__name__} вызвана {datetime.datetime.now().strftime('%d.%m %H:%M:%S')}\n")#записывает строку в файл `f`, содержащую имя декорируемой функции, текущую дату и время в формате "день.месяц часы:минуты:секунды"
            return func(*args, **kwargs)#вызывает декорируемую функцию `func` с переданными ей аргументами и возвращает её результат.
        return wrapper#возвращает функцию-обёртку `wrapper`.
    return decorator#возвращает функцию-декоратор `decorator`

@func_log ('mylog.txt')
def my_func():
    print("Hallo, Welt!")

my_func()


# def func_log(file_log='log.txt'):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             with open(file_log, 'a') as f:
#                 f.write(f'{func.__name__} вызвана {datetime.time().strftime("%d.%m %H:%M:%S")}\n')
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @func_log()
# def remove_digits(file_path):
#     with open(file_path, 'r') as f:
#         text = f.read()
#     text_without_digits = ''.join([i for i in text if not i.isdigit()])
#     with open('test_file/task1_answer.txt', 'w') as f:
#         f.write(text_without_digits)
#
#
# @func_log(file_log='func2.txt')
# def some_func():
#     pass
#
#
# remove_digits('test_file/task1.txt')
# some_func()