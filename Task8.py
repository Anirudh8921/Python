def Add(num1,num2):
    return f'Addition: {num1+num2}'
def Sub(num1,num2):
    return f'Subtraction: {num1-num2}'
def Mul(num1,num2):
    return f'Multiplication: {num1*num2}'
def Div(num1,num2):
    return f'Division: {num1/num2}'


def main():
    print('1.+','2.-','3./','4.*',sep='\n')
    value=int(input('Enter the choice: '))
    value1=int(input('Enter the value1: '))
    value2=int(input('Enter the value2: '))
    Result={1:Add,2:Sub,3:Div,4:Mul}
    if value==1:
        print(Result[1](value1,value2))
    elif value==2:
        print(Result[2](value1,value2))
    elif value==3:
        print(Result[3](value1,value2))
    elif value==4:
        print(Result[4](value1,value2))

if __name__=='__main__':
    main()