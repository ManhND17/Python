def round(i): return 1 if i>=5 else 0
t=input()
for i in range(int(t)):
    arr=[int(x) for x in input()]
    for i in range(arr.__len__()-1,0,-1):
        arr[i-1]+=round(arr[i])
        arr[i]=0
    print(''.join(map(str,arr)))