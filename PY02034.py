s = str(input())
x=""
a =[]
for i in range(len(s)):
    if len(x)<2:
        x = x +s[i]
    if len(x)==2:
        a.append(int(x))
        x=""
if len(x)==2:
    a.append(int(x))
b = {}
for i in a:
    if i not in b:
        b[i]=1
    else: b[i]+=1

for i in b:
    print(i,b[i],sep=' ')
    