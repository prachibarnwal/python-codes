#library import
import mysql.connector as sql
import time
import random as rd

def medicine():
    #function to add a medicine       
    def addmedicine():
        print("😇🙃"*15)
        mid = input("Enter Medicine Id : ")
        name = input("Enter Medicine Name : ")
        mf = input("Enter Name of Manufacturer : ")
        dom = input("Enter Date of Manufacture : ")
        doe = input("Enter Date of Expiry : ")
        mg = input("Enter the Weight (in mg) : ")
        content = input("Enter Content : ")
        price = input("Enter the Price : ")
        qty = input("Enter the Quantity : ")
        print("\nSTORING MEDICINE DETAILS.......")
        time.sleep(2)
        q = "insert into medicine values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (mid,name,mf,dom,doe,mg,content,price,qty)
        cr = mydb.cursor()
        cr.execute(q,data)
        print("\tMedicine Inserted.......!!!!")
        print("👍😎"*15)
        mydb.commit()

    #function to show all medicine
    def showmedicine():
        print("🤩😄"*15)
        q = "select * from medicine"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-"*95)
        print("Id\tName\t\tDate_of_Expiry\t\tPrice\t\tQty")
        print("-"*95)
        for k in res:
            print(k[0],"\t",k[1],"\t\t",k[4],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*95)
        print("\n")

    #function to restock a medicine
    def restock():
        mid = input("Enter the Medicine ID : ")
        qty = input("Enter the Quantity to Add : ")
        q = "update medicine set qty = qty + %s where mid = %s"
        d = (qty,mid)
        cr = mydb.cursor()
        cr.execute(q,d)
        print("\n")
        print("😎😄"*12)
        print("Medicine Restocked......!!")
        print("😎😄"*12)
        print("\n")
        mydb.commit()

    #function to search a medicine
    def search():
        mid = input("Enter the Medicine ID : ")
        q = "select * from medicine where mid = "+mid
        cr = mydb.cursor()
        cr.execute(q)
        k = cr.fetchone()
        if k == None:
            print("\nNo Medicine Available With This ID\n")
            print("😣😣"*15)
        else:
            print("\nMedicine Found......!!")
            print("😀😀"*15)
            print("\n")
            print("-"*95)
            print("Id\tName\t\tDate_of_Expiry\t\tPrice\t\tQty")
            print("-"*95)
            print(k[0],"\t",k[1],"\t\t",k[4],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*95)
        print()

    #Function to delete a medicine
    def deletem():
        mid = input("Enter the Medicine ID : ")
        q = "delete from medicine where mid = "+mid
        cr = mydb.cursor()
        cr.execute(q)
        print("\nMedicine Deleted......!!\n")
        print("😒😒"*15)
        print("\n\n")
        mydb.commit()

    #function for billing
    def billing():
        cname = input("Enter Customer's Name : ")
        date = input("Enter the Date of Purchase (in yyyy_mm-dd) : ")
        amount = 0
        cr = mydb.cursor()
        while True:
            mid = input("Enter Medicine id : ")
            q = "select * from medicine where mid = "+mid
            cr.execute(q)
            res = cr.fetchone()
            if res == None:
                print("\nNo Medicine Available With This ID\n")
                print("😣😣"*15)
            else:
                price = int(res[-2])
                print("Price of Medicine is : ",price)
                qty = int(input("Enter the Quantity to be Purchased : "))
                bill = price * qty
                amount += bill
                print("Amount for Medicine ",amount)
                ans = input("Are There More Medicine to be Purchased : ")
                if ans.lower() == "no":
                    print("Calculating Your Bill ")
                    break
        print("Total Bill Amount is : ",amount)
        q = "insert into bills values(%s,%s,%s,%s)"
        data = ('medical_store',cname,date,amount)
        cr.execute(q,data)
        mydb.commit()
        

    #FUNCTION TO DISPLAY PREVIOUS BILLS
    def displaymed():
        print("🤩😄"*15)
        q = "select * from bills where Store_name = 'medical_store'"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-"*95)
        print("shop_name\tcustomer_name\t\tDate_of_Pur\t\tAmount")
        print("-"*95)
        for k in res:
            print(k[0],"\t",k[1],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*95)
        print("\n")
        
    while True:
        print("😇🙃"*15)
        print("\t\t\tAL Medical Store")
        print("😇🙃"*15)
        print("\n")
        print("Press 1 - Add New Medicine")
        print("Press 2 - Restock a Medicine")
        print("Press 3 - Show All Medicines")
        print("Press 4 - Search a Medicine")
        print("Press 5 - Delete a Medicine")
        print("Press 6 - Billing")
        print("Press 7 - Display Previous Bills")
        print("press 8 - to Exit")
        print("\n")
        opt = int(input("Enter Your Choice : "))
        if opt == 1:
            addmedicine()
        elif opt == 2:
            restock()
        elif opt == 3:
            showmedicine()
        elif opt == 4:
            search()
        elif opt == 5:
            deletem()
        elif opt == 6:
            billing()
        elif opt == 7:
            displaymed()
        elif opt == 8:
            print("THANKS FOR VISITING..!!")
            print("✌😄"*15)
            print("\t\t Have a Medicine-Free Life Ahead")
            print("*"*95)
            break
        else:
            print("You're having only 8 options to choose -___-")
            break

