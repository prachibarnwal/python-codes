'''
a binary file STUDENT.dat has the structure sid,name,mark)
 -write a function SEARCH(Id) to search and
     display the deatils of a particular student whose
         id is passed as parameter to the function.
-write a function DISPLAY() to count total number
    of student getting mark > 90
'''

import pickle
def WRITE():
    f = open("STUDENT.dat","ab")
    n = int(input("Enter Number of Student to Add in the List : "))
    for ch in range(n):
        sid = int(input("Enter Student Id : "))
        name = input("Enter Student Name : ")
        marks = int(input("Enter Student's Marks : "))
        data = (sid,name,marks)
        pickle.dump(data,f)
    f.close()

def SEARCH(Id):
    f = open("STUDENT.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            if data[0] == Id:
                print(data)
    except EOFError:
        f.close()

def DISPLAY():
    f = open("STUDENT.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            if data[2] > 90:
                print(data)
    except EOFError:
        f.close()
        
WRITE()
Id = int(input("Enter Student's Id to be Searched : "))
SEARCH(Id)
print("\n")
DISPLAY()
