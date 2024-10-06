from math import sqrt

def snt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0: return False
    return True

def check(n):
    tong=0
    for i in range(len(n)):
        tong+=int(n[i])
        if i%2==0 and int(n[i])%2!=0: return False
        if i%2==1 and int(n[i])%2==0: return False
    if snt(tong)==False: return False
    return True

for i in range(int(input())):
    n=str(input())
    print("YES") if check(n) else print("NO")