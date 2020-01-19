n,k = list(map(int,input().split()))
l=[]
for i in range(0,n):
    a,b=list(map(int,input().split()))
    l.append([a,b])
l=sorted(l,key=lambda x : (x[1],x[0]),reverse=True)
r = 0
for li in l:
    if(li[1]==1 and k>0):
        r = r + li[0]
        k = k -1
    elif(li[1]==1 and k==0):
        r = r - li[0]
    elif(li[1]==0):
        r = r + li[0]
print(r)