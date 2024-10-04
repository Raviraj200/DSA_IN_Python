class Atm:
    # Constructor
    counter = 1
    def __init__   (self):
        self.__pin=""
        self.__balance=0
        # print(id(self))
        self.sno=Atm.counter
        Atm.counter=Atm.counter+1
        # self.__menu()
    def getData(self):
        return self.__pin 
    def setData(self,value):
        self.__pin=value       
        
    def __menu(self):
        user_input = input('''
        Hello How would you like to proced?
        1. Enter For Create __pin
        2.Enter For deposit
        3.Enter For Withdraw
        4.Enter for Check __balance
        5.Enter for Exit
        ''')
        if user_input =="1":
            self.Create___pin()
        elif user_input == "2":
        
            self.Deposit()    
        elif user_input=="3":
            self.WithDraw()
        elif user_input=="4":
            self.Check___balance() 
        else:
            print("Bye")      
    def Create___pin(self):
        self.__pin = input("Enter your __pin")
        print("__pin Set Succ")

    def Deposit(self):
        temp=int(input("Enter your __pin"))
        if temp==self.__pin:
            amount = input("Enter the Amount")
            self.__balance = self.__balance+amount   
            print("Deposit Succ")
        else:
            print("Invalid __pin")     
    def WithDraw(self):
        temp =input("Enter your __pin")
        if temp == self.__pin:
            amount = input("Enter the Amount")
            if amount<self.__balance:
                self.__balance-=self.__balance
                print("WithDraw Succ"+ "\n __balance is "+self.__balance)
            else:
                print("Insufficient Funds")    
        else:
            print("Invalid __pin")
    def Check___balance(self):
        temp = input("Enter your __pin")
        if temp==self.__pin:
            print(self.__balance)
        else:
            print("invalid __pin")    

# sbi is reference variable
sbi =Atm()
print(sbi.sno)




