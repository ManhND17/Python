from math import gcd,sqrt

def tong(c):
    ton=0
    s=str(c)
    for i in range(len(s)):
        ton+=int(s[i])
    return ton

def snt(a):
    if(a<2): return False
    for i in range(2,int(sqrt(a))+1,1):
        if a%i==0: return False
    return True

for i in range(int(input())):
    a,b=[int(x) for x in input().split()]
    c=int(gcd(a,b))
    print("YES") if snt(tong(c)) else print("NO")