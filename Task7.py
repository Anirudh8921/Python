class Bank_Account:
   
    BankName= "SBI Bank"
    ROI=7
    def __init__(self):
        self.Name="Anirudh" 
        self.Amount=10000
        self.Address="Nellore"
        self.AccountNo=123456789
       
       
    def Withdraw(self):
        amount=int(input('Enter the Amount to Withdraw: '))
        if(amount<self.Amount):
         print('your withdrawal Amount :',amount)
        else:
            print('insufficiant Balance')
           
    def Balance(self):
        print('Your Remaining Balance is',self.Amount)
       
    def Deposite(self):
        amount=int(input('Enter the Amount to deposite: '))
        self.Amount=amount+self.Amount
        print('your Deposite Amount is :',amount)
       
       
       
       
def main():
   
    print('Bank Name: ',Bank_Account.BankName)
    print('Rate Of Interest: ',Bank_Account.ROI)
    Bank=Bank_Account()
    value=int(input('press 1 for Balance \n Press 2 for Check Withdraw \n Press 3 for Deposite  '))

   
    if(value==1):
       Bank.Balance()
   
    elif(value==2):
        Bank.Withdraw()
      
    elif(value==3):
        Bank.Deposite()
      
       
    else:
        print('Choose valid value 1/2/3')
   
   
   
if __name__=="__main__":
    main()