'''
WAF in python to receive a list of names and
    print only those where middle element is 'a' '''
def DONE(l):
    for i in l:
        a = len(i) // 2
        if len(i) % 2 == 0:
            print(i[a-1], i[a])
        else:
            print(i[a])
l = list(eval(input("Enter List of Names : ")))
DONE(l)
