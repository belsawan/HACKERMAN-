a=list(map(int, input().split()))
for t in range(0,int(input())):
     a.insert(len(a)-a[-1]-1, a[-1])
     del a[-1]
print(a)
