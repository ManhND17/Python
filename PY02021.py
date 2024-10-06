for t in range(int(input())):
    n,m,k=map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d,e=[],[]
    i=0
    j=0
    while i<n and j<m:
        if a[i]==b[j]:
            d.append(a[i])
            i+=1
            j+=1
        elif a[i]>b[j]:
            j+=1
        else: i+=1
    i=j=0
    while i <len(d) and j<k:
        if d[i]==c[j]:
            e.append(d[i])
            i+=1
            j+=1
        elif d[i]>c[j]:
            j+=1
        else: i+=1
    if len(e)==0:
        print("NO")
    else:
        for i in e:
            print(i,end=' ')
        print()