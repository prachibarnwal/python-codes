import pickle
def SNAMES():
    f = open("empl.dat","rb")
    n = 0
    m = 0
    try:
        while True:
            row = pickle.load(f)
            m += 1
            if rows[1][0].lower() == 's':
                print(rows)
                n += 1
    except:
        print(n,"/",m)
        f.close()

SNMAES()
