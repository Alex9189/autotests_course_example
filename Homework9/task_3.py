# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

f = open('test_file/task_3.txt', 'r', encoding='utf-8')
nums = f.read().split('\n\n')
prices = [list(map(int, p.split())) for p in nums if p]
# print(prices)
sums = [sum(lst) for lst in prices]
sorted_sums = sorted(sums, reverse=True)
three_most_expensive_purchases = sum(sorted_sums[:3])
assert three_most_expensive_purchases == 202346
# print(three_most_expensive_purchases)
# for s in sorted_sums:
#     print(s)

# def find_three_most_expensive(file_path):
#     with open(file_path, 'r') as f:
#         prices = f.read().split('\n\n')
#         prices = [list(map(int, p.split())) for p in prices if p]
#
#     flat_prices = [price for sublist in prices for price in sublist]
#     sorted_prices = sorted(flat_prices, reverse=True)
#     three_most_expensive_purchases = sum(sorted_prices[:3])
#
#     return three_most_expensive_purchases


# three_most_expensive_purchases = find_three_most_expensive('test_file/task3.txt')
# print(three_most_expensive_purchases)
# assert three_most_expensive_purchases == 202346
# @func_log()
# # def find_three_most_expensive(file_path):
# #     with
# f = open('test_file/task_3.txt', 'r', encoding='utf-8')
# prices = f.read().split('\n')
# #a = sum(prices, delimiter='')
# #nums = prices.split()
# #print(sum(nums))
# prices = [list(map(int, p.split())) for p in prices if p]
# print(prices)
# flat_prices = [price for sublist in prices for price in sublist]
# sorted_prices = sorted(flat_prices)
# print(flat_prices)
# three_most_expensive_purchases = sum(sorted_prices[:3])
#
# # return three_most_expensive_purchases
#
#
# # three_most_expensive_purchases = find_three_most_expensive('test_file/task3.txt')
# print(three_most_expensive_purchases)