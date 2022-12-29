def prime(a):
    for i in range(2,a):
        if a % i == 0:
            break
        else:
            return a
            
def FONTNAME(A,B):
    l = []
    for ch in range(A,B+1):
        if prime(ch) != None:
            l.append(ch)
    print(l)

a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))
FONTNAME(a,b)
