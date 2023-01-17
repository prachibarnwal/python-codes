'''
WAP to store data about courses in a file COURSE.CSV
    details of the course [cid, name, duration, fee]
        a function ADD_COURSE() has to be implemented
            a function DISPLAY() to show all those records
            where fee > 3000
'''
import csv
def ADD_COURSE():
    f = open("COURSES.CSV","w")
    c = int(input("ENter Number of Course to Add : "))
    s = []
    for i in range(c):
        cid = int(input("Enter Courses's Id : "))
        name = input("Enter Course's Name : ")
        duration = input("Enter Duration : ")
        fee = int(input("Enter Fees : "))
        data = [cid,name,duration,fee]
        s.append(data)
    cw = csv.writer(f)
    cw.writerows(s)
    f.close()

def DISPLAY():
    f = open("COURSES.CSV")
    cr = csv.reader(f)
    for rows in cr:
        if len(rows) != 0:
            if int(rows[-1]) > 3000:
                print(rows)
    f.close()

ADD_COURSE()
DISPLAY()
