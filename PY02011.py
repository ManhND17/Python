n = int(input())
a=[]
while len(a)<n:
    a.extend( list(map(int,input().split())))
b=[]
k = 10**18
tong = 0
for i in range(n):
    for j in range(n):
        if a[i]>a[j]: tong+=a[i]-a[j]
        else: tong +=a[j]-a[i]
    b.append(tong)
    k = min(tong,k)
    tong=0

for i in range(n):
    if b[i]==k:
        print(b[i],a[i],sep=' ')
        break