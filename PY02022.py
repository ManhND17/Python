from math import sqrt
def snt(a):
    if a<2: return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            return False
    return True


n = int(input())
a = [int(x) for x in input().split()]
b={}
for x in a:
    if x not in b:
        b[x]=1
    else:
        b[x]+=1
for x in b:
    if snt(x):
        print(x,b[x])