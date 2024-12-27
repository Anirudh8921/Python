def add(value1,value2):
    return value1+value2
def sub(value1,value2):
    return value1-value2
def Multi(value1,value2):
    return value1*value2
def Div(value1,value2):
    return value1/value2
def exp(value1,value2):
    return value1**value2

def main():
    value1=int(input('Enter value1: '))
    value2=int(input('Enter value2: '))
    print('1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exp\nEnter your choice:',end='')
    user_input=int(input())
    if user_input==1:
       print('Add:',add(value1,value2))
    elif user_input==2:
       print('Sub:',sub(value1,value2))
    elif user_input==3:
       print('Multiplication:',Multi(value1,value2))
    elif user_input==4:
        if value2:
           print('Division:',Div(value1,value2))
        else:
           print("Enter non zero")
    elif user_input==5:
        print('Exponential:',exp(value1,value2))
    else:
        print('Invalid option....')
main()