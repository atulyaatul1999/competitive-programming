n=int(input())
n=n+1
a=[1]*n
print(a)
a[0]=0
a[1]=0
for i in range(2,int(n**.5)+1):
    for j in range(i+1,n):
        if j%i==0:
            a[j]=0
print(a)
for i in range(n):
    if a[i]==1:
        print(i)

