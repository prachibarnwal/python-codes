def SORTED(L):
    a = L[0]
    for ch in L:
        if ch < a:
            print("NOT A SORTED LIST")
            break
        a = ch
    else:
        print("SORTED LIST")

l = list(eval(input("Enter a List of Numbers : ")))
SORTED(l)


