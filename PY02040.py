n = int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

s1=0
s2=0
for i in range(n):
    for j in range(n):
        if i+j<n-1: s1+=a[i][j]
        if i+j>n-1: s2+=a[i][j]
k = int(input())
print("YES") if abs(s1-s2)<=k else print("NO")
print(abs(s1-s2))