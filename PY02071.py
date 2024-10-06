a=[]
def Try(start,sum,n,s):
    if sum==n:
        a.append(f'({s[:-1]})')
    if sum>n: return
    for i in range(start,0,-1):
        Try(i,sum+i,n,s+f'{i} ')
    
for t in range(int(input())):
    n = int(input())
    a.clear()
    Try(n,0,n,'')
    print(len(a))
    print(' '.join(a))