def bakery():
    #Function for adding an item to the menu ...
    def additem():
        print("\n")
        print("😇🙃"*15)
        print("\n")
        cid = input("What's the Code of the Dish You want to add : ")
        cake = input("Which type of Dish you want to add (cake / pizza / pastry / etc (name) : ")
        flavour = input("Enter Flavour of the Dish : ")
        dateofm = input("Enter Date of Manufacture : ")
        weight = input("Enter weight(in grams) : ")
        content = input("Enter Ingredients : ")
        price = input("Enter the Price : ")
        print("\nSTORING FOOD DETAILS.......")
        time.sleep(2)
        q = "insert into bakery values(%s,%s,%s,%s,%s,%s,%s)"
        data = (cid,cake,flavour,dateofm,weight,content,price)
        cr = mydb.cursor()
        cr.execute(q,data)
        print("\nDishh Deatils Inserted.......!!!!")
        time.sleep(1)
        print("👍😎"*15)
        print("\n")
        mydb.commit()
    #Function to refill ingredients or flavour
    def refillitem():
        cid = input("Enter the Code of the Dish whose ingredients/flavour you want to Change  : ")
        print("Press 1 - to change Flavour")
        print("Press 2 - to change their Ingredients")
        print("Press 3 - to goto the main menu")
        a = int(input("What do You want to do : "))
        if a == 1:
            flavour1 = input("What's the new flavour to be replaced : ")
            q = "update bakery set flavour = %s where cid = %s"
            d = (flavour1,cid)
            cr = mydb.cursor()
            cr.execute(q,d)
            print("\n")
            print("😎😄"*12)
            print("FLAVOUR   CHANGED......!!")
            print("😎😄"*12)
            print("\n")
            mydb.commit()
        elif a == 2:
            content1 = input("What's the new Ingredients to be replaced : ")
            q = "update bakery set content = %s where code = %s"
            d = (content1,cid)
            cr = mydb.cursor()
            cr.execute(q,d)
            print("\n")
            print("😎😄"*12)
            print("INGREDIENTS   UPDATED......!!")
            print("😎😄"*12)
            print("\n")
            mydb.commit()
            
        else:
            print("\n")
            
    #Function to show all dish detailss
    def showitems():
        print("🤩😄"*15)
        q = "select * from bakery"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n","-"*95)
        print("Code\tName\t\tflavour\t\tweight\t\tPrice")
        print("-"*95)
        for k in res:
            print(k[0],"\t",k[1],"\t\t",k[2],"\t\t",k[-3],"\t\t",k[-1])
            print("-"*95)
    #Function to search a dish
    def searchitem():
        cid = input("Enter the DISH'S CODE : ")
        q = "select * from bakery where cid = "+cid
        cr = mydb.cursor()
        cr.execute(q)
        k = cr.fetchone()
        if k == None:
            print("\nNo Dish Found With This Code\n")
            print("😣😣"*15)
        else:
            print("\nDish Found......!!")
            print("😀😀"*15,"\n")
            print("-"*95)
            print("Code\tName\t\tflavour\t\tweight\t\tPrice")
            print("-"*95)
            print(k[0],"\t",k[1],"\t\t",k[2],"\t\t",k[-3],"\t\t",k[-1])
            print("-"*95)
       
    #FUNCTION TO DELETE A DISH'S DETAIL
    def deleteitem():
        cid = input("Enter the Code of the Dish to be Deleted : ")
        q = "delete from bakery where cid = "+cid
        cr = mydb.cursor()
        cr.execute(q)
        print("\nDish Deleted......!!\n")
        print("😒😒"*15)
        print("\n\n")
        mydb.commit()

    #Function for making billl......
    def billitem():
        cname = input("Enter Customer's Name : ")
        date = input("Enter the Date of Purchase (in yyyy_mm-dd) : ")
        amount = 0
        cr = mydb.cursor()
        while True:
            code = input("Enter Dish code : ")
            q = "select * from bakery where cid = "+code
            cr.execute(q)
            res = cr.fetchone()
            if res == None:
                print("\nNo Dish Found With This ID\n")
                print("😣😣"*15)
            else:
                price = int(res[-1])
                print("Price of Dish is : ",price)
                qty = int(input("How Many Piece of the Item You Want to Have : "))
                bill = price * qty
                amount += bill
                print("Amount for All Items are : ",amount)
                ans = input("Do You Want to Have More Food in Your House : ")
                if ans.lower() == "no":
                    print("Calculating Your Bill ....... ")
                    time.sleep(2)
                    break
        print("Total Bill Amount to be paid by MR./MISS ",cname," is : ",amount)
        q = "insert into bills values(%s,%s,%s,%s)"
        data = ('bakery',cname,date,amount)
        cr.execute(q,data)
        mydb.commit()
    #FUNCTION TO DISPLAY PREVIOUS BILLS
    def displaybill():
        print("🤩😄"*15)
        q = "select * from bills where Store_name = 'bakery'"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-"*95)
        print("shop_name\tcustomer_name\t\tDate_of_Pur\t\tAmount")
        print("-"*95)
        for k in res:
            print(k[0],"\t",k[1],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*95)
        print("\n")
        
    while True:
        print("😇🙃"*15)
        print("\t\t\tAL Bakery Corner")
        print("😇🙃"*15)
        print("\n")
        print("Press 1 - Add New Item to the Menu")
        print("Press 2 - Refill an item")
        print("Press 3 - Show All Eatables")
        print("Press 4 - Search an Cake/Pizza/Burger")
        print("Press 5 - Delete an Eatable Details")
        print("Press 6 - for Billing of Items")
        print("Press 7 - Display Previous Bills")
        print("press 8 - to Exit")
        print("\n")
        opt = int(input("Enter Your Choice : "))
        if opt == 1:
            additem()
        elif opt == 2:
            refillitem()
        elif opt == 3:
            showitems()
        elif opt == 4:
            searchitem()
        elif opt == 5:
            deleteitem()
        elif opt == 6:
            billitem()
        elif opt == 7:
            displaybill()
        elif opt == 8:
            print("THANKS FOR VISITING..!!")
            print("✌😄"*15)
            print("\t\t Have a Sweet Life Ahead")
            print("*"*95)
            break
        else:
            print("You're having only 8 options to choose -__-")
            break

