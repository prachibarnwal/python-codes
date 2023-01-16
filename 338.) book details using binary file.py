'''
write a program to input details of 10 books and
    store those in a binary file. Details include
        [bid,name,cost]
    display those books which costs more than 500
'''
import pickle

def STORREE():
    f = open("BOOKS.dat","wb")
    for i in range(4):
        sid = int(input("Enter Book's Id : "))
        name = input("Enter Book Name : ")
        Class = int(input("Enter Book's Cost : "))
        lis = [sid,name,Class]
        pickle.dump(lis,f)
    f.close()
def DISPLAY():
    f = open("BOOKS.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            if data[-1] > 500:
                print(data)
    except:
        f.close()

STORREE()
DISPLAY()
