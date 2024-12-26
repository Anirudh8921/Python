Menu_card = ['Dosa','Idly','Biryani']
def Display():
    print('Display_item:',Menu_card)
def Add():
    Menu_card.append('Butter Chicken')
    print('Add_item:',Menu_card)    
def Update():
    Menu_card[1]=('Vada')
    print('Update:',Menu_card)
def Delete():
    Menu_card.remove('Dosa')
    print('Delete:',Menu_card)









def main(enter):
    if enter==1:
        Display()
    elif enter==2:
        Add()
    elif enter==3:
        Update()    
    elif enter==4:
        Delete()




if __name__=="__main__":
    enter=int(input())
    main(enter)