from functools import reduce 

## Вывод квадрата числа и округление до 3 знаков после запятой с помощью map
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

## Вывод только тех имён, которые меньше или равны 7 буквам с помощью filter
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

## Использование reduce, чтобы вывести произведение этих чисел
my_numbers = [4, 6, 9, 23, 5]


map_result = list(map(lambda x: round(x ** 2, 2), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)