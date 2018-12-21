x=int(input("enter x :"))    #عدد مورد نظر در مبناي اوليه
n=int(input("enter n (n must be bigger than each digits of x): "))    #مبناي اوليه
m=int(input("enter m:"))    #مبناي ثانويه
s=x    #متغير کمکي براي ثابت ماندن مقدار ايکس
p=x    #متغير کمکي براي ثابت ماندن مقدار ايکس

count=0    #تعداد ارقام ايکس
while(s != 0):
    s=s//10
    count +=1

z=0    #ايکس در مبناي ده
for i in range (0,count,1):
    r=p%10
    z += r*(n**i)
    p=p//10
print("x in base 10 = ",z)

y=z   #متغير کمکي براي ثابت ماندن مقدار زد
q=0   #عدد مورد نظر در مبناي ثانويه به صورت معکوس
t=y%m
if(t==0):
    t=1
q=(q*10)+t
y=y//m
while(y>=m):
    t=y%m
    q=(q*10)+t
    y=y//m
q=(q*10)+y

l=0    #عدد مورد نظر در مبناي ثانويه
while(q !=0 ):
    d=q%10
    l=(l*10)+d
    q=q//10
if(z%m == 0):
    l=l-1

print("x in base m = ",l)
    
