n=str(input())
chuaxet=[0]*15


def Try(s):
    if len(s) == len(n):
        print(s)
        return
    
    for j in range(len(n)):
        if chuaxet[j]==0:
            chuaxet[j]=1
            Try(s+n[j])
            chuaxet[j]=0
Try('')