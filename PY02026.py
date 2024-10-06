n,m = map(int,input().split())
a = sorted(set(list(map(int,input().split()))))
b = sorted(set(list(map(int,input().split()))))
if len(a)!=len(b):
    print("NO")

else:
    ok=True
    for i in range(len(a)):
        if a[i]!=b[i]:
            print("NO")
            ok=False
            break
    if ok:
        print('YES')