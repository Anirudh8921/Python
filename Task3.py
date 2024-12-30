def find(my_list,rt):
 temp=0
 for i in range(len(my_list)):
        if(my_list[i]==rt):
            temp=temp+1
 return temp




def repeating(my_list):
 temp=0
 temp2=0
 for i in range(len(my_list)):
        first = find(my_list,my_list[i])

        if(first>temp):
            temp=first
            temp2=my_list[i]

 return temp,temp2


            
length=input('enter the length of the list')
my_list1=[]

for i in range(int(length)):
     my_list1.append(input('enter the data'))

result = repeating(my_list1)
print(f"Most repeating count: {result[0]}")
print(f"repetition Element: {result[1]}")