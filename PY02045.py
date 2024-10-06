s = str(input())
while len(s)>1:
    s1=""
    for i in range(int(len(s)/2)):
        s1+=s[i]
    s2=""
    for i in range(int(len(s)/2),len(s)):
        s2+=s[i]
    s= str(int(s1)+int(s2))
    print(s)
    