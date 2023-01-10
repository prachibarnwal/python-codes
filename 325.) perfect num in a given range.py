def PERFECT(a,b):
    for i in range(a, b + 1):
        c = 0
        for ch in range(1, i):
            if i % ch == 0:
                c += ch
        if c == i:
            print(c)
a = int(input("Enter Lower Range : "))
b = int(input("Enter Upper Range : "))
PERFECT(a,b)
