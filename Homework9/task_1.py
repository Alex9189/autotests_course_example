# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path
# print(*a)
# work_dir = Path.cwd()
# path1 = Path ('test_file/task1_answer.txt')
# path2 = Path ('test_file/task1_data.txt')
# abs_path1 = Path(Path.cwd(), path1)
# abs_path2 = Path(Path.cwd(), path2)
# f = open('abs_path2')
# print(f)
# print(abs_path1)
# # print(abs_path2)
# def remove_digits(file_path):
#      with open("test_file/task1_data.txt", 'r', encoding='utf-8') as f:
# f = open('test_file/task1_data.txt')
# print(*f)
#     #     text = f.read()
#     # text_without_digits = ''.join([i for i in text if not i.isdigit()])
#     # with open('abs_path1', 'w') as f:
#     #     f.write(text_without_digits)

# def remove_digits():
#     with open("test_file/task1_data.txt", 'r', encoding='utf-8') as f:
#         text = f.read()
#     text_without_digits = ''.join([i for i in text if not i.isdigit()])
#     with open('test_file/task1_answer.txt', 'w', encoding='utf-8') as f:
#         f.write(text_without_digits)
a = open("test_file/task1_data.txt", 'r', encoding='utf-8')
b = open("test_file/task1_answer.txt", 'w', encoding='utf-8')
text = a.read()
text_without_digits = ''.join([i for i in text if not i.isdigit()])
b.write(text_without_digits)
b.close()
# # Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
