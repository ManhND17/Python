import re
s=''
while True:
   try: s+=input()
   except: break
ss = re.split('[.?!]',s)
for i in ss:
    if len(i)==0: continue
    i = i.lower().split()
    i[0] =i[0][0].upper()+i[0][1:]
    print(' '.join(i)) 

 