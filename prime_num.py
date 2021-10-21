# num=1
# while num<=20:
#     if num==2 or num==3 or num==5 or num==7:
#         print(num,"is prime nuber")
#     elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
#         print(num,"is not a prime nuber")
#     else:
#         print(num,"prime nuber")
#     num+=1

num=int(input("enter the number"))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print("prime number")
else:
    print("not a prime number")