n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    k = 0
    m = 0
    for j in range(n):
        if a[i]<a[j]:
            k+=1
        elif a[i]>a[j]:
            m+=1
    if (k==n//2) and (m==n//2):
        print(a[i])

