for t in range(int(input())):
    n = int(input())
    a={}
    s=list(map(int,input().split()))
    for x in s:
        if x not in a:
            a[x]=1
        else: a[x]+=1
    ok=0
    for x in a:
        if a[x]>int(n/2):
            print(x)
            ok=1
    if ok==0: print("NO")