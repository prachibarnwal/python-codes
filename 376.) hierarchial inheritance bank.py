#hierarchial inheritance
class Account():
    def __init__(self, accno, name, bal):
        self.accno = accno
        self.name = name
        self.bal = bal
    def show(self):
        print("\nAccount Number            ", self.accno)
        print("Account Holder's Name     ", self.name)
        print("Available Balance               ", self.bal)

class Saving(Account):
    def __init__(self, accno, name, bal):
        super().__init__(accno, name, bal)
    def Withdraw(self):
        amt = int(input("Enter the Amount to be Withdraw : "))
        if self.bal >= amt:
            print("    !!!  Transaction Successful  !!!")
            self.bal -= amt
            print("Remaining Balance : ", self.bal)
        else:
            print("Insufficient Balance >__<")
    def Deposit(self):
        amt = int(input("Enter the Amount to be Deposited : "))
        print("   !!!  Amount Deposited  !!!")
        self.bal += amt
        print("Total Balance : ", self.bal)

class FD(Account):
    def __init__(self, accno, name, bal, rate, time):
        self.rate = rate
        self.time = time
        super().__init__(accno, name, bal)
    def show(self):
        super().show()
        print("Rate of Interest             ", self.rate)
        print("Maturity Time                ", self.time)
    def showam(self):
        am = self. bal + ((self.bal * self.rate * self.time) / 100)
        print("Amount On Maturity : ",am)

acno = int(input("Enter the Account Number : "))
name = input("Enter Account Holder's Name : ")
bal = int(input("Enter the Initial Amount : "))
rate = int(input("Enter Rate of Interest : "))
time = float(input("Enter Time (in years) : "))
acc = Account(acno, name, bal)
sav = Saving(acno, name, bal)
fd = FD(acno, name, bal, rate, time)

while True:
    print("-----------------------------------------------------------")
    print("Press 1 : Withdraw Money")
    print("Press 2 : Deposit Money")
    print("Press 3 : Show Account Details")
    print("Press 4 : Show FD Details")
    print("Press 5 : Show FD Money")
    print("Press 6 : Exit")
    print("-----------------------------------------------------------")
    n = int(input("Enter a Number : "))
    if n == 1:
        sav.Withdraw()
    elif n == 4:
        fd.show()
    elif n == 5:
        fd.showam()
    elif n == 2:
        sav.Deposit()
    elif n == 3:
        acc.show()
    elif n == 6:
        break
    else:
        print("Invalid Choice")
        break
