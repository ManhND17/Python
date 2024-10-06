n = int(input())
a=[]
s=0
for i in range(n):
    b = list(map(int,input().split()))
    s+=sum(b)
    a.append(b)
    
    
if n==2:
    print(1,s//2-1)
else:
    x1 = (sum(a[0]) - s//((n-1)*2))//(n-2)
    # Tong hang thu nhat co (n-1)*a[0]+(a[1]+..+a[n-1])
    # Do hang i va cot i thi a[i] dc tinh n-1 lan => s=(n-1)*(a[0]+...+a[n-1])
    print(x1,end=' ')
    for i in range(1,n):
        print(a[0][i]-x1,end=' ')
        
        