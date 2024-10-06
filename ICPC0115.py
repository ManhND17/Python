f=[1]
a=1
for i in range(1,10):
    a*=i
    f.append(a)

def check(n):
    a=0
    for i in range(len(n)):
        a+=f[int(n[i])]
    if a!=int(n): return False
    return True

for t in range(int(input())):
    n = input()
    print('Yes') if check(n) else print('No')