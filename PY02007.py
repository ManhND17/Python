b=[]
while len(b)<10:
    b+=list(map(int,input().split()))
for i in range(10):
    b[i]%=42
print(len(set(b)))