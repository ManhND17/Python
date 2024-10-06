import math

def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

def snt(a):
    if a<=1: return 0
    for i in range(2,int(math.sqrt(a))+1,1):
        if a%i==0: return 0   
    return 1

t=int(input())
for i in range(t):
    n=int(input())
    dem=0
    for j in range(n):
        if gcd(n,j)==1: dem+=1  
    if snt(dem)==1: print("YES")
    else: print("NO")