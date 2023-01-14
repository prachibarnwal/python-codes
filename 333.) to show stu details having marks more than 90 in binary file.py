import pickle
def DISPLAY_STUDENT():
    f = open("student.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            if data[2] > 90:
                print(data)
    except:
        f.close()
DISPLAY_STUDENT()
