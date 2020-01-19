n,l,r = list(map(int,input().split()))
a = 0
for i in range(0,l):
    x = pow(2,i)
    a = a + x
a = a + 1*(n-l)
b = 0
for i in range(0,r):
    x = pow(2,i)
    b = b + x
b = b + (n-r)*(pow(2,r-1))
print(str(a)+" "+str(b))
