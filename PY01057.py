from math import sqrt

def snt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0: return False
    return True

def check(n):
    for i in range(len(n)):
        if snt(i) and snt(int(n[i]))==False: return False
        if snt(i)==False and snt(int(n[i])): return False
    return True

for i in range(int(input())):
    n=str(input())
    print("YES") if check(n) else print("NO")