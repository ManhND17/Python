for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ok=0
    for i in range(n):
        if a[i]>b[i]:
            ok=1
            break
    print("YES") if ok==0 else print('NO')