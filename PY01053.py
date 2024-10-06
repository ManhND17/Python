
for i in range(int(input())):
    n=str(input())
    tong=1
    for j in range(len(n)):

        if n[j]!='0': tong*=int(n[j])
    print(tong) 