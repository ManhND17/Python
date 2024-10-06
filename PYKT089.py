n = int(input())
a=[]
b=[]
c=[]
while len(c)<n:
    c.extend(list(map(int,input().split())))
for i in c:
    if i%2==1: a.append(i)
    else: b.append(i)
a.sort()
b.sort()
m = len(a)-1
k = 0
for i in c:
    if i%2==0:
        print(b[k],end=' ')
        k+=1
    else:
        print(a[m],end=' ')
        m-=1