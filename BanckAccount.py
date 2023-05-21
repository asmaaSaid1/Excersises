class BankAccount():
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
   
    def deposit(self,d):
        self.balance+=d
        return self.balance
              
    def withdraw(self,w):
        self.balance-=w
        return self.balance
    
    def check_balance(self):
        return self.balance
        

p1=BankAccount(54,576,"5/5/2023","Hamza")
print(" balance :",p1.check_balance())
print(" balance after deposit :",p1.deposit(87))
print(" balance after withdraw :",p1.withdraw(60))
print(" balance :",p1.check_balance())


        
        
    