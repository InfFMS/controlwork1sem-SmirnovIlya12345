from math import sqrt
a=[]
for i in range(174457, 174506):
    c=0
    for j in range(2, round(sqrt(i))):
        if i%j==0:
            c+=1
    if c==1:
        a.append(i)
print(a)