t = int(input())
for i in range(0,t):
    n = int(input())
    l = list(map(int,input().split()))
    a = [i for i in range(1,len(l)+1)]
    i = len(l)-1
    c = 0
    while(i>=0 and x):
        if(a[i][0]!=l[i]):
            if(a[i][1]>0):
                a[i][1]=a[i][1]-1
                x = a[i]
                a.remove(a[i])
                a.insert(i-1,x)
                c = c + 1
        if(a[i][0]!=l[i]):
            if(a[i][1]>0):
                a[i][1]=a[i][1]-1
                x = a[i]
                a.remove(a[i])
                a.insert(i-1,x)
                c = c + 1
        if(a[i][0]!=l[i]):
            x = 0
        i = i-1
    print(a,l)
    if(x==0):
        print('Too chaotic')
    else:
        print(c)