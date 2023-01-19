def Add(a,b):
    sm = a + b
    print("Sum of ",a,"+",b," is ",sm)
def subtract(a,b):
    choice = int(input("Enter Your Choice ; 1 for first number - second number ; 2 for second number - first number : "))
    if choice == 1:
        diff = a -b
        print("Difference of ",a,"-",b," is ",diff)
    elif ch == 2:
        diff = b - a
        print("Difference of ",b,"-",a," is ",diff)
def multiply(a,b):
    prod = a * b
    print("Product of ",a,"*",b," is ",prod)
def divide(a,b):
    choice = int(input("ENter Your Choice ; 1 for first number / second number ; 2 for second number / first number : "))
    try:
        if choice == 1:
            qt = a / b
            print("Quotient of ",a,'/',b,' is ', round(qt,2))
        elif choice == 2:
            qt = b / a
            print("Quotient of ",b,'/',a,' is ', round(qt,2))
    except:
        print("Division by Zero is Not Possible")

while True:
    a = eval(input("Enter First Number : "))
    b = eval(input("ENter Second Number : "))
    ch = int(input("enter 1 to add ; enter 2 to subtract ; enter 3 to multiply ; enter 4 to divide : "))
    if ch == 1:
        Add(a,b)
    elif ch == 2:
        subtract(a,b)
    elif ch == 3:
        multiply(a,b)
    elif ch == 4:
        divide(a,b)
    else:
        print("Invalid Choice")
    ch2 = input("Enter 'yes' to run again ; 'no' to exit : ")
    c = ch2.lower()
    if c == 'yes':
        pass
    elif c == 'no':
        print("*"*100)
        print("Thanks fo using our calculator")
        print("*"*100)
        break
