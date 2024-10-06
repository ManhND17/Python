for i in range(int(input())):
    n=int(input())
    s=str(input())
    x=0
    s=s[::-1]
    for i in range(len(s)):
        if(s[i]=='1'): x+=pow(2,i)
    y=''
    while x>0:
        k=x%n
        if(k>=10): y=chr(ord('A')+k-10)+y
        else: y=str(k)+y
        x=int(x/n) 
    print(y)