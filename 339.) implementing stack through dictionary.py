'''WRITE A CODE TO IMPLEMENT A STACK

'''
def PUSH(st):
    n = int(input("Enter No. of Employees to Add : "))
    for i in range(n):
        d = {}
        name = input("ENter Name : ")
        sal = int(input("ENter Salary : "))
        d[name] = sal
        st.append(d)

def POP(ST):
    while True:
        if len(ST) == 0:
            print("UNDERFLOW")
            break
        else:
            print(ST.pop())
st = []
PUSH(st)
POP(st)