def grocery():
    #FUNCTION TO ADD A GROCERY
    def addgroc():
        print("😇🙃"*15)
        Pid = input("What's the Code of the Grocery You want to add : ")
        gname = input("Enter Grocery's Name : ")
        manufacturer = input("Enter Name of Manufacturer : ")
        dateofm = input("Enter Date of Manufacture : ")
        dateofexp = input("Enter Date of Expiry : ")
        gtype = input("Enter Which Type of Grocery Product it is (rice,pulse,noodles,etc) : ")
        content = input("Enter Content of the Grocery : ")
        price = eval(input("Enter Price of Cosmetic : "))
        quantity = int(input("Enter The Available Quantity : "))
        print("\nSTORING GROCERY'S DETAILS.......")
        time.sleep(2)
        q = "insert into GROCERY values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (Pid,gname,manufacturer,dateofm,dateofexp,gtype,content,price,quantity)
        cr = mydb.cursor()
        cr.execute(q,data)
        print("\nGrocery Deatils Inserted.......!!!!")
        time.sleep(1)
        print("👍😎"*15)
        mydb.commit()
    #Function to Restock a grocery
    def restockgroc():
        aid = input("Enter the GROCERY'S CODE : ")
        qty = input("Enter the Quantity to Add : ")
        q = "update GROCERY set QUANTITY = QUANTITY + %s where Pid = %s"
        d = (qty,aid)
        cr = mydb.cursor()
        cr.execute(q,d)
        print("\n")
        print("😎😄"*12)
        print("GROCERY Restocked......!!")
        print("😎😄"*12)
        print("\n")
        mydb.commit()
    #FUNCTION TO SHOW ALL GROCERYYY......
    def showgroc():
        print("🤩😄"*15)
        q = "select * from GROCERY"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-"*150)
        print("Code\tNAME\t\tManuf.\t\tDate_of_manu.\t\tDate_of_exp\t\tprice\t\tqty")
        print("-"*150)
        for k in res:
            print(k[0],"\t",k[1],"\t\t",k[2],"\t\t",k[3],"\t\t",k[4],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*150)
        print("\n")
    #Function to search a grocery
    def searchgroc():
        cid = input("Enter the GROCERY'S CODE : ")
        q = "select * from grocery where Pid = "+cid
        cr = mydb.cursor()
        cr.execute(q)
        k = cr.fetchone()
        if k == None:
            print("\nNo Grocery Found With This Code\n")
            print("😣😣"*15)
        else:
            print("\nGrocery Details Found......!!")
            print("😀😀"*15)
            print("\n")
            print("-"*150)
            print("Code\tNAME\t\tManuf.\t\tDate_of_manu.\t\tDate_of_exp\t\tprice\t\tqty")
            print("-"*150)
            print(k[0],"\t",k[1],"\t\t",k[2],"\t\t",k[3],"\t\t",k[4],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*150)
        print()
    #function to delete a grocery
    def deletegroc():
        cid = input("Enter the Code of the Grocery to be Deleted : ")
        q = "delete from grocery where Pid = "+cid
        cr = mydb.cursor()
        cr.execute(q)
        print("\nGrocery Deleted......!!\n")
        print("😒😒"*15)
        print("\n\n")
        mydb.commit()
    #function for billing of PRODUCTSS
    def billgroc():
        cname = input("Enter Customer's Name : ")
        date = input("Enter the Date of Purchase (in yyyy_mm-dd) : ")
        amount = 0
        cr = mydb.cursor()
        while True:
            code = input("Enter Grocery's code : ")
            q = "select * from grocery where Pid = "+code
            cr.execute(q)
            res = cr.fetchone()
            if res == None:
                print("\nNo Grocery Available With This ID\n")
                print("😣😣"*15)
            else:
                price = int(res[-2])
                print("Price of Grocery is : ",price)
                qty = int(input("How Many Piece of this Product You Want to Have with you : "))
                bill = price * qty
                amount += bill
                print("Amount for All Items are : ",amount)
                ans = input("Do You Want to Have More Products with you : ")
                if ans.lower() == "no":
                    print("Calculating Your Bill ....... ")
                    time.sleep(2)
                    break
        print("Total Bill Amount to be paid by MR./MISS ",cname," is : ",amount)
        q = "insert into bills values(%s,%s,%s,%s)"
        data = ('grocery_store',cname,date,amount)
        cr.execute(q,data)
        mydb.commit()

    #FUNCTION TO DISPLAY PREVIOUS BILLS
    def displaybills():
        print("🤩😄"*15)
        q = "select * from bills where Store_name = 'grocery_store'"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-"*95)
        print("shop_name\tcustomer_name\t\tDate_of_Pur\t\tAmount")
        print("-"*95)
        for k in res:
            print(k[0],"\t",k[1],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*95)
        print("\n")

    while True:
        print("😇🙃"*15)
        print("\t\t\tAL   FOOD   FESTIVE")
        print("😇🙃"*15)
        print("\n")
        print("Press 1 - Add New Grocery details to the Mart")
        print("Press 2 - Restock a Grocery details")
        print("Press 3 - Show All Grocery")
        print("Press 4 - Search a Grocery's Details")
        print("Press 5 - Delete a Grocery from the list")
        print("Press 6 - for Billing of Products")
        print("Press 7 - Display Previous Bills")
        print("press 8 - to Exit")
        print("\n")
        opt = int(input("Enter Your Choice : "))
        if opt == 1:
            addgroc()
        elif opt == 2:
            restockgroc()
        elif opt == 3:
            showgroc()
        elif opt == 4:
            searchgroc()
        elif opt == 5:
            deletegroc()
        elif opt == 6:
            billgroc()
        elif opt == 7:
            displaybills()
        elif opt == 8:
            print("THANKS FOR VISITING..!!")
            print("✌😄"*15)
            print("\t\t Have a Foody Life Ahead")
            print("*"*95)
            break
        else:
            print("You're having only 8 options to choose -__-")
            break

