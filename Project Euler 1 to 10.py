# 1	Multiples of 3 and 5	

s = sum([i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)])
 
# 2	Even Fibonacci numbers	

def fib_sum(n):
    fib = [1,2]
    n1,n2 = 1,2
    while n1+n2 &lt; n:
        fib.append(n1+n2)
        n1,n2 = n2,n1+n2
    return sum(fib[1::3])
 

for i in range(1000000): fibsum = fib_sum(4000000)


# 3	Largest prime factor	

 n = 600851475143
 i = 2
 while i * i < n:
   while n % i == 0:
     n = n / i
   i = i + 1
 print n

# 4	Largest palindrome product	
 n = 0
 for a in xrange(999, 100, -1):
      for b in xrange(a, 100, -1):
         x = a * b
         if x > n:
             s = str(a * b)
             if s == s[::-1]:
                 n = a * b

 print n
 
# 5	Smallest multiple	
 def gcd(a,b): return b and gcd(b, a % b) or a
 def lcm(a,b): return a * b / gcd(a,b)
 n = 1
 for i in xrange(1, 21):
     n = lcm(n, i)
 print n
 
# 6	Sum square difference	
 r = xrange(1, 101)
 a = sum(r)
 print a * a - sum(i*i for i in r)
 
# 7	10001st prime	


def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
 
def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime

prime = nth_prime(10001)
 
print prime

 
# 8	Largest product in a series	

 
L = []
L.append("73167176531330624919225119674426574742355349194934")
L.append("96983520312774506326239578318016984801869478851843")
L.append("85861560789112949495459501737958331952853208805511")
L.append("12540698747158523863050715693290963295227443043557")
L.append("66896648950445244523161731856403098711121722383113")
L.append("62229893423380308135336276614282806444486645238749")
L.append("30358907296290491560440772390713810515859307960866")
L.append("70172427121883998797908792274921901699720888093776")
L.append("65727333001053367881220235421809751254540594752243")
L.append("52584907711670556013604839586446706324415722155397")
L.append("53697817977846174064955149290862569321978468622482")
L.append("83972241375657056057490261407972968652414535100474")
L.append("82166370484403199890008895243450658541227588666881")
L.append("16427171479924442928230863465674813919123162824586")
L.append("17866458359124566529476545682848912883142607690042")
L.append("24219022671055626321111109370544217506941658960408")
L.append("07198403850962455444362981230987879927244284909188")
L.append("84580156166097919133875499200524063689912560717606")
L.append("05886116467109405077541002256983155200055935729725")
L.append("71636269561882670428252483600823257530420752963450")
 
 
M = []
for s in L:
    for t in list(s): M.append(t)
prod = 0
for i in range(len(M)-4):
    p = int(M[i])*int(M[i+1])*int(M[i+2])*int(M[i+3])*int(M[i+4])
    if p > prod: prod = p
print prod
 
 

 
# 9	Special Pythagorean triplet	

 
def prod_triplet_w_sum(n):
    for i in range(1,n,1):
        for j in range(1,n-i,1):
            k = n-i-j
            if i**2+j**2==k**2:
                return i*j*k
    return 0
 

product = prod_triplet_w_sum(1000)

 
print product
 
# 10	Summation of primes

def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
    return sum


sum = prime_sum(2000000)
 
print sum