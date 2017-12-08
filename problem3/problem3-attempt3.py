# Improved version of solution given by bitRake on ProjectEuler forums

import math
import time

def main():
    start = time.time()
    target = 600851475143
    divisor = 1

    while True:
        divisor += 1
        if (target % divisor) == 0:
            target /= divisor
            if target == 1:
                break
            divisor = 1

    print(divisor)

    elapsed = time.time() - start
    print(elapsed)


main()
