L = list(eval(input("Enter a List of Numbers : ")))
a = len(str(max(L)))
d = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : []}
num = -1
print("Original List : ",L)
for i in range(1, a + 1):
    for ch in L:
        try:
            k = str(ch)[num]
            d[int(k)].append(ch)
        except:
            k = 0
            d[k].append(ch)
    newd = d
    newl = []
    for var in newd:
        newl.extend(newd[var])
    L = newl
    print("Step ",i," : ",L)
    for number in d:
        d[number] = []
    num -= 1
