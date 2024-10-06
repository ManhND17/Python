from math import sqrt

def snt(s):
    if s<2: return False
    for i in range(2,int(sqrt(s))+1,1):
        if s%i==0: return False
    return True

for i in range(int(input())):
    n=str(input())
    tong=0
    for j in range(len(n)):
        tong+=int(n[j])
    print("YES") if tong%3==0 else print("NO")