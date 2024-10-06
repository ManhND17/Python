from math import sqrt

def snt(s):
    if s<2: return False
    for i in range(2,int(sqrt(s))+1):
        if s%i==0: return False
    return True

for i in range(int(input())):
    s=str(input())
    x=0
    y=0
    for j in range(len(s)):
        if snt(int(s[j])): x+=1
        else: y+=1
    print("YES") if x>y and snt(len(s)) else print("NO")