def stationary():
    #FUNCTION TO ADD A STATIONARY
    def addstan():
        print("😇🙃"*15)
        sid = input("What's the Code of the Stationary You want to add : ")
        sname = input("Enter Stationary Name : ")
        manufacturer = input("Enter Manufacturer Name : ")
        dateofm = input("Enter Date of Manufacture : ")
        stype = input("Enter which type of  is it (pen,pencil,notebook,color pens,scale,graph,etc..) : ")
        price = eval(input("Enter Price of Stationary : "))
        qty = int(input("How Many Stationary Are There in Stock : "))
        print("\nSTORING STATIONARY'S DETAILS.......")
        time.sleep(2)
        q = "insert into Stationary values(%s,%s,%s,%s,%s,%s,%s)"
        data = (sid,sname,manufacturer,dateofm,stype,price,qty)
        cr = mydb.cursor()
        cr.execute(q,data)
        print("\tStationary Deatils Inserted.......!!!!")
        time.sleep(1)
        print("👍😎"*15)
        mydb.commit()
    #Function to Restock a Stationary
    def restockstan():
        aid = input("Enter the STATIONARY'S CODE : ")
        qty = input("Enter the Quantity to Add : ")
        q = "update STATIONARY set qty = qty + %s where sid = %s"
        d = (qty,aid)
        cr = mydb.cursor()
        cr.execute(q,d)
        print("\n")
        print("😎😄"*12)
        print("Stationary Restocked......!!")
        print("😎😄"*12)
        print("\n")
        mydb.commit()
    #FUNCTION TO SHOW ALL Stationary DETAILS......
    def showstan():
        print("🤩😄"*15)
        q = "select * from Stationary"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-"*150)
        print("Code\tName\t\tManuf.\t\tDate_of_M.\t\tPrice\t\tQty\t\t")
        print("-"*150)
        for k in res:
            print(k[0],"\t",k[1],"\t\t",k[2],"\t\t",k[3],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*150)
        print("\n")
    #Function to search a Stationary
    def searchstan():
        cid = input("Enter the STATIONARY'S CODE : ")
        q = "select * from Stationary where sid = "+cid
        cr = mydb.cursor()
        cr.execute(q)
        k = cr.fetchone()
        if k == None:
            print("\nNo Stationary Found With This Code\n")
            print("😣😣"*15)
        else:
            print("\n Stationary Details Found......!!")
            print("😀😀"*15)
            print("\n")
            print("-"*170)
            print("Code\tName\t\tManuf.\t\tDate_of_M.\t\tPrice\t\tQty\t\t")
            print("-"*170)
            print(k[0],"\t",k[1],"\t\t",k[2],"\t\t",k[3],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*170)
        print()

    #function to delete a Stationary
    def deletestan():
        cid = input("Enter the Code of the Stationary to be Deleted : ")
        q = "delete from Stationary where sid = "+cid
        cr = mydb.cursor()
        cr.execute(q)
        print("\nStationary Deleted......!!\n")
        print("😒😒"*15)
        print("\n\n")
        mydb.commit()
    #function for billing of Stationary
    def billstan():
        cname = input("Enter Customer's Name : ")
        date = input("Enter the Date of Purchase (in yyyy_mm-dd) : ")
        amount = 0
        cr = mydb.cursor()
        while True:
            code = input("Enter Stationary's code : ")
            q = "select * from Stationary where sid = "+code
            cr.execute(q)
            res = cr.fetchone()
            if res == None:
                print("\nNo Stationary Available With This ID\n")
                print("😣😣"*15)
            else:
                price = int(res[-2])
                print("Price of Stationary is : ",price)
                qty = int(input("How Many Piece of this Stationary You Want to Have in Your Bag : "))
                bill = price * qty
                amount += bill
                print("Amount for All Items are : ",amount)
                ans = input("Do You Want to Have More with you (YES/NO): ")
                if ans.lower() == "no":
                    print("Calculating Your Bill ....... ")
                    time.sleep(2)
                    break
        print("Total Bill Amount to be paid by MR./MISS ",cname," is : ",amount)
        q = "insert into bills values(%s,%s,%s,%s)"
        data = ('stationary_shop',cname,date,amount)
        cr.execute(q,data)
        mydb.commit()

    #FUNCTION TO DISPLAY PREVIOUS BILLS
    def displaystan():
        print("🤩😄"*15)
        q = "select * from bills where Store_name = 'stationary_shop'"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-"*95)
        print("shop_name\tcustomer_name\t\tDate_of_Pur\t\tAmount")
        print("-"*95)
        for k in res:
            print(k[0],"\t",k[1],"\t\t",k[-2],"\t\t",k[-1])
            print("-"*95)
        print("\n")
        
    while True:
        print("😇🙃"*15)
        print("\t\t\tAL   PaperGrafixx")
        print("😇🙃"*15)
        print("\n")
        print("Press 1 - Add New Stationary details to the Shop")
        print("Press 2 - Restock a Stationary details")
        print("Press 3 - Show All Stationary")
        print("Press 4 - Search a Stationary's Details")
        print("Press 5 - Delete a Stationary from the list")
        print("Press 6 - for Billing of Products")
        print("Press 7 - Display Previous Bills")
        print("press 8 - to Exit")
        print("\n")
        opt = int(input("Enter Your Choice : "))
        if opt == 1:
            addstan()
        elif opt == 2:
            restockstan()
        elif opt == 3:
            showstan()
        elif opt == 4:
            searchstan()
        elif opt == 5:
            deletestan()
        elif opt == 6:
            billstan()
        elif opt == 7:
            displaystan()
        elif opt == 8:
            print("THANKS FOR VISITING..!!")
            print("✌😄"*15)
            print("\t\t Have a Happy Happy si Stationary wali Life Ahead")
            print("*"*95)
            break
        else:
            print("You're having only 8 options to choose -__-")
            break

