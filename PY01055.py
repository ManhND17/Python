def Check(n):
    if len(n)%2==0: return False
    if n[0]==n[1]: return False
    for i in range(2,len(n),2):
        if n[i]!=n[i-2]: return False
    return True

for i in range(int(input())):
    n=str(input())
    print("YES") if Check(n) else print("NO")