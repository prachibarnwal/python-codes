class Rectangle():
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        
    def Show(self):
        print("Length of Rectangle is : ",self.length)
        print("Breadth of Rectangle is : ",self.breadth)
        print("\n")

    def Area(self):
        print("Area of Rectangle is : ", self.length * self.breadth)
        print("\n")

class Cuboid(Rectangle):
    def __init__(self, l, b, h):
        self.height = h
        super().__init__(l, b)

    def Show(self):
        print("Length of Cuboid is : ",self.length)
        print("Breadth of Cuboid is : ",self.breadth)
        print("Height of Cuboid is : ",self.height)
        print("\n")

    def Area(self):
        area = 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)
        print("Area of Cuboid is : ", area)
        print("\n")

while True:
    print("Press 1 : Process a Rectangle")
    print("Press 2 : Process a Cuboid")
    print("Press 3 : Exit")
    n = int(input("Enter Your Choice : "))
    if(n == 1):
        l = int(input("Enter Legth of Rectangle : "))
        b = int(input("Enter Breadth of Rectangle : "))
        rect = Rectangle(l, b)
        rect.Show()
        print("************************************************")
        rect.Area()
    elif(n==2):
        l = int(input("Enter Legth of Cuboid : "))
        b = int(input("Enter Breadth of Cuboid : "))
        h = int(input("Enter Height of Cuboid : "))
        cub = Cuboid(l, b, h)
        cub.Show()
        print("************************************************")
        cub.Area()
    elif(n==3):
        break
    else:
        print("Invalid Choice")
        break
