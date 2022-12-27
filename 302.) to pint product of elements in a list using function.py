def product(L):
    p = 1
    for ch in L:
        p *= ch
    print(p)

L = list(eval(input("Enter a List of Numbers : ")))
product(L)
