for t in range(int(input())):
    n,m= map(int,input().split())
    a =[]
    for i in range(n):
        a.append(list(map(int,input().split())))

    b=[]
    for i in range(3):
        b.append(list(map(int,input().split())))
    tong = 0
    for i in range(n):
        if i==n-2: break
        for j in range(m):
            if j== m-2: break
            for k in range(3):
                for h in range(3):
                    tong+= b[k][h]*a[i+k][j+h]
    print(tong)


