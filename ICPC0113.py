from math import sqrt

def snt(a):
    if a<2: return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0: return False
    return True

def check(s,n):
    s1 = s[::-1]
    if s1==s: return False
    if int(s1)<int(s): return False
    if snt(int(s1)) and snt(int(s)) and int(s1)<n: return True
    return False

for t in range(int(input())):
    n = int(input())
    for i in range(13,n,2):
        if check(str(i),n): print(i,str(i)[::-1],end=' ')
    print()