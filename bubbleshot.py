a=[78,8,76,35,87,42,36]
for i in range(len(a)):
    for j in range(len(a)-i):
        if a[j]>[i+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)        