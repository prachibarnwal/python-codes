stk = []
def AddStudent(stu):
    if stu[2] == "XII" and stu[3] == "A":
        stk.append(stu[:2])
    

def PopStudent():
    if len(stk) == 0:
        print("Stack is Empty")
    else:
        print(stk.pop())
        
AddStudent(["Rajveer","7586596969959",'XI','B'])
AddStudent(["Swatantra","8879897979","XII","A"])
AddStudent(["Sajal","8877968789","VIII","A"])
AddStudent(["Yash","10101001010","XII","A"])

while True:
    PopStudent()
    if len(stk) == 0:
        print("Stack is Empty")
        break
