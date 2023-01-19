'''
WAP to accept a filename and a position. Using the
    inputs, call a function SearchFile(Fname, pos) to
        read the contents of the file from the position
            to the end. now display all those words that
                start with 'u' or "U".
'''
def SearchFile(Fname, Pos):
    f = open(Fname+".txt")
    f.seek(Pos)
    data = f.read()
    print(data)
    data = data.split()
    for ch in data:
        if ch[0].lower() == 'u':
            print(ch)
    f.close()
f = input("Enter File Name : ")
p = int(input("Enter Position : "))
SearchFile(f,p)    
