a = {}
ok=0
x =""
for t in range(int(input())):
    s = str(input())
    if ok==0:
        x=s
        a[s]=0
        ok=1
    if s =="": ok=0
    else: a[x]+=1
[print(f"{key}: {value-1}") for key,value in a.items()]