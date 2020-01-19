from collections import defaultdict
def sync(a,b):
    r = 0
    for i,ai in enumerate(a):
        if(b[1]<ai[0]-1):
            a.insert(i,b)
            r = 1
            break
        elif(b[0]<=ai[0] and b[1]>=ai[1]):
            a.remove(ai)
        elif(b[0]<=ai[0]-1 and b[1]>=ai[0]-1 and b[1]<=ai[1]):
            a.insert(i,[b[0],ai[1]])
            a.remove(ai)
            r = 1
            break
        elif(b[0]<=ai[0] and b[1]>=ai[1]):
            b[1]=ai[1]
            a.remove(ai)
        elif(b[0]>=ai[0] and b[1]<=ai[1]):
            r = 1
            break
        elif(b[0]>=ai[0] and b[0]<=ai[1]+1 and b[1]>=ai[1]):
            b[0]=ai[0]
            a.remove(ai)
    if(r==0):
        a.append(b)

n,m,k=list(map(int,input().split()))
d=defaultdict(list)
for i in range(0,k):
    s=list(map(int,input().split()))
    sync(d[s[0]],[s[1],s[2]])
print(d)
z = 0
for c in d.values():
    for e in c:
        z = z +e[1]-e[0]+1
print(n*m-z)



