t = int(input())
d={}
for i in range(0,t):
    b = input()
    if b not in d:
        d[b]=1
        print("OK")
    else:
        print(b+str(d[b]))
        d[b]=d[b]+1