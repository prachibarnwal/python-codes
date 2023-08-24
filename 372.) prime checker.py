'''
WAP to accept a number ‘n’ and 
    a. Check if ’n’ is prime 
    b. Generate all prime numbers till ‘n’ 
    c. Generate first ‘n’ prime numbers 
This program may be done using functions
'''
def prime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return 0
    else:
        return 1
def bbb(n):
    for i in range(2,n):
        if prime(i) == 1:
            print(i)
def cjhdg(n):
    num = 2
    nm = 1
    while nm <= n:
        if prime(num) == 1:
            print(num," is Prime")
            nm += 1
        num += 1
        
n = int(input("Enter a Number : "))
xx = prime(n)
if xx == 1:
    print(n," is prime")
else:
    print(n," is not a prime")
print("*"*30)
print("All prime till ",n, " is : ")
bbb(n)
print("*"*30)
print("first ",n," prime are : ")
cjhdg(n)
