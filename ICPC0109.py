e=10**8
for t in range(int(input())):
    n=int(input())
    l=input()
    x, y, z = [e, e, e]
    for i in map(int, l.split()): 
        if i<=x:
            z = y
            y = x
            x = i
        elif i<=y:
            z = y 
            y = i
        elif i<z: z = i
    print(x+y+z)