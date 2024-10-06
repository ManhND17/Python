for t in range(int(input())):
    n,d = input().split()
    n = int(n)
    d = int(d)
    a = list(map(int,input().split()))
    for i in range(d,n):
        print(a[i],end=' ')
    for i in range(d):
        print(a[i],end=' ')
    print()