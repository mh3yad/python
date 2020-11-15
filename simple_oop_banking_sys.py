class User:
    def __init__(self,name,age,total):
        self.name  = name
        self.age = age
        self.total = total
    def show(self):
        print("username: "+self.name + " age is " + int(self.age))   
class Bank(User):
    def __init__(self,name,age,total):
        super().__init__(name,age,total)
        self.amount = None
    def deposit(self,amount):
        self.total +=amount
        
        print("account balance has been updated $ " +  str(self.total))
    def withdrow(self,amount):
        if self.total < amount:
            print("insuffient amount total is $ " + str(self.total))
            return
        self.total -= amount
        return self.total
   
        
bank = Bank("ayad",15,500)
bank.deposit(12)
bank.withdrow(800)    
