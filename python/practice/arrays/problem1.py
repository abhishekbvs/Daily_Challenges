a=[]
for i in range(0,6): 
    a.append(list(map(int,input().split())))
r = a[0][1-1]+a[0][1]+a[0][1+1]+a[0+1][1]+a[0+2][1-1]+a[0+2][1]+a[0+2][1+1]
for i in range(1,5):
    for j in range(0,4):
        x=a[j][i-1]+a[j][i]+a[j][i+1]+a[j+1][i]+a[j+2][i-1]+a[j+2][i]+a[j+2][i+1] 
        if(x>r):
            r = x
print(r)