list1=[]
list2=[]
list3=[]

x=int(input("enter x:"))
y=int(input("enter y:"))

count=0
counter=0

for i in range (1,x+1,1):
    if(x%i==0):
        list1 += [i]
        count +=1

for i in range (1,y+1,1):
    if(y%i==0):
        list2 += [i]
        counter +=1

for i in range (0,count,1):
    for j in range (0,counter,1):
        
        if (list1[i]==list2[j]):
            temp=list1[i]
            list3 += [temp]

print("divisors of x : ",list1)
print("divisors of y : ",list2)
print("common divisors of x and y : ",list3)
