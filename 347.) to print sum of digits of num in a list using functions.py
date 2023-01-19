'''
QNO 29
Write a user defined function change(L) to accept
    a list of numbers and replace the numbers in the list
        with their sum of digits
'''
def CHANGE(L):
    for i in range(len(L)):
        ch = str(L[i])
        num = 0
        for k in ch:
            num += int(k)
        L[i] = num
    return L
l = list(eval(input("Enter a List of Numbers : ")))
CHANGE(l)
print(l)
