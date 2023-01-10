'''
WAF in python to read content of a text file name story.txt
    and display only those words which have more than 4 letters'''
def FILEE():
    f = open("story.txt","r")
    data = f.read().split()
    for i in data:
        if len(i) > 4:
            print(i)

FILEE()
