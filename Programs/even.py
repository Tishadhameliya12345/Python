# find even number without using if statment

for i in range(1,5,2):
        print(i)
        
#Write a python program to check whether it contains same number in adjacent position.
#Display the count 

#list_num=[1,1,3,2,2,4]
list_num=list(map(int,input().split(",")))
count=0

for i in range(len(list_num)-1):
    if list_num[i]==list_num[i+1]:
        count+=1
        
print(count)