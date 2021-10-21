user=int(input("enter the number"))
revers=0
i=1
while i >0:
    revers=(revers*10)+i%10
    i=i//10
    print(revers)
    
