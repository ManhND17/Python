check=[0,0]
for i in range(2,8001):
    check.append(1)
for i in range(2,8001):
    for j in range(2*i,8001,i):
        check[j]=0

a=[]
for i in range(2,8000):
    if check[i]==1:
        a.append(i)

n,m=list(map(int,input().split()))
print(m,end=' ')
for i in range(n):
    m+=a[i]
    print(m,end=' ')