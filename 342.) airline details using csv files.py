'''
WAP to store the information about airlines in a
    csv file and display only those flight details
        which are going to sydney.
 flight details should be like :
     [flight id, strting. destination, dept_time]
 '''
import csv
def FLIGHT():
    f = open("AIRLINES.CSV","w")
    l = []
    cw = csv.writer(f)
    n = int(input("Enter Number of Records to Add : "))
    for i in range(n):
        f_id = int(input("Enter Flight Id : "))
        starting = input("Enter Starting Location : ")
        dest = input("Enter Final Destination : ")
        dept_time = input("Enter Departure Time : ")
        lis = [f_id, starting, dest, dept_time]
        l.append(lis)
    cw.writerows(l)
    f.close()

def SYDNEY():
    f = open("AIRLINES.CSV","w")
    cr = csv.reader(f)
    for rows in cr:
        if len(rows) != 0:
            if rows[-2].lower() == 'sydney':
                print(rows)
    f.close()

FLIGHT()
SYDNEY()
