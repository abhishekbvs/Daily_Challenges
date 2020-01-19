n = list(map(int,input().split()))
l = list(input())
print(n,l)
r = [0 for i  in range (0,10)]
for a in l:
    if(a=='L'):
        x = 1
        i = 0
        while(x):
            if(r[i]==0):
                r[i]=1
                x=0
            i = i+1
            
    elif(a=='R'):
        x = 1
        i = -1
        while(x):
            if(r[i]==0):
                r[i]=1
                x=0
            i = i-1
    else:
        r[int(a)]=0
print(''.join(str(e) for e in r))

