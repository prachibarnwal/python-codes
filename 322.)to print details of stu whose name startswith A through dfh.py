'''
WAP to read content of a file named 'students.txt'
    and print the details of only those students
        students whose names starts with A.
'''
f = open("students.txt",'r')
data = f.readlines()
for i in data:
    i = i.split()
    if i[0][0].lower() == 'a':
        print(i)
f.close()
