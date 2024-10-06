def check(s):
    for i in range(len(s)):
        if s[i]!='0' and s[i]!='1'and s[i]!='2':
            return "NO"
    return 'YES'

for i in range(int(input())):
    s=str(input())
    print(check(s))