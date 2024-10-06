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
b = list(set(a))
for i in a:
    if i in b:
        print(i,end=' ')
        b.remove(i)
    