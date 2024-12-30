list=eval(input('enter a number:'))
# print(list[0])
if (list[0]<list[1])and(list[0]<list[2]):
    print('minimum',list[0])
elif (list[1]<list[2]):
    print('minimum',list[1])
else:
    print('minimum',list[2])
if (list[0]>list[1])and(list[0]>list[2]):
    print('maximum',list[0])
elif (list[1]>list[2]):
    print('maximum',list[1])
else:
    print('maximum',list[2])
total=0
for i in list:
    total=total+i
print('total',total)


# list_1=eval(input('enter a number:'))
# max=list_1[0]
# min=list_1[0]
# tot=0
# for i in list_1:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
#     tot=tot+i
    
# print(max)
# print(min)
# print(tot)