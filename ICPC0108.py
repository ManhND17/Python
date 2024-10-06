for k in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    s=0
    for i in range(n-2):
        l=i+1
        r=len(a)-1
        x=a[i]
        while l<r:
            if x+a[r]+a[l]==0:
                s+=1
                l+=1
            elif x+a[r]+a[l]>0:
                r-=1
            else:
                l+=1
    print(s)