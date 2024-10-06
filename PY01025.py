n=str(input())
dem=0
s=''
for i in range(len(n)-1,-1,-1):
    dem+=1
    s=n[i]+s
    if dem==3:
        s=','+s
        dem=0
if s[0]==',':
    for i in range(1,len(s),1):
        print(s[i],end='')
else : 
    print(s)