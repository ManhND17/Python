def Union(s):
    tong=0
    for i in range(len(s)):
        tong+=ord(s[i])-ord('0')
    if tong%10!=0: return 'NO'
    for i in range(0,len(s)-1,1):
        if(abs(ord(s[i])-ord(s[i+1]))!=2): return 'NO'
    return "YES"
    

for i in range(int(input())):
    s=str(input())
    print(Union(s))