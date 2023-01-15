'''
WAF to read content of a text file story.txt
    convert the words staring with s to capital
        letters and print the same'''
def MAMCALL():
    f = open("Story.txt")
    data = f.read().split()
    for ch in data:
        if ch[0].lower() == 's':
            ch = ch.upper()
        print(ch,end = ' ')
MAMCALL()
