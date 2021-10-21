i=0
sum=0
average=0
while i<=11:
    weight=int(input("enter the weight"))
    sum=sum+weight
    average=sum/11
    i=i+1
if weight%5==0:
    print(average,"is divisible")
else:
    print(average,"is not diviible")
