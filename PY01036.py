for i in range(int(input())):
    n=int(input())
    s=.0
    if n%2==0:
        for j in range(2,n+1,2):
            s+=float(1/j)
    else:
        for j in range(1,n+1,2):
            s+=float(1/j)
    print("{:.6f}".format(s))