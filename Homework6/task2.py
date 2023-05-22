# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
  msg = 1 # создаем переменную внутри global_function
  def local_function(): # создаем функцию local_function внутри global_function
  # Здесь нужно написать код
      nonlocal msg # используем слово nonlocal для объявления переменной msg как не локальной для функции local_function (а глобальной, она должна существовать)
      msg = 2

  local_function()
  return msg


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
