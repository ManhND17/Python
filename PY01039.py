# Y tuong: dau tien so sanh hai ky tu dau tien 
# Neu bang nhau => NO
# So sanh cac ky tu o vi tri chan voi ky tu dau tien
#  tuong tu voi cac vi tri le
# a&b so sanh cac bit(bit nhi phan) giong nhau giu nguyen khac nhau la 0

def solve(n):
    if n[0] == n[1]:
        return "NO"
    for i in range(2, len(n)):
        if n[i] != n[i & 1]:
            return "NO"
    return "YES"

for i in range(int(input())):
    print(solve(input()))