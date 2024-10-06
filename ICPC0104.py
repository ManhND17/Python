for i in range(int(input())):
    n=str(input())
    x=0
    y=0
    for j in range(len(n)):
        if(n[j].isdigit()): y=y*10+int(n[j])
        else:
            x=max(x,y)
            y=0
    x=max(x,y)
    print(x)