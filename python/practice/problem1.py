n = int(input())
s = list(input())
r = 0
x = 0
for i in range(0,len(s)):
    if(r==0):
        a = 0
    else:
        a =1
    if(s[i]=='U'):
        r = r+1
    elif(s[i]=='D'):
        r = r-1
    if(r<0 and a==0):
        x = x+1
print(n,s,x)
