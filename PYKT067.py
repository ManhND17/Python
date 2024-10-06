a =[]
b =[True]*11
c =[1]*11

def Try(n,i):
    if i>n: return
    for j in range(1,n+1):
        if b[j]:
            b[j]=False
            c[i]=j
            if i==n:
                s=''
                for k in range(1,n+1):
                   s+=str(c[k])
                a.append(s) 
            else: Try(n,i+1)
            b[j]=True  
               
for t in range(int(input())):
    n = int(input())
    a.clear()
    b=[True]*11
    Try(n,1)
    print(len(a))
    print(' '.join(a[::-1]))