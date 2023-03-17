stk = []
def AddCustomer():
    cid = int(input("Enter Customer's Id : "))
    cname = input("Enter Customer's Name : ")
    Customer = [cid,cname]
    stk.append(Customer)

def PopCustomer():
    if len(stk) == 0:
        print("Stack is Empty")
    else:
        print(stk.pop())

AddCustomer()
AddCustomer()
AddCustomer()
while True:
    PopCustomer()
    if len(stk) == 0:
        print("Stack is Empty")
        break
