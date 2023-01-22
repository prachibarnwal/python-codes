stk = []
def PUSH(stk, dc):
    for k in dc:
        if dc[k] > 75:
            stk.append(k)

def POP(stk):
    if len(stk) == 0:
        print("UNDERFLOW")
    else:
        return stk.pop()
stu = {"OM" : 89,"RK" : 67,"Pricne" : 93}
PUSH(stk,stu)
while len(stk) > 0:
    print(POP(stk), end = "     ")
