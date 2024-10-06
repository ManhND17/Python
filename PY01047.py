from math import sqrt

def snt(s):
    if s<2: return 0
    for i in range(2,int(sqrt(s))+1,1):
        if s%i==0: return 0
    return 1


for i in range(int(input())):
    n=str(input())
    s=n[len(n)-4:len(n)]
    s = int(s)
    print("YES") if snt(s) else print("NO")