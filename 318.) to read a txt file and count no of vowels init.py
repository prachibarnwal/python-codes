f = open("Birthday.txt")
data = f.read()
c = 0
for i in data:
    if i in 'aeiouAEIOU':
        c += 1
print(c)
f.close()
