year=int(input("enter the year"))
i=0
while i<1:
    if year%4==0 or year%100==0 or year%400==0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
    i+=1