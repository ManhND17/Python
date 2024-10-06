from math import sqrt
def snt(a):
    if a<2: return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0: return False
    return True

for t in range(int(input())):
    n = int(input())
    dem=0
    for i in range(3,n-6,2):
        if (snt(i) and (snt(i+2) or snt(i+4)) and snt(i+6)): 
            dem+=1
            
    print(dem)