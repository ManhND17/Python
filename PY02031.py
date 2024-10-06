from math import sqrt
def snt(a):
    if a<2: return False
    for i in range(2,int(sqrt(a))+1,1):
        if a%i==0:
            return False
    return True
[n,m]=input().split()
for i in range(int(n)):
    a=list(map(int,input().split()))
    for x in a:
        print(1,end=' ') if snt(int(x)) else print(0,end=' ')
    print()