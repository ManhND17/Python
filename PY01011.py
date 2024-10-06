def check(n):
    s=str(n)
    if len(s)%2==1: return False
    for i in range(len(s)):
        if s[i]=='1' or s[i]=='3' or s[i]=='5': return False
        if s[i]=='7' or s[i]=='9': return False
    for i in range(int(len(s)/2)):
        if s[i]!=s[len(s)-1-i]: return False
    return True

for i in range(int(input())):
    n=int(input())
    for j in range(n):
        if check(j): print(j,end=' ')
    print()