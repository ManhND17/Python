def cv(a,b,p,q):
    a=a.replace(p,q)
    b=b.replace(p,q)
    return int(a)+int(b)

for i in range(int(input())):
    [p,q]=input().split()
    s=input().split()
    if len(s)>1:
        a,b=s[0],s[1]
    else:
        a=s[0]
        b=input()
    x = cv(a, b, p, q)
    y = cv(a, b, q, p)
    print(min(x, y), max(x, y)) 