#setting connection
mydb = sql.connect(host = "localhost", user = "root", password = "")

#making cursor
cr = mydb.cursor()

#Selecting database
q = "use super_markett"
cr.execute(q)

#login screen
a = rd.randint(1,9)
b = rd.randint(1,9)
c = rd.randint(1,9)
d = rd.randint(1,9)
e = rd.randint(1,9)
num = str(a)+str(b)+str(c)+str(d)+str(e)

print("\t\t",num)
n = int(input("Enter The Number Shown Above : "))
if str(n) == num:
    print("Yayyyiieee...You've Successfully Entered the Market..!!")
    while mydb. is_connected():
        print("🥳🥳🎁"*10)
        print("\n")
        print("\t\t\tAHNOOR SUPER MARKET")
        print("\n")
        print("🥳🥳🎁"*10)
        print("Press 1 - to go to the Bakery  ☆")
        print("Press 2 - to the Grocery Shop ☆")
        print("Press 3 - to go to Medicine Store  ☆")
        print("Press 4 - to go to the Stationary Corner  ☆")
        print("Press 5 - to Exit the Market  ☆\n")
        ch = int(input("Which Shop You Want to Visit : "))
        if ch == 1:
            bakery()
        elif ch == 2:
            grocery()
        elif ch == 3:
            medicine()
        elif ch == 4:
            stationary()
        elif ch == 5:
            print("🙂🙃"*15)
            print("\t\tThanks for Visiting....!!!")
            print("🙂🙃"*15)
            break
        else:
            print("You're Having Only 10 Choices -___-")
            print("Try Again......!!!")
else:
    print("Seems like it's not a human being -__-")
    print("You Can't Enter The Market. SORRY >_____<")
