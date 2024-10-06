from math import sqrt
def snt(a):
    if a<2:
        return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0: return False
    return True

n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
    if snt(i):
        b.append(i)
b = sorted(b)

j=0
for i in a:
    if snt(i):
        print(b[j],end=' ')
        j+=1
    else:
        print(i,end=' ')