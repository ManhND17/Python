
for i in range(int(input())):
    n=str(input())
    s=n[::-1]
    ok=True
    for j in range(1,len(s)):
        if abs(ord(s[j])-ord(s[j-1]))!=abs(ord(n[j])-ord(n[j-1])):
            ok=False
            break
    print('YES') if ok else print('NO')