# def get_name():
#     return ["Ваня", "Коля", "Миша"]
#
# def get_eng_name():
#     return ["Maicokl", "Eugeniy", "Harry"]
# name_getters = [get_name(), get_eng_name()]
#
# for getter in name_getters:
#     print(getter)
#
# print(get_name.__name__)
# my_func = get_name
# print(my_func())
# print(my_func.__name__)
##############################################################
# def adder(args):
#     res = 0
#     for arg in args:
#         res += arg
#     return res
# def multipleer(args):
#     res = 1
#     for arg in args:
#         res *= arg
#     return res
#
# def proceses_numbers(numbers, funcion):
#     result = funcion(numbers)
#     print(f"Получилась {result}")
#
# my_numbers = [1, 2, 3, 4, 5]
#
#
# proceses_numbers(numbers=my_numbers, funcion=adder)
# proceses_numbers(numbers=my_numbers, funcion=multipleer)

#########################################################################

def mult_by_2(x):
    return x * 2

my_numbers1 = ["1", "2", "3", "4", "5"]
my_numbers = [1, 2, 3, 4, 5]
result = map(mult_by_2, map(int, my_numbers1))# это если нужно преобразовать с помощью функции map число из строки в
result1 = map(mult_by_2, my_numbers)# числа функия map переумнажает каждый элимент в списке не используя цикл
print(result) # чтоб вывести из функии map результат нам не достаточно его вызвать print  нам нужно сделать список как
# указанно ниже
print(list(result)) # Вот так нужно выводить результат после конвертации в список
print(list(result1))

##################################################################################

def is_add(x):
    return x % 2 == 0

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_add, my_list )
print(result)
print(list(result))









