'''
consider a binary file employee.dat containing details
    such as empno:ename:salary (separator ':'). write
         a python function to display details of those
             employees who are earning between 20000
                 and 40000. (both values inclusive)
'''
import pickle
def add():
    f = open("employee.dat","ab")
    N = int(input("Enter Number of Employees to Add : "))
    for ch in range(N):
        empno = input("Enter Employee Number : ")
        ename = input("Enter Employee Name : ")
        salary = input("Enter Employee Salary : ")
        data = empno + ':' + ename + ':' + salary
        pickle.dump(data,f)
    f.close()
def display():
    f = open("employee.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            data = data.split(':')
            if 20000 <= int(data[2]) <= 40000:
                print(data)
    except:
        f.close()
add()
display()
