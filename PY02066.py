n = int(input())
a = []
while len(a)<n:
    arr = list(map(int,input().split()))
    a.extend(arr)
ok=0
a.sort()
for i in range(1,a[len(a)-1]):
    if i not in a:
        print(i)
        ok=1
      
if ok==0:
    print('Excellent!')