stack =[]
def empty():
    return len(stack)==0

def pop():
    if empty()==False:
        stack.pop()
def push(a):
    stack.append(a)

for  t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n):
        while empty()==False and a[i]>=a[stack[-1]]:
            pop()
        
        if empty()==True:
            print(i+1,end=' ')
        else:
            print(i-stack[-1],end=' ')
        push(i)
    print()
    stack.clear()