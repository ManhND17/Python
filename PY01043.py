def check(n):
    if len(str(n))%2!=0:
        return 0
    s=str(n)
    for i in range(len(s)):
        if int(s[i])%2!=0:
            return 0
    for i in range(int(len(s)/2)+1):
        if(s[i]!=s[len(s)-1-i]):
            return 0
    return 1
for i in range(int(input())):
    n=int(input())
    for j in range(22,n,2):
        if check(j)==1: 
            print(j,end=' ')
    print()