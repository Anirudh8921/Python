list_1=eval(input('enter a number:'))
max=list_1[0]
min=list_1[0]
tot=0
for i in list_1:
    if i>max:
        max=i
    if i<min:
        min=i
    tot=tot+i
    
print(max)
print(min)
print(tot)
