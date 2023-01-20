import csv
def add():
    f = open("MOBILES.CSV","a")
    cw = csv.writer(f)
    modelno = input("Enter Model Number : ")
    name = input("Enter Model Name : ")
    manuf = input("Enter Manufacturer Name : ")
    price = input("Enter Price : ")
    data = [modelno,name,manuf,price]
    cw.writerow(data)
    f.close()
def display():
    with open("MOBILES.CSV","r") as f:
        cr = csv.reader(f)
        for rows in cr:
            if len(rows) != 0 and rows[-2].lower() == 'apple':
                print(rows)
while True:
    print("Press 1 - to add")
    print("Press 2 - to show apple products")
    print("press 3 - to exit")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        add()
    elif ch == 2:
        display()
    else:
        break
        
