n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))

l=[]

for i in arr:
    if i not in l:
        l.append(i)

l.sort()
n = len(l)
a=[]

def Try(i):
    if len(a)==k:
        for j in a:
            print(j,end=' ')
        print()
        return
    if i ==n: return

    for j in range(i,len(l)):
        a.append(l[j])
        Try(j+1)
        a.pop()

Try(0)
