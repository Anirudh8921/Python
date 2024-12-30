class Menu:
   
    def __init__(self):
        self.Menu_Card=['Dosa','Idly','Biryani']
       
       
    def show(self):
       print(self.Menu_Card)
      
      
    def add(self):                 
        dish=input('Which dish you Want to Add: ')
        self.Menu_Card.append(dish)
        print(self.Menu_Card)
       
       
    def update(self):
        dish1=input('Which dish you Want to update: ')
        dish2=input('Which dish you Want to replace: ')
        for i in range(len(self.Menu_Card)):
         if self.Menu_Card[i] == dish1:
            self.Menu_Card[i] = dish2
        print(self.Menu_Card)
       
       
    def Delete(self):
        dish=input('Which dish you Want to Remove')
        self.Menu_Card.remove(dish)
        print(self.Menu_Card )
      
      
def main():
    card=Menu()
    in_put=int(input('Print 1 for display \n Print 2 for add \n Print 3 for update \n Print 4 for Delete \n '))

   
    if(in_put==1):
       card.show()
   
    elif(in_put==2):
        card.add()
      
    elif(in_put==3):
        card.update()
      
    elif(in_put==4):
        card.Delete()
     
       
    else:
        print('You Selected Invalid input')
   
   
if __name__=='__main__':
    main()