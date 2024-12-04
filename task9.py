c=0
for a in range(1, 2097152):
    for b in range(2097152//a+1):
        A=max(a,b)
        B=min(a,b)
        C=(A-B)*(A+B+1)/2
        D=B*(B+1)-1
        if C+D==2097152:
            c+=1
print(c)

