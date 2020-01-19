t = int(input())
for j in range(0,t):
    n,m,k=list(map(int,input().split()))
    h=list(map(int,input().split()))
    i=0
    c = 1
    while(i<n-1 and c==1):
        r = 1
        a = 1
        while(a<=h[i] and r!=0):
            if(abs(a-h[i+1])<=k):
                r = 0
                m = m + h[i]-a  
                h[i] = a   
            a = a+1
        b = 0
        while(b<=m and r!=0):
            if(abs(h[i]+b-h[i+1])<=k):
                r = 0
                h[i]=h[i]+b
                m = m - b    
            b = b+1
        if(r==1):
            c = 0
        i = i+1
    if(i==n-1 and c==1):
        print('YES')
    else:
        print('NO')