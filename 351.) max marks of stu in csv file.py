'''
WAF to read from student.csv file and print the
    highest marks scored in class 12. file stores
    data in format
        [sid,name,class,marks]
'''
import csv
def AVRG():
    f = open("STUDENT.CSV")
    cr = csv.reader(f)
    su = 0
    for rows in cr:
        if len(rows) != 0:
            if int(rows[2]) == 12:
                if int(rows[-1]) > su:
                    su = int(rows[-1])
    f.close()
    print(su)

AVRG()
