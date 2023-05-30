# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
class PersonInfo:# Объявляем класс
    def __init__(self, full_name, age, *departments):# создаем конструктор, который принимает три обязательных аргумента
        self.full_name = full_name
        self.age = age
        self.departments = departments

    def short_name(self):# метод возвращает короткое имя
        last_name, first_name = self.full_name.split()# разделяем строку с именем и фамилией на отдельные слова
        # print (f"{first_name} {last_name[0]}.")
        return f"{first_name} {last_name[0]}."# возвращаем фамилию и первую букву имени

    def path_deps(self):# метод возвращает список департаментов
        return " --> ".join(self.departments)# объединяем подразделения в один путь добавляя специальный разделитель

    def new_salary(self):# метод возвращает новую зарплату
        letters_count = {} # создаем словарь, который будет содержать количество каждой буквы в названии отделов
        for dep in self.departments:# итерируемся по каждому отделу
            for letter in dep: # итерируемся по каждой букве
                if letter in letters_count: # если буква уже в словаре то увеличиваем ее значение на 1
                    letters_count[letter] += 1
                else:
                    letters_count[letter] = 1 # если буквы нет то добавляем в словарь со значением 1
        top_three_letters = sorted(letters_count, key=letters_count.get, reverse=True)[:3] # определяем три наиболее часто встречающиеся буквы, сортируем словарь в порядке убывания и получаем ключи
        sum_top_three_letters = sum([letters_count[l] for l in top_three_letters])# вычисляем сумму количества этих трех наиболее часто встречающихся букв
        # print(letters_count)
        return 1337 * self.age * sum_top_three_letters


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
