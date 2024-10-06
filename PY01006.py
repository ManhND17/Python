def check(s):
    for i in range(len(s)):
        if s[i]!='4' and s[i]!='7': return False
    return True

for i in range(int(input())):
    s=str(input())
    print("YES") if check(s) else print("NO")