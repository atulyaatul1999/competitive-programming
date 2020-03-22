n=int(input())
f=[]
e=[]
if n==1:
    f.append(1)
    e.append(1)
else:
    x=int(n**.5)
    print(x)
    d=2
    while d<=x and n>1:
        s=0
        while n%d==0:
            s+=1
            n/=d
        if s>0:
            f.append(d)
            e.append(s)
        d += 1
    if n>1:
        f.append(n)
        e.append(1)
for i in range(len(f)):
    print(f[i],end="-")
    print(e[i])