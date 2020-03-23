def psa(a,c,d):
    b = [0] * len(a)
    b[0] = a[0]
    for i in range(1, len(a)):
        b[i] = b[i - 1] + a[i]
    return b[d]-b[c]
a=[int(e) for e in input().split()]
print(psa(a,2,5))

