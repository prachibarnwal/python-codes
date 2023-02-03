''' Write a definition of a user defined function PushNV(N)
    which accepts a list of strings in the parameter N
        and pushes all strings which have no vowels present
            in it, into a list named NoVowel.
WAP in Python to input 5 words and Push them one by
    one into a list named A11.
The Program should then use the function PushNV() to create
    a stack of words in the list NoVowel so that is stores only
        those words which do not have any vowel present in it,
            from the list A11. Thereafter, pop each word from the list
        NoVowel and display the popped word. When the stack is
    empty display the message "EmptyStack".   '''
def PushNV(N):
    for ch in N:
        for i in ch:
            if i in 'aeiouAEIOU':
                break
        else:
            A11.append(ch)
def POP(A11):
    a = A11.pop()
    print(a, end = "    ")
NoVowel = list(eval(input("Enter A List Of 5 Words : ")))
A11 = []
PushNV(NoVowel)
while True:
    if len(A11) != 0:
        POP(A11)
    else:
        print("EmptyStack")
        break
