'''
WAP to read content of a text file named
    student.txt and print the number of C.S.
        student
'''
f = open("students.txt","r")
data = f.readlines()
c = 0
for i in data:
    i = i.split()
    if i[1] == 'C.S.' or i[1] == 'c.s.':
        c += 1
print("Number of Students Having C.S. are : ",c)
f.close()
