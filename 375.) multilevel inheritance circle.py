#multi level inheritance
class Circle():
    def __init__(self,radius):
        self.radius = radius
    def Area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle is : ", area, "\n")

class Cylinder(Circle):
    def __init__(self, radius, height):
        self.height = height
        super().__init__(radius)
    def Area(self):
        area = 2 * 3.14 * self.radius * self.height
        print("Area of Cylinder is : ",area, "\n")

class Cone(Cylinder):
    def __init__(self, radius, height, slant_height):
        self.slant_height = slant_height
        super().__init__(radius, height)
    def Area(self):
        area = 3.14 * self.radius * self.slant_height
        print("Area of Cone is : ", area, "\n")

while True:
    print("Press 1 : Process a Circle")
    print("Press 2 : Process a Cylinder")
    print("Press 3 : Process a Cone")
    print("Press 4 : Exit")
    n = int(input("Enter Your Choice : "))
    if(n == 1):
        r = int(input("Enter Radius of Circle : "))
        circ = Circle(r)
        print("************************************************")
        circ.Area()
    elif(n==2):
        r = int(input("Enter Radius of Cylinder : "))
        h = int(input("Ener Height of Cylinder : "))
        cyl = Cylinder(r, h)
        print("************************************************")
        cyl.Area()
    elif n == 3:
        r = int(input("Enter Radius of Cone : "))
        h = int(input("Enter Height of Cone : "))
        l = int(input("Enter Slant Height of Cone : "))
        con = Cone(r, h, l)
        print("************************************************")
        con.Area()
    elif(n==4):
        break
    else:
        print("Invalid Choice")
        break

