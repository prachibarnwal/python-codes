a = 'this is a sample file'
a = list(a.split())
for i in range(len(a) - 1, -1, -1):
    print(a[i], end = '  ')
