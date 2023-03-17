import csv
def copyfile(source,target):
    with open(source,"r") as f:
        g = open(target,"w")
        cr = csv.reader(f)
        cw = csv.writer(g)
        for row in cr:
            cw.writerow(row)
        g.close()

copyfile("furdata.csv","newfurniture.csv")
