from math import sqrt

def snt(a):
    if a<2: return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0: return False
    return True

def check(n):
    n1 = n[::-1]
    if snt(int(n))==False or snt(int(n1))==False: return False
    tong=0
    for i in range(len(n)):
        tong+=int(n[i])
        if snt(int(n[i]))==False: return False
    return snt(tong)

for t in range(int(input())):
    n = input()
    print('Yes') if check(n) else print('No')