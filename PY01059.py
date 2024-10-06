def Tinh(n):
    tong =0
    tich =1
    ok=True
    for i in range(len(n)):
        if i%2==1: tong+=int(n[i])
        else:
            if n[i]!='0':
                tich*=int(n[i])   
    return (tong,tich)

for i in range(int(input())):
    n=str(input())
    (x,y)=Tinh(n)
    print(y,x,sep=" ")