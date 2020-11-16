class Register:
    def __init__(self,username,password,total):
        self.username = username
        self.password = password
        self.total = total
        print(f"username {username} has been registerd successfully !!!")
        return 
class Login():
    def __init__(self,username,password,register_class):
        self.username = username
        self.password = password
        self.loggedin_users  = []
        
        if(username  == register_class.username):
           print("/./././. checking existence of username /./././.")
           if(password == register_class.password):
                print("logged in successfully !!!")
                self.loggedin_users.append(register_class.username)
           else:
                print("password is incorrect")    
        else:
            print("username is not exist")     

class User:
    def __init__(self,username,login_check,user_data):
        self.username  = username
        if(username  not in login_check.loggedin_users):
            print("username is not logged in yet login and try again ") 
            return
        else:
            self.total = user_data.total
            print(f"welcome {username} your balance is ${self.total}")
    
class Bank(User):
    def __init__(self,user):
        self.user = user
        self.amount = None
    def deposit(self,amount):
        self.user.total +=amount
        
        print("account balance has been updated $ " +  str(self.user.total))
    def withdrow(self,amount):
        if self.user.total < amount:
            print("insuffient amount total is $ " + str(self.user.total))
            return
        self.user.total -= amount
        return self.user.total
   

register =  Register("ayad","123",500)
register =  Register("mido","456",400)
login = Login("ayad","1232",register)
login = Login("mido","456",register)

user = User("mido",login,register)
bank = Bank(user)
bank.deposit(50)
bank.withdrow(300)
