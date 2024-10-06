n = int(input())
a = []
for i in range(n):
    a.append(list(input()))

dem=0
for i in range(n):
    for j in range(n):
       if a[i][j]=='C':
          for k in range(n):
              if a[i][k]=='C' and k!=j: dem+=1
              if a[k][j]=='C' and k!=i: dem+=1

print(int(dem/2))

            
