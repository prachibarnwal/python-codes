stk = []
def AddStudent():
    name = input("Enter Student's Name : ")
    phone = input("Enter Phone Number : ")
    stu = [name,phone]
    stk.append(stu)

def PopStudent():
    if len(stk) == 0:
        print("Stack is Empty")
    else:
        print(stk.pop())

n = int(input("How many students are there : "))
for i in range(n):
    AddStudent()
while True:
    PopStudent()
    if len(stk) == 0:
        print("Stack is Empty")
        break
