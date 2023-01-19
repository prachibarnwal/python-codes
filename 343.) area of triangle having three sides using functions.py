'''
Write a python program using functions to calculate area of
    a triangle after obtaining its three sides
'''
def AREA(A,B,C):
    s = (A + B + C) / 2
    area = (s * (s - A) * (s - B) * (s - C) ) ** 0.5
    print("AREA OF TRIANGLE HAVING SIDES : ",a,", ",b,", ",c," IS ", round(area, 2))
a = eval(input("Enter First Side of Triangle : "))
b = eval(input("Enter Second Side of Triangle : "))
c = eval(input("Enter Third Side of Triangle : "))
AREA(a,b,c)
