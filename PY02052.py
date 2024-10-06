n = int(input())
x = 0
y = 0
a =[]
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
   
k = int(input()) 
for i in range(n):
    for j in range(n):
        if i< j: x+=a[i][j]
        if j<i: y+=a[i][j]

if abs(x-y)<k: print('YES')
else: print('NO')
print(abs(x-y))