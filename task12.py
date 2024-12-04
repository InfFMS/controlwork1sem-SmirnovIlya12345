from math import sqrt
cc=0
while cc<5:
    a=[]
    c=0
    for i in range(300000000, 100000000000000000000000):
        B=[]
        for j in range(2, round(sqrt(i))):
            if i%j==0:
                c+=1
                b=i/j
                B.append(j)
        if len(B)>=5:
            print(i/B[4])
        elif len(B)==4:
            print(B[3])
        elif len(B)==3:
            print(B[1])
        if c>2:
            cc+=1
            a.append(i)
        c=0
        if cc>4:
            break
print(a)