# Практическое задание к пятой лекции
#
#
#Задание 1
#
# Создать программный файл в текстовом формате, 
# записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных будет свидетельствовать пустая строка.
# one_file = open("File_1.txt", "a+") 

one_file = open("File_1.txt", "a+") 
bul = True
while bul == True:
    tmp_str = input()
    if tmp_str == '':
        bul = False
    else:
        one_file.write(tmp_str + '\n')
one_file.close()
        

#
#Задание 2
#
# Создать текстовый файл (не программно), 
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

one_file = open("File_1.txt", "r")  # Читаем фаил из первого задания
str_line = 0
srt_word = 0
for line in one_file:
    srt_word += len(line.split())
    str_line += 1
print("Общее количество слов: " , srt_word,  "\n",  "Общее количество строк: ", str_line)
one_file.close()    


#
#Задание 4
#
# Создать (не программно) текстовый файл со следующим содержимым: 
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.

with open("z4.txt") as str_f1:
    print("Исходный фаил: ", "\n",str_f1.read())
    for line in str_f1:
        line = line.replace("One","Один"). replace("Two","Два"). replace("Three","Три"). replace("Four","Четыре")
        with open("z4f.txt" ,"a+") as str_f2:
            print(line, file = str_f2)
with open("z4f.txt" ) as str_f2:
    print("Конечный фаил: ", "\n",str_f2.read())



#
#Задание 5
#
# Создать (программно) текстовый файл, 
# записать в него программно набор чисел, разделённых пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
sum_file = open("File_5_sum.txt", "w+")
sum_file.write(input("Введите числа через пробел "))
sum_file.close()

with open("File_5_sum.txt") as str1:
    for Line in str1:
        strng_tmp = Line.split(" ")
        result = [int(item) for item in strng_tmp]
    print("Сумма чисел: ", sum(result))
 