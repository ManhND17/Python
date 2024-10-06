for i in range(int(input())):
    s=str(input())
    for j in range(0,len(s),2):
        for k in range(0,int(s[j+1]),1):
            print(s[j],end='')
    print()