for i in range(int(input())):
    n,b=input().split()
    n=int(n)
    b=int(b)
    a=[]
    while n>0:
        x=n%b
        if(x<10): a.append(x)
        else: 
            x+=55
            a.append(chr(x))
        n=int(n/b)
    a.reverse()
    for x in a:
        print(x,end='')
    print()