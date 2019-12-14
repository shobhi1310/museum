import re

l = ['  ','str rum',' ','fcuk','\n ',' yoyo']
a =[]
for i in l:
    if ((re.search("\w",i))):
        a.append(i)
print(a)
