'''
WAP to read content of a text file and print
    only those who have got marks above 90'''
f = open("students.txt")
data = f.readlines()
for ch in data:
    ch = ch.split()
    if int(ch[2]) > 90:
        print(ch)
f.close()
