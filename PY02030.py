from math import sqrt
def snt(a):
    if a<2: return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            return False
    return True

n = int(input())
a = list(map(int,input().split()))
b = list(set(a))
c = []
for i in a:
    if i in b:
        c.append(i)
        b.remove(i)

x=0
y=0
ok=True
for i in range(0,len(c)):
    y+=c[i]
for i in range(len(c)):
    x+=c[i]
    y-=c[i]
    if snt(x) and snt(y):
        print(i)
        ok=False
        break
if ok:
    print("NOT FOUND")