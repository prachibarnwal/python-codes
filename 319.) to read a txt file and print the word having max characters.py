'''
WAP to read content of a text file 'story.txt'
    and print the word with maximum number
        of characters.'''
f = open("STORY.txt","r")
data = f.read().split()
d = {}
for ch in data:
    d[len(ch)] = ch
print(d)

a = 0
for ch in d:
    if ch > a:
        a = ch
print(d[a])
    
