n,d = list(map(int,input().split()))
a = list(map(int,input().split()))
for i in range(0,d):
    x = a[0]
    a.remove(x)
    a.append(x)
print(" ".join(str(i) for i in a ))