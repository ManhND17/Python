s=str(input())
cnt=0
for i in range(len(s)):
    if s[i]=='4': cnt+=1
    if s[i]=='7': cnt+=1
print("YES") if cnt==4 or cnt==7 else print("NO")


