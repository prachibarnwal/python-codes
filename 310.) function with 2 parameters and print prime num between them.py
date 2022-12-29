def listPrime(n1,n2):
    res = []
    for num in range(n1,n2+1):
        f = 0
        for i in range(1,num+1):
            if num % i == 0:
                f += 1
        if f == 2:
            res.append(num)
    return res

a = listPrime(10,20)
print(a)
