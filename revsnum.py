# revers number
# num = int(input("enter numbers"))
# rev = 0
# while num > 0:
#   rem = num % 10  # Finding the remainder
#   rev = (rev*10) + rem
#   num = num//10  # Finding the quotient
# print(rev)


user=int(input("enter the number"))
revers=0
while user>0:
    rem=user%10#reminder
    revers=(revers*10)+rem
    user=user//10
print(revers)