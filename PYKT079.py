for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    x = set(a)
    mi = 10**3
    ma = 0
    for i in a:
        if i> ma: ma=i
        if i<mi: mi =i
    print(ma-mi+1-len(x))