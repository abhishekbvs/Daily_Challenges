n = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
p,x,c = [0,0,0]
for i in a:
    y = 1
    while x<len(b) and y==1:
        if i<b[x] :
            p = p+b[x]
            y = 0
            c = c+1
        x = x+1
if(c==len(a)):
    print("YES")
    print(p)
else:
    print("NO")