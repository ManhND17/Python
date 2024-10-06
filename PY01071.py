s=str(input())
s1=s[len(s)-3:len(s)]
s1 = s1.lower()
print("yes") if s1=='.py' else print("no")