from math import gcd
for i in range(int(input())):
    n=str(input())
    n1=n[::-1]
    print("YES") if gcd(int(n),int(n1))==1 else print("NO")
