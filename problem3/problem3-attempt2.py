import math
import time

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if (x % i) == 0:
            return False
    return True


def main():
    start = time.time()
    target = 600851475143
    max_factor = None
    for i in range(2, int(math.sqrt(target))+1):
        if (target % i) == 0:
            result = target // i
            if is_prime(result):
                max_factor = result
                return
            elif is_prime(i):
                max_factor = i

    print(max_factor)
    elapsed = time.time() - start
    print(elapsed)


main()
