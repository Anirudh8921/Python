def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num2/num2)
def mod(num1,num2):
    print(num1//num2)
def exp(num1,num2):
    print(num1**num2)


def main(value):
    if value=='+':
       num1=30
       num2=20
       add(num1,num2)
    elif value=='-':
       num1=30
       num2=20
       sub(num1,num2)
    elif value=='*':
       num1=5
       num2=10
       mul(num1,num2)
    elif value=='/':
       num1=25
       num2=5
       div(num1,num2)
    elif value=='//':
       num1=30
       num2=4
       mod(num1,num2)
    elif value=='**':
       num1=2
       num2=3
    exp(num1,num2)

if __name__=="__main__":
    value=input("enter a symbol")
    main(value)