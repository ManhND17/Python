n,m = map(int,input().split())
a = list(map(int,input().split()))
b={}
for i in a:
    if i not in b:
        b[i]=1
    else: b[i]+=1

a = sorted(b,key=lambda x: (-b.get(x),x))
Max = b[a[0]]
while len(a)>0 and b[a[0]]==Max: a.pop(0)
if len(a)==0: print('NONE')
else:
    print(a[0])