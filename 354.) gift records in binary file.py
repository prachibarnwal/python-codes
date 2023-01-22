import pickle
def addGift():
    f = open("Gifts.dat","ab")
    gid = int(input("Enter Gift Id : "))
    name = input("Enter Name : ")
    cost = int(input("Enter Cost : " ))
    remarks = input("Enter Remarks : ")
    g = {"ID" : gid, "Name" : name, "COST" : cost, "REMARKS" : remarks}
    pickle.dump(g,f)
    f.close()

def BUMPER():
    f = open("Gifts.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            if data["REMARKS"] == "ON DISCOUNT":
                print(data)
    except:
        f.close()

for i in range(0):
    addGift()
BUMPER()
    
