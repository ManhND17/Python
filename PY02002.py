a=[0,1,1]
for i in range(3,93):
    a.append(a[i-1]+a[i-2])

for t in range(int(input())):
    n,m=list(map(int,input().split()))
    for i in range(n,m+1):
        print(a[i],end=' ')
    print()