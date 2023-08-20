from func import *
from interface import *
import datetime

print("Программа для работы с текстовым файлом \nсодержащим ФИО и номер телефона.\n")
file = "bd.csv"
print(quantstrigfile(file))
readfile(file)

 
datainput = datetime.datetime.today()
print(datainput.strftime("%Y-%m-%d %H:%M:%S"))