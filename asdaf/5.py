a=list(map(int, input().split()))
for i in range(len(a)): print(a[i-1], end=' ')
print(str(a[-1])+ " "+' '.join(map(str, a[:-1])))