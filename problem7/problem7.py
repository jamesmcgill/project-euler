import time

# Primes are numbers which are:
# - Odd
# - Can't be divided integrally with previous primes
# TODO - another condition that means we can skip ahead some. Don't want to check every odd number as the distance between primes increases.
def prime_numbers():
    primes = [2]
    yield 2

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
            #import pdb; pdb.set_trace()

        current += 2    # skip even numbers

def get_nth_prime(n):
    for i, v in enumerate(prime_numbers()):
        #print("i:{}, v:{} ".format(i, v))
        if i == (n-1):
            return v
    return -1


def main():
    start = time.time()
    result = get_nth_prime(10001)

    elapsed = time.time() - start
    print("result: ", result)
    print("elapsed: ", elapsed)

main()