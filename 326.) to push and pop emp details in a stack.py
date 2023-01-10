'''
WAP to implement stack to store data of an employee
    [empid,name,salary]
    define functions PUSH_EMP() to add an employee
        and POP_EMP() to delete an employee'''
L = []
def PUSH_EMP():
    n = int(input("Enter Number of Employees to Add : "))
    global L
    for ch in range(n):
        eid = int(input("Enter Employee Id : "))
        name = input("Enter Employee Name : ")
        sal = int(input("Enter Employee Salary : "))
        data = [eid,name,sal]
        L.append(data)
def POP_EMP():
    if len(L) == 0:
        print("UNDERFLOW")
    else:
        data = L.pop()
        print(data)

PUSH_EMP()
POP_EMP()
