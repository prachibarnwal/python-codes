import pickle
def DISPLAY():
    f = open("employee.dat","rb")
    try:
        while True:
            data = pickle.load(data)
            if data['Job'].lower() == 'manager':
                print(data)
    except:
        f.close()
