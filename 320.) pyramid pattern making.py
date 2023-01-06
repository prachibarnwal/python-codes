for a in range(1,6):
    for b in range(5-a):
        print(" ",end = ' ')
    for n in range(a,0,-1):
        print(n,end = " ")
    for m in range(2,a+1):
        print(m,end=  " ")
    print()
