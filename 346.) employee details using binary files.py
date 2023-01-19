'''
a binary file 'emp.dat' contains records of eployees in the form
    [eno, ename, salary]
write a program in python to open the binary file 'emp.dat'
    and display only those records where the employee
        salary is greater than 75000
'''
import pickle
def add():
    f = open("emp.dat","wb")
    N = int(input("Enter Number of Employees to Add : "))
    for ch in range(N):
        empno = input("Enter Employee Number : ")
        ename = input("Enter Employee Name : ")
        salary = int(input("Enter Employee Salary : "))
        data = [empno, ename, salary]
        pickle.dump(data,f)
    f.close()
    
def EMPLOYEE():
    f = open("EMP.dat",'rb')
    try:
        while True:
            data = pickle.load(f)
            if data[2] > 75000:
                    print(data)
    except:
        f.close()
add()
EMPLOYEE()
