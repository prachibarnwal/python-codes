n = list(eval(input("Enter a List of Numbers : ")))
print("Original List : ",n)
for i in range(len(n) - 1):
    for j in range(i+1,len(n)):
        if n[i] < n[j]:
            n[i],n[j] = n[j],n[i]
    print("List after ",i+1," step : ",n)
print("Sorted List : ",n)
