a=list(map(int, input().split()))
for i in range(0, len(a), 2): a[i-2:i-1], a[i-1:i]=a[i-1:i], a[i-2:i-1]
print(a)