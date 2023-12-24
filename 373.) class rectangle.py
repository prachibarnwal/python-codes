class Rectangle:
    def __init__(self, leng, br):
        self.leng = leng
        self.br = br
    def area(self):
        print("Area is  : ", self.leng * self.br)
r1 = Rectangle(12,3)
r1.area()
