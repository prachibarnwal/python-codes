stk = []
def PUSH(stk):
    n = int(input("Enter Number of Marks to Push : "))
    for i in range(n):
        ch = eval(input("Enter Marks : "))
        stk.append(ch)

def POP(stk):
    if len(stk) == 0:
        print("UNDERFLOW")
    else:
        return stk.pop()
PUSH(stk)
while len(stk) > 0:
    print(POP(stk), end = "     ")
