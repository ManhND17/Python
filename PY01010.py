for i in range(int(input())):
    s=str(input())
    x=int(s[0])*10+int(s[1])
    y=int(s[len(s)-2])*10+int(s[len(s)-1])
    print("YES") if x==y else print("NO")