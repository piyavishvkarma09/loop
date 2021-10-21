#chr key word use for character
#character starts from 65 to 91 for  capital and 97 to 121 for small letters

#
num=int(input("enter the number of row"))
k=65
i=1
while i<num:
    j=1
    while j<i+1:
        a=chr(k)
        print("",a,end="")
        j=j+1
        k=k+1
    print()
    i=i+1