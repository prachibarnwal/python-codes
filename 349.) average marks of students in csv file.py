'''
WAF to read from student.csv file and print the
    average marks scored. file stores data in format
        [sid,name,class,marks]
'''
import csv
def AVRG():
    f = open("STUDENT.CSV")
    cr = csv.reader(f)
    su = 0
    c = 0
    for rows in cr:
        if len(rows) != 0:
            su += int(rows[-1])
            c += 1
    marks = su / c
    print("AVERAGE MARKS : ", round(marks, 2))
    f.close()

AVRG()
