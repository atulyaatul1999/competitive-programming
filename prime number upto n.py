n=int(input("enter a number"))
a=[0]*n
for i in range(2,n):
    a[i]=1
for i in range(2,n//2):
    for j in range(i+1,n):
        if j%i==0:
           a[j]=0
b=[]
for i in range(n):
    if a[i] != 0:
        b.append(i)
print(b)