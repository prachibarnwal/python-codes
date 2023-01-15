import pickle
import os
def THANKS():
    f = open("PRODUCT.DAT")
    g = open("temp.dat","wb")
    while True:
        try:
            data = pickle.load(f)
            data[-1] += 0.10 * data[-1]
            pickle.dump(data,g)
        except:
            f.close()
            g.close()
    os.remove("PRODUCTS.dat")
    os.rename("temp.dat","PRODUCT.dat")
THANKS()
