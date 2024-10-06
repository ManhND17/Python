n,m = map(int,input().split())
a=[]
x = 0
y =10000
for i in range(n):
    arr = list(map(int,input().split()))
    x = max(x,max(arr))
    y = min(y,min(arr))
    a.append(arr)
      
k = x-y
ok=1
for i in range(n):
    for j in range(m):
        if a[i][j]==k:
            ok =0
            break
        
if ok == 1: print('NOT FOUND')
else:
    print(k)
    for i in range(n):
     for j in range(m):
        if a[i][j]==k:
            print("Vi tri "+"["+str(i)+"]"+"["+str(j)+"]")
            
