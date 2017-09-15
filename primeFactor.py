# got this algo from stack overflow...
def primes_sieve(limit):
    limitn = limit+1
    is_prime = [True] * limitn #assumes everything is prime
    primes = []
    tenBillionCounter = 0
    for i in range(2, limitn):

        if i % 10000000000 == 0:
            tenBillionCounter +=1
            print "%d Ten Billion Count"

        if (is_prime[i] != True):
            continue

        # eliminate all multiples of the prime through the limit
        for f in xrange(i*2, limitn, i):
            is_prime[f] = False

        primes.append(i)

    return primes

n = 343
primesForN = primes_sieve(n)

print "Largest Prime Number less than or equal to %d is %d" %(n, primesForN[-1])

# now walk backwards through the primes table to find the largest prime factor
for i in range(len(primesForN)-1, 0, -1):
    if n % primesForN[i] == 0:
        print "Largest Prime Factor for %d is %d" %(n, primesForN[i])
        break
