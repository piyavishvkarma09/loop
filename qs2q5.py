# User se ek n naam ke variable mein ek integer input lo. Fir user se utni baar input baar ek integer ko input lo jitni n ki value hai. Finally unn saare integer jinko user ne input kara hai, sum karke print karo.

# Example: Jaise agar n mein user ne ki 6 daala hai toh 6 baar input lo.

# Kitni baar input lein? ' 6
# Ek number daalo> 10
# Ek number daalo> 1
# Ek number daalo> 56
# Ek number daalo> 89
# Ek number daalo> 11
# Ek number daalo> 12
# Sum: 179

# n ki value Kitni baar input lein? waali line mein input li gai hai.

# Sum 179 isliye likha hai kyunki 10+1+56+89+11+12 ka result 179 hai.

n=int(input("enter the number"))
i=1
sum=0
while i<=n:
    num=int(input("enter the number")) 
    sum=sum+num
    i=i+1
print(sum)
