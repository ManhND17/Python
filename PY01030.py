from math import gcd, pow
n,k=[int(x) for x in input().split()]
cnt=0
for i in range(int(pow(10,k-1)),int(pow(10,k)),1):
    if gcd(i,n)==1:
        cnt+=1
        print(i,end=' ')
    if cnt==10:
        cnt=0
        print()
         