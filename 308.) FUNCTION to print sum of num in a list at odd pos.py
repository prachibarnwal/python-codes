def BOMBFUTA(L):
    s = 0
    for ch in range(len(L)):
        if ch % 2 != 0:
            s += L[ch]
    if s % 5 == 0:
        print("MAI CHALI JUPITER PE")
    else:
        print("EARTH PE HI JINDA RHO TUM >_<")

L = list(eval(input("Enter a List of NUmbers : ")))
BOMBFUTA(L)
