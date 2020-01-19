import math
m = input()
n = 0
for d in m:
    n = n*2 +int(d)
if(n!=0):
    x = math.log(n,4)
    print(int(math.ceil(x)))
else:
    print(0)