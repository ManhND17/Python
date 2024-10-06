tong =0
a ={}
for i in range(int(input())):
    s = list(map(str,input().split()))
    if s[3]=='IN':
        if s[1]=='Xe_con':
            if s[2]=='5':
                if s[4] not in a:
                    a[s[4]] =10000
                else: a[s[4]]+=10000
            else:
                if s[4] not in a:
                    a[s[4]] =15000
                else: a[s[4]]+=15000
        elif s[1]=='Xe_tai':
            if s[4] not in a:
                a[s[4]] =20000
            else: a[s[4]]+=20000
        else:
            if s[2]=='29':
                if s[4] not in a:
                    a[s[4]] =50000
                else: a[s[4]]+=50000
            else:
                if s[4] not in a:
                    a[s[4]] =70000
                else: a[s[4]]+=70000
[print(f"{key}: {value}") for key, value in a.items()]