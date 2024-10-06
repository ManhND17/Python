from math import sqrt
def snt(a):
    if a<2: return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0: return False
    return True
   
def tn(a):
    if a<10: return False
    s = str(a)
    if s!=s[::-1]: return False
    return True
     
n,m = map(int,input().split())
a=[]
x = 0
for i in range(n):
    a.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        if tn(a[i][j]): x = max(x,a[i][j])
        
if x==0: print('NOT FOUND')
else:
    print(x)
    for i in range(n):
      for j in range(m):
        if a[i][j]==x:
            print("Vi tri "+"["+str(i)+"]"+"["+str(j)+"]")
            
