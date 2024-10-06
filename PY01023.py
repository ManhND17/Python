for i in range(int(input())):
    n=int(input())
    x=2
    print('1',end='')
    dem=0
    while n>1:
        if n%x==0:
            dem=0
            while n%x==0:
                dem+=1
                n/=x
            print(' * ',x,'^',dem,sep='',end='')
        else: x+=1
    print()