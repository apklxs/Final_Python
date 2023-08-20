import datetime



def quantstrigfile(file):
    data = open(file, encoding = "utf-8")
    j = 0
    for i in data:
        j = j + 1
    data.close
    return j
        

def readfile(file):
    data = open(file, encoding = "utf-8")
    print(data.read(), end="")
    print()
    data.close

def findinfile(note,file):
    data = open(file, encoding = "utf-8")
    j = quantstrigfile(file)
    k = 0
    for i in range(j):
        strfile = data.readline() 
        if note in strfile[strfile.find(' ')+1:][0:strfile[strfile.find(' ')+1:].find(' ')+1]:
            print(strfile, end = "")
            k = k + 1
    print(f"\n Найдено совпадений {k}")
    data.close

def addcontactinfile(addinfo,file):
    data = open(file, "a", encoding = "utf-8")
    datainput = (datetime.datetime.today()).strftime("%d.%m.%Y %H:%M:%S")
    data.write("\n"+str(quantstrigfile(file)+1) + ".; " + datainput + ";-->" + addinfo) 
    print(f"добавлена информация {addinfo}")
    data.close

def delstringfile(numberstr,file):
    data = open(file,"r",encoding = "utf-8")
    listfile = data.readlines()
    data.close
    data = open(file,"w",encoding = "utf-8")
    for i in listfile:
        if i[:i.find(';')] != str(numberstr)+".":
           data.write(i)
    data.close

def checknumerentry(file):
    data = open(file, encoding = "utf-8")
    listfile1 = data.readlines()
    data.close
    data = open(file,"w",encoding = "utf-8")
    j = 0
    for i in listfile1:
        j = j + 1
        data.write(str(j)+".;"+i[i.find(' '):])
    data.close

def changefile(note,numberstr, file):
    data = open(file,"r",encoding = "utf-8")
    listfile = data.readlines()
    data.close
    data = open(file,"w",encoding = "utf-8")
    print()
    for i in listfile:
        if i[:i.find(';')] == str(numberstr)+".":
            print(f"заменена запись {i}")
            i = i[:i.find('>')+1] + note + "\n"
        data.write(i)
    data.close

def delemptystringfile(file):
    data = open(file,"r",encoding = "utf-8")
    listfile = data.readlines()
    data.close
    listfile = [i for i in listfile if i.strip()]
    data = open(file,"w",encoding = "utf-8")
    data.writelines(listfile)
    """ for i in listfile:
        if i != "\n":
           data.write(i) """
    data.close