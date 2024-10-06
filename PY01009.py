s=str(input())
dem=0
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z': dem+=1
print(s.lower()) if dem*2>=len(s) else print(s.upper())