while 1:
    a,b,c,d = list(map(int,input().split()))
    if a==b and a==c and a==d and a==0: break
    else:
        dem=0
        while a!=b or a!=c or a!=d:
            x=a
            a = abs(a-b)
            b = abs(b-c)
            c = abs(d-c)
            d = abs(x-d)
            dem+=1
        print(dem)