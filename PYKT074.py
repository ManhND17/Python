n = int(input())
for t in range(n):
    s = input().split()
    ans = s[0]
    for i in s[1:]:
        if (len(ans)+len(i)+1>100): break
        ans += ' '+i
    print(ans)