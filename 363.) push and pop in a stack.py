stk = []
def Push_element(Visitors):
    if 20 >=Visitors[4] >= 15:
        stk.append(Visitors[3])

def Pop_element():
    if len(stk) == 0:
        print('stack is empty')
    else:
        print(stk.pop())
lis = [['305','10/11/2022','Geeta','F',35],
       ['306','10/11/2022','Arham','M',15],
       ['307','11/11/2022','David','M',18],
       ['308','11/11/2022','Madhuri','F',17],
       ['309','11/11/2022','Sikandar','M',13]]
for ch in lis:
    Push_element(ch)
m = 0
f = 0
for ch in stk:
    if ch == 'F':
        f += 1
    else:
        m += 1
while True:
    Pop_element()
    if len(stk) == 0:
        print('stack is empty')
        break
print("Female : ",f)
print("Male : ",m)
