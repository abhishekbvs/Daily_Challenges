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
    l,r = list(map(int,input().split()))
    pr=[]
    s = 0
    p0 = l-1
    while (isPrime(p0) == False): 
        p0 -= 1
    pr.append(p0)

    prime = [True for i in range(r+1)] 
    p = 2
    while(p * p <= r): 
           
        if (prime[p] == True): 
               
            for i in range(p * 2, r + 1, p): 
                prime[i] = False
        p += 1

    for p in range(l,r+1): 
        if prime[p]: 
            pr.append(p)
    
    p1=r+1
    while (isPrime(p1) == False): 
        p1 += 1
    pr.append(p1)
    
    s=0
    for i in range(1,len(pr)-1):
        if(2*pr[i]>pr[i-1]+pr[i+1]):
            s=s+1
    print(s)
     