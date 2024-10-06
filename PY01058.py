from math import sqrt
def snt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0: return False
    return True

for i in range(int(input())):
    n=str(input())
    s=n[(len(n)-3):len(n)]
    s1=n[0:3]
    print("YES") if snt(int(s))and snt(int(s1)) else print("NO")