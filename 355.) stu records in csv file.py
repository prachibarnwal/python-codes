import csv
def add():
    f = open("STUDENTS.CSV","w")
    cr = csv.writer(f)
    sid = int(input("Enter Studnet's Id : "))
    sname = input("Enter Student's Name : ")
    scity = input("Enter City : ")
    lis = [sid,sname,scity]
    cr.writerow(lis)
    f.close()
def search():
    f = open("STUDENTS.CSV")
    cr = csv.reader(f)
    for rows in cr:
        if rows[1].lower() == 'ram':
            print(rows)
add()
search()
