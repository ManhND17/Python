for i in range(int(input())):
    n=str(input())
    cnt=0
    if int(n)%7==0:
        print(n)
    else:
        while 1:
            cnt+=1
            n1=n[::-1]
            s=int(n1)+int(n)
            if s%7==0:
                print(s)
                break
            else: n=str(s)
            if cnt==1000:
                print(-1)
                break