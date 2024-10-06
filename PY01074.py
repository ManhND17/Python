tong=0
for i in range(int(input())):
    n=int(input())
    if n%2==0:
        while n%2==0:
            tong+=2
            n/=2
    x=3
    while n>1:
        if n%x==0:
            while n%x==0:
                tong+=x
                n/=x
        else: x+=2
    
print(tong)

