for t in range(int(input())):
    n,m= input().split()
    n = int(n)
    m = int(m)
    a = list(map(int,input().split()))
    maxi =0
    for i in range(n):
        maxi = i if a[i]>a[maxi] else maxi
    a.insert(maxi,m)
    for i in a:
        if i<0: print(i,end=' ')
    for i in a:
        if i>=0: print(i,end=' ')
    print()