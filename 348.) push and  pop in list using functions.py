'''
Write Push(contents) and pop() methods to add
    numbers and remove numbers considering them
        to act as Push and Pop operations of stack
'''
nl = []
def PUSH(contents):
    for ch in contents:
        nl.append(ch)
    return nl
def POP(nl):
    while True:
        if len(nl) == 0:
            print("UNDERFLOW")
            break
        else:
            print(nl.pop())
L = [10,20,30,405]
a = PUSH(L)
print(a)
POP(nl)
