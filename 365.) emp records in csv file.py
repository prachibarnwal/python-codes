import csv
def SNAMES():
    f = open("empl.csv")
    cr = csv.reader()
    for rows in cr:
        if rows[1][0].lower() == 's':
            print(rows)

    f.close()
SNMAES()
