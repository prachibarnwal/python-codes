def NEWYEAR(l):
    g = []
    for ch in l:
        if ch > 90:
            g.append('A')
        elif ch > 80:
            g.append('B')
        elif ch > 70:
            g.append('C')
        elif ch > 60:
            g.append('D')
        else:
            g.append('>_<')
    return g

lis = list(eval(input("Enter a List of Marks : ")))
a = NEWYEAR(lis)
print(a)
