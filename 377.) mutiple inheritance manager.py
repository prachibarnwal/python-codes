class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

class Employee:
    def __init__(self, empid, dept):
        self.empid = empid
        self.dept = dept
    def show(self):
        print("Employee Id : ",self.empid)
        print("Employee's Department : ", self.dept)
        
class Manager(Person, Employee):
    def __init__(self, name, age, empid, dept, gender):
        self.gender = gender
        Person.__init__(self, name, age)
        Employee.__init__(self,empid,dept)
    def show(self):
        Person.show(self)
        Employee.show(self)
        print("Gender is : ", self.gender)
        
name = input("Enter Name : ")
age = int(input("Enter Age : "))
empid = int(input("Enter Employee's Id : "))
dept = input("Enter Department : ")
gender = input("Enter Gender (M/F) : ")
m1 = Manager(name, age, empid, dept, gender)
m1.show()
