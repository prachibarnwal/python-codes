'''
WAF to read from student.csv file and delete the
    student with the given id. file stores
    data in format
        [sid,name,class,marks]
'''
import csv
import os

def DELT():
    f = open("STUDENT.CSV")
    g = open("TEMP.CSV","w")
    ID  = int(input("Enter Student's Id to be Deleted : "))
    cr = csv.reader(f)
    cw = csv.writer(g)
    for rows in cr:
        if len(rows) != 0:
            if int(rows[0]) == ID:
                print(rows)
                print("\tDATA DELETED")
            elif int(rows[0]) != ID:
                cw.writerow(rows)
    f.close()
    g.close()
    os.remove("STUDENT.CSV")
    os.rename("TEMP.CSV","STUDENT.CSV")

DELT()

