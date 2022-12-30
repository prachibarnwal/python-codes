'''write a function in python to search and display deatils
    of all those students, whose stream is 'HUMANITIES'
        from pickled file"Student.dat". Assuming the file is
            containing the objects of the following class :
                [admno,name,stream,semester]'''

import pickle
def WRITE():
    f = open("student1.dat","ab")
    n = int(input("Enter Number of Students to Add : "))
    for i in range(n):
        admno = int(input("Enter Admission Number : "))
        name = input("Enter Name : ")
        stream = input("Enter Stream : ")
        sem = input("Enter Semester (1st,2nd,etc) : ")
        lis = [admno,name,stream,sem]
        pickle.dump(lis,f)
    f.close()

def SEARCH():
    f = open("student1.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            if data[2].lower() == 'humanities':
                print(data)
    except:
        f.close()

WRITE()
SEARCH()
