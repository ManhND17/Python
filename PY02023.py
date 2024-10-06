def Tong(s):
    x=1
    for i in range(len(s)):
        x*=int(s[i])
    return x

for t in range(int(input())):
    n = int(input())
    a = [str(x) for x in input().split()]
    a = sorted(a,key=lambda x: (Tong(x),int(x)))
    [print(x,end=' ') for x in a]
    print()