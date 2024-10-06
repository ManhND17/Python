from math import sqrt
def snt(s):
    if s<2: return 0
    for i in range(2,int(sqrt(s))+1,1):
        if s%i==0: return 0
    return 1

for i in range(int(input())):
    x1=0 
    x2=0
    s=str(input())
    if snt(len(s))==0: print("NO")
    else:
        for j in range(len(s)):
            if s[j]=='2' or s[j]=='3' or s[j]=='7' or s[j]=='5': x1+=1
            else: x2+=1
        if x1>x2: print('YES')
        else: print('NO')


