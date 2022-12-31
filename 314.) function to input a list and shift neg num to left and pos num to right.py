def lis(a):
    l = []
    for ch in a:
        if ch < 0:
            l.insert(ch,0)
        else:
            l.append(ch)
    return l
a = list(eval(input("Enter a Lit of Numbers : ")))
b = lis(a)
print(b)
            
