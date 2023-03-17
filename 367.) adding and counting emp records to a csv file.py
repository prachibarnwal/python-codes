import csv
def APPEND():
    n = int(input("Enter Number of Employees to Add : "))
    for i in range(n):
        empno = int(input("Enter Employee Number : "))
        name = input("Enter Name : ")
        phone = input("Enter Phone Number : ")
        lis = [empno,name,phone]
        f = open("Myrecord.csv","a")
        cw = csv.writer(f)
        cw.writerow(lis)
        print("Data Added Successfully !!")

def RECCOUNT():
    f = open("Myrecord.csv","r")
    cr = csv.reader(f)
    c = 0
    for rows in cr:
        if rows != []:
            c += 1
    print("Total Number of Records : ",c)
    
        
APPEND()
RECCOUNT()
