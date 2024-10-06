n,a = int(input()), list(map(int,input().split()))
m = max(a)
cnt=0
i=0
while i<n:
    if a[i]==m:
        x=0
        while  i<n and a[i]==m :
            i+=1
            x+=1
        cnt=max(cnt,x)
    else: i+=1   
print(cnt)