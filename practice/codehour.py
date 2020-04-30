t = int(input())
while(t):
    r,c = list(map(int,input().split()))
    a = list(map(int,input().split()))
    for i in range(0,r*c):
        if(a[i]==1):
            x = i//r
            y = i%c
        for ii in range(0,c):
            a[x*(c-1)+ii]=1
        for jj in range(0,r):
            a[jj*(c-1)+y]=1
    for i in a:
        print(a,end=" ")
    t = t-1
    