# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

# Здесь пишем код
class RomanNums:# Объявляем класс
        def __init__(self, roman_num):
                self.roman_num = roman_num

        #@staticmethod
        def from_roman(self):#определяем метод класса
                roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}# создаем словарь, содержащий соответствия между римскими цифрами и арабскими
                result = 0 #инициализируем переменную,которая будет содержать результат преобразования римской цифры в арабскую.
                for i in range(len(self.roman_num)): # итерируемся по всем символам в строке
                        if i > 0 and roman_dict[self.roman_num[i]] > roman_dict[self.roman_num[i - 1]]:#проверяем, является ли текущий символ больше 0 и больше предыдущего символа в строке
                                result += roman_dict[self.roman_num[i]] - 2 * roman_dict[self.roman_num[i - 1]]#Если да, то вычитаем из результата двойное значение предыдущего символа и прибавляем значение текущего символа
                        else:
                                result += roman_dict[self.roman_num[i]]# если текущий символ не больше предыдущего. В этом случае мы просто добавляем значение текущего символа к результату.
                # print(result)
                return result

        def is_palindrome(self):
                #arabic_num = RomanNums.from_roman(self.roman_num)
                arabic_num = self.from_roman()
                return str(arabic_num) == str(arabic_num)[::-1] #преобразуем полученное арабское число в строку. Затем он сравнивает эту строку с ее перевернутой версией и возвращает результат сравнения.
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]


test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
