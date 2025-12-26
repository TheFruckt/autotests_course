# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open('test_file/task_3.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

list_sum = []
purchase_sum = 0
for i in text:
    i = i.strip()
    if i:
        purchase_sum += int(i)
    else:
        list_sum.append(purchase_sum)
        purchase_sum = 0

list_sum.sort(reverse=True)
three_most_expensive_purchases = sum(list_sum[:3])

assert three_most_expensive_purchases == 202346