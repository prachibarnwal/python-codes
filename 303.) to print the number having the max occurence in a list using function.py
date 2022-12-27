def MAXOCCURENCE(L):
    d = {}
    for ch in L:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    a = max(d.values())
    for ch in d:
        if d[ch] == a:
            print(ch)

L = list(eval(input("ENter a List of Numbers : ")))
MAXOCCURENCE(L)
