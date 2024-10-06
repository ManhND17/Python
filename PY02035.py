s = str(input())
k = int(input())
x=0
s1=""
a={}
for i in s:
    x+=1
    s1+=i
    if x%2==0:
        if s1 not in a:
            a[s1]=1
        else: a[s1]+=1
        s1=""
#a = sorted(a.items(),key=lambda x: x[0])
ok=0
for i in sorted(a):
    if a[i]>=k:
       print(i,a[i],sep=' ')
       ok=1
if ok==0: print("NOT FOUND")