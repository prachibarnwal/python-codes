import csv
def AddRecord():
    n = int(input("Enter Number of Furnitures to Add : "))
    for i in range(n):
        fid = int(input("Enter Furniture Id : "))
        fname = input("Enter Furniture's Name : ")
        fprice = input("Enter Furniture's Price : ")
        lis = [fid,fname,fprice]
        f = open("furdata.csv","w")
        cw = csv.writer(f)
        cw.writerow(lis)
        print("Data Added Successfully !!")

def SearchRecord():
    f = open("furdata.csv","r")
    cr = csv.reader(f)
    for rows in cr:
        if rows != [] and int(rows[-1]) > 3500:
            print(rows)
    
        
AddRecord()
SearchRecord()
