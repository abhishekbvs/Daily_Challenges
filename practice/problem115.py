b = []
b.append([[8,3,4],[1,5,9],[6,7,2]])
b.append([[6,7,2],[1,5,9],[8,3,4]])
b.append([[4,9,2],[3,5,7],[8,1,6]])
b.append([[8,1,6],[3,5,7],[4,9,2]])
b.append([[2,7,6],[9,5,1],[4,3,8]])
b.append([[4,3,8],[9,5,1],[2,7,6]])
b.append([[6,1,8],[7,5,3],[2,9,4]])
b.append([[2,9,4],[7,5,3],[6,1,8]])
a = []
for i in range(0,3):
    a.append(list(map(int,input().split())))
c = []
for i in range(0,8):
    y = 0
    for j in range(0,3):
        for k in range(0,3):
            y = y+abs(b[i][j][k]-a[j][k])
    c.append(y)
print(min(c))
