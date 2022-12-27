'''
write a function in python, which accepts an integer
     list as argument and swaps the elements of every
         location with the following odd location.
         ex : list received is : [12,34,45,56]
         output should be : [34,12,56,45]
'''
def SWAP(L):
    for i in range(0,len(L) - 1,2):
        L[i],L[i+1] = L[i+1],L[i]
    return L

L = list(eval(input("Enter a List of Numebrs : ")))
a = SWAP(L)
print(a)
