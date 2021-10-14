#       Практическое задание ко второй лекции
#
#
#Задание 1
#
#Создать список и заполнить его элементами различных типов данных. 
#Реализовать скрипт проверки типа данных каждого элемента. 
#Использовать функцию type() для проверки типа. 
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
#

test_list=[1234567890,1234.567890,True,"String"]
for el in test_list:
    print(el, ' --> ',type(el))

########################################################################################################################################
#Задание 2
#
#Для списка реализовать обмен значений соседних элементов. 
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
#При нечётном количестве элементов последний сохранить на своём месте. 
#Для заполнения списка элементов нужно использовать функцию input().


ListAll= input("Введите значения списка через пробел ").split()    #split() делит данные из input на части через пробел (по умолчанию)
k=int(0)
while k < (len(ListAll)-1):                                        # len(ListAll)-1 потому, что ListAll[k+1]
    ListAll[k],ListAll[k+1]=ListAll[k+1],ListAll[k]                # k=k+2 потому что "перескакиваем" на 2 позиции
    k=k+2                                                 
print(ListAll)


# Функция: "При нечётном количестве элементов последний сохранить на своём месте." получилась сама -собой
########################################################################################################################################
#
#Задание 3
#
#Пользователь вводит месяц в виде целого числа от 1 до 12. 
#Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и dict.
#
#list
import random
month=int(input('Введите порядковый номер месяца '))
if month > 12 or month==0:
    month=random.randint(1,12)
    print("Месяцев 12. Допустим Вы ввели",month)
list_month=["зима","зима","весна","весна","весна","лето","лето","лето","осень","осень","осень","зима"]
print(list_month[month-1])
    
# dict
import random
month=int(input('Введите порядковый номер месяца '))
if month > 12 or month==0:
    month=random.randint(1,12)
    print("Месяцев 12. Допустим Вы ввели",month)
dict_month={12:"зима", 1:"зима",2:"зима", 3:"весна" , 4:"весна", 5:"весна", 6:"лето", 7:"лето", 8:"лето", 9:"осень", 10:"осень", 11:"осень"}
print(dict_month.get(month))

########################################################################################################################################
#
#Задание 4
#
#Пользователь вводит строку из нескольких слов, разделённых пробелами. 
#Вывести каждое слово с новой строки. 
#Строки нужно пронумеровать. 
#Если слово длинное, выводить только первые 10 букв в слове.
user_string=input("Введите строку ").split()
n=1
for el in user_string:
    if len(el) > 10:
        print(n, "-", "{:.10}.".format(el))
        n=n+1
    print(n,"-", el)
    n=n+1
########################################################################################################################################
#
#Задание 5
#
#Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. 
#У пользователя нужно запрашивать новый элемент рейтинга. 
#Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

# Пришлось добавить цикл for для того чтобы преобразовать элементы списка в int. Возможно существует более изящное решение, но я его не нашел
my_list = input("Введите начальные значения списка через пробел ").split()
for i, item in enumerate(my_list):
    my_list[i] = int(item)
my_list=sorted(my_list, reverse = True)
print("Начальные значения списка: ", my_list)

my_list.append(input("Введите новый элемент рейтинга "))
for i, item in enumerate(my_list):
    my_list[i] = int(item)
my_list=sorted(my_list, reverse = True)
print("Конечные значения списка: ", *my_list, sep=" " )

########################################################################################################################################
#
#
#Задание 6
#
#*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
#Каждый кортеж хранит информацию об отдельном товаре. 
#В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: 
#название, цена, количество, единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.
# будет работать только для трех товаров

#Это "обезьяний" вариант. Будет немного времени по пробую сделать лучше с помощью циклов, условий или как нибудь красивее. 
#С возможностью неограниченного кольчества элементов (если это в принципе возможно)

dict_1={"Название товара: ":input("Введите название товара "), "Цена ":input("Введите цену "), "Количество ":input("Введите колличество "), "Единицы измерения ":input("Введите Единицы измерения ")}
dict_2={"Название товара: ":input("Введите название товара "), "Цена ":input("Введите цену "), "Количество ":input("Введите колличество "), "Единицы измерения ":input("Введите Единицы измерения ")}
dict_3={"Название товара: ":input("Введите название товара "), "Цена ":input("Введите цену "), "Количество ":input("Введите колличество "), "Единицы измерения ":input("Введите Единицы измерения ")}
tuple_1=(1, dict_1)
tuple_2=(2, dict_2)
tuple_3=(3, dict_3)
master_list=[tuple_1,tuple_2,tuple_3]
print(master_list)

#Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. 
#Тогда значение — список значений-характеристик, например, список названий товаров.
list_name=[dict_1.get("Название товара: "),dict_2.get("Название товара: "),dict_3.get("Название товара: ")]
list_price=[dict_1.get("Цена "),dict_2.get("Цена "),dict_3.get("Цена ")]
list_num=[dict_1.get("Количество "),dict_2.get("Количество "),dict_3.get("Количество ")]
list_unit=[dict_1.get("Единицы измерения "),dict_2.get("Единицы измерения "),dict_3.get("Единицы измерения ")]
master_dict={"Название товара: ":list_name, "Цена ":list_price, "Количество ":list_num, "Единицы измерения ":list_unit}
print(master_dict)
