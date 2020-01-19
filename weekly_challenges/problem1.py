n,a,x,b,y = list(map(int,input().split()))
x1 = a
y1 = b
flag = 0
while x1!=x and y1!=y  :
    if x1 != x :
        if x1 == n :
            x1 = 1
        else:
            x1 = x1 + 1
    if y1 != y :
        if y1 == 1 :
            y1 = n
        else:
            y1 = y1 - 1
    if x1 == y1:
        flag = 1
        break
if flag:
    print("YES")
else:
    print("NO")
