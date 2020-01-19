s=list(input())
n=int(input())
a = []
x  = 0
for i in range(0,len(s)):
    if(s[i]=='a'):
        a.append(i)
        x=x+1
r = int(n/len(s))*x
b = n%len(s)-1
for j in a:
    if(j<=b):
        r=r+1
    else:
        break
print(r)

