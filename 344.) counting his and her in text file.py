'''
WAF CountHisHer() in python which reads the content of
    a text file 'story.txt' and counts the words His and Her
        (not Case Sensitive)
'''
def CountHisHer():
    f = open("NEWSTORY.TXT")
    data = f.read().split()
    his = 0
    for ch in data:
        if ch.lower() == 'his' or ch.lower() == 'her':
            his += 1
    f.close()
    print("NO. OF 'HIS' & 'HER' IN THE FILE IS : ",his)

CountHisHer()
