# #the cube's sum of each number is equal to the number

# 153
num=int(input("enter 3 digits number"))
temp=num
digit=0
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

