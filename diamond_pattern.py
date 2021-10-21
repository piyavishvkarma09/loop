n=7
d=n//2+1
x=0
while x<7:
    for y in range(1,n+1):
        if (y>=d)!=0 and y<=n-d+1:
            print("* ",end="")
        else:
            print(" ",end="")#2ws
    if x<=n//2:
        d-=1
    else:
        d+=1
        print()
    x+=2-1