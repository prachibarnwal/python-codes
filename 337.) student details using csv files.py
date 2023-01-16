'''
Write a function in python to input details of 5 students
    and store them in a csv file. [sid,name,class]
        display only those students who are in class 12
'''
import csv

def STORREE():
    f = open("STU.csv","w")
    cw = csv.writer(f)
    for i in range(2):
        sid = int(input("Enter Student's Id : "))
        name = input("Enter Name : ")
        Class = int(input("Enter Student's Class : "))
        lis = [sid,name,Class]
        cw.writerow(lis)
    f.close()
def DISPLAY():
    f = open("STU.csv","r")
    cr = csv.reader(f)
    for row in cr:
        if len(row)  != 0:
            if row[-1] == '12':
                print(row) 
    f.close()
STORREE()
DISPLAY()
