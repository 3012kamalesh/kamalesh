num=int(input("enter the number"))
x=num

while x>0:
    sum=0
    rem=x%10
    sum=sum+(rem**2)
    x=x//10
x=sum
if x==1:
    print(x,"is the happy nnumber")
else:
    print(x,'is the sad number')



