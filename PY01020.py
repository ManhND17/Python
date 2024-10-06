for i in range(int(input())):
    s=str(input())
    x=int(s[len(s)-2])*10+int(s[len(s)-1])
    print('YES') if x==86 else print('NO')