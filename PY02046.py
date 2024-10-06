from math import sqrt
def snt(a):
    if a<2:
        return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0: return False
    return True

n = int(input())
a = list(map(int,input().split()))
b = {}
for i in a:
    if i not in b:
        b[i]=1
        
a.clear()
for i in b:
    a.append(i)
tong =0   
for i in range(len(a)):
    tong+=a[i]
    
c=0
check =True
for i in range(len(a)):
        c+=a[i]
        tong-=a[i]
        if snt(c) and snt(tong):
            print(i)
            check= False
            break
        
if check: print("NOT FOUND")