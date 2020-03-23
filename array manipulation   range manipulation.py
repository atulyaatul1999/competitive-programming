def arrayManipulation(n, q):
    x=[0]*(n+1)
    y=[0]*(n+1)
    for i in range(len(q)):
        a,b,c=q[i][0],q[i][1],q[i][2]
        x[a-1]+=c
        x[b]-=c
        y[0]=x[0]
    for i in range(1,n):
        y[i]=y[i-1]+x[i]
    return(max(y))
n,m=(int(e) for e in input().split())
a=[]
for j in range(m):
    b=[int(e) for e in input().split()]
    a.append(b)
print(arrayManipulation(10,a))
