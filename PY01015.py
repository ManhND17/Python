

def check(s):
    for i in range(len(s)-1):
        if(int(s[i])-int(s[i+1])>0): return False
    return True

for i in range(int(input())):
    s=str(input())
    print("YES") if check(s) else print("NO")
