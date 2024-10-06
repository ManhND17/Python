for i in range(int(input())):
    s=str(input())
    dem=1
    for j in range(len(s)-1):
        if(s[j]==s[j+1]): dem+=1
        else:
            print(dem,s[j],sep='',end='')
            dem=1
    if dem>0: print(dem,s[len(s)-1],sep='',end='')
    print()