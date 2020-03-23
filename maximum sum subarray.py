a=[int(e) for e in input().split()]
s=0
ans=a[1]
for i in range(len(a)):
    s+=a[i]
    if s>ans:
        ans=s
    if s<0:
        s=0
    print(s)
print(ans)