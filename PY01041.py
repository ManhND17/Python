def find(n):
    for i in range(1,len(n),1):
        if n[i]==n[i-1]:
            return -1
        if n[i]<n[i-1]:
            return i
    return -1
def check(n):
    if len(n)<3:
        return 'NO'
    idex=find(n)
    if idex==-1:
        return 'NO'
    else:
        for i in range(idex+1,len(n)):
            if n[i]>=n[i-1]:
                return 'NO'
        return 'YES'

for i in range(int(input())):
    n=str(input())
    print(check(n))