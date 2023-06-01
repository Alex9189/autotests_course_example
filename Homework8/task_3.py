# Напишите функцию segment
# На вход подается два кортежа с координатами точек (x1, y1), (x2, y2)

# В функции происходит проверка на корректность полученных данных.
# С помощью инструкции try/except as отлавливается исключение Exception. И если это исключение поймано,
# то функция возвращает текст исключения задом наперед (Нужно обратится к атрибуту экзепляра класса Exception)
# Если исключения не произошло, то функция возвращает сумму всех координат


# Здесь пишем код
def segment(coord1, coord2):
    try:
        if not all(isinstance(coord, (int, float)) for coord in coord1 + coord2):
            raise TypeError
        else:
            return sum(coord1) + sum(coord2)
    except Exception as e:
        return str(e)[::-1]
# def segment(point1, point2):
#     try:
#         x1, y1 = point1
#         x2, y2 = point2
#         if isinstance(x1, (int, float)) and isinstance(y1, (int, float)) and isinstance(x2, (int, float)) and isinstance(y2, (int, float)):
#             return x1 + y1 + x2 + y2
#         # else:
#         #     raise TypeError('Координаты должны быть числами')
#     except Exception as e:
#         return str(e)[::-1]
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    ((2, 3), (4, 5)),
    ((2, -3), (4, 5)),
    ((2, 3), ('4', 5)),
    (('a', 3), (4, 5)),
]

test_data = [
    14,
    8,
    "'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu",
    'rts ot )"tni" ton( rts etanetacnoc ylno nac']


for i, d in enumerate(data):
    assert segment(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
