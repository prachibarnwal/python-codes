def COLD(a,l):
    for ch in a:
        if ch % 2 == 0:
            l.append(2)
        elif ch % 5 == 0:
            l.append(1)
        elif ch % 7 == 0:
            l.append(2)
        else:
            l.append(3)
    return l
l = []
a = list(eval(input("Enter a List of Numbers : ")))
COLD(a,l)
