from func import *
from interface import *
import datetime



print("Программа для работы с текстовым файлом \nсодержащим заметки.\n")
file = "bd.csv"
number = interface()
# readfile(file)

while number != 6:
    if number == 1:
        note = input("Введите текст заметки для добавления ") 
        addcontactinfile(note,file)
        number = interface()
    elif number == 2:
        readfile(file)
        number = interface()
    elif number == 3:
        note = input("Введите дату заметки в виде д.м.г например 01.05.2023, дата ") 
        findinfile(note,file)
        number = interface()
    elif number == 4:
        numberstr = input("Введи номер записи для удаления, внимание список будет перенумерован ") 
        if int(numberstr) <= quantstrigfile(file):
            delstringfile(numberstr,file)
            checknumerentry(file)
        else:
            print("Нет такой записи для удаления")
        number = interface()
    elif number == 5:
        numberstr = input("Введи номер записи для изменения ") 
        if int(numberstr) <= quantstrigfile(file):
            note = input("Введи заметку ")
            changefile(note,numberstr, file)
            checknumerentry(file)
        else:
            print("Нет такой запси для изменения")
        number = interface()
 





