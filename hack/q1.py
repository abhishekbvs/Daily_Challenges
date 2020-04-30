from math import sqrt 

def isPrime(n): 
      
    if (n <= 1): 
        return False
    if (n == 2 or n==3): 
        return True

    if (n % 2 == 0 or n % 3 == 0): 
        return False
      
    k = int(sqrt(n)) + 1
    for i in range(5, k, 6): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
    return True

t=int(input())
for _ in range(t):
    l,r=list(map(int,input().split()))
    p=[]
    s = 0
    p0 = l-1
    while (isPrime(p0) == False): 
        p0 -= 1
    p.append(p0)
    p1=l
    while (isPrime(p1) == False): 
        p1 += 1
    p.append(p1)
    while(p[-1]<=r):
            p2=p[-1]+1
            while (isPrime(p2) == False): 
                p2 += 1
            p.append(p2)
            if(2*p[-2]>p[-1]+p[-3]):
                s = s+1
    print(s)
 
    
         
