import csv
import os

f = open("emp.csv",'r')
g = open("temp.csv","w")

cr = csv.reader(f)
cw = csv.writer(g)
for row in cr:
    if int(row[-1]) > 50000:
        print(row)
        row[-1] = int(row[-1]) + 0.12 * int(row[-1])
        cw.writerow(row,g)
    else:
        cw.writerow(row,g)
f.close()
g.close()
os.remove("emp.csv")
os.rename("temp.csv","emp.csv")
