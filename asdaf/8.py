a=list(map(int, input().split()))
m=len(a)
for i in range(0, m):
    print(a[i], end=' ')
    print(a[m-i-1], end=' ')

