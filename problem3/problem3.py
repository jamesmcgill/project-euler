#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
from math import sqrt
import time


# Primes are numbers which are:
# - Odd
# - Can't be divided integrally with previous primes
# TODO - another condition that means we can skip ahead some. Don't want to check every odd number as the distance between primes increases.
def prime_numbers():
    primes = []
    current = 3

    while True:
        is_prime = True
        for i in primes:
            if current % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(current)
            yield current

        current += 2    # skip even numbers

def main():
    start = time.time()
    target = 600851475143
    range = sqrt(target)

    prime_factors = []
    for i in prime_numbers():
        if target % i == 0:
            prime_factors.append(i)
            target = target // i
        if i > range:
            break

    print(prime_factors)
    elapsed_time = time.time() - start
    print(elapsed_time)


main()