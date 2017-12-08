import time


DIVISOR_LIMIT = 20

# Only need to test divisors 11 -> 20, because the smaller numbers are multiples of these
#DIVISORS = (12, 14, 16, 18, 20)
#2, 3, 4, 6,     12
#7               14
#2, 4, 8         16
#2, 3, 6, 9,     18
#2, 4, 5, 10     20

# Testing divisors from largest to lowest had the biggest impact on performance. Around 1/10 execution time

# Incrementing test values by 20 each time -> 1/20 execution time. 

# Combined 1/200 execution time improvement.  48 seconds -> 0.28 seconds

def main():
    start = time.time()
    test_value = DIVISOR_LIMIT

    found = False
    while not found:

        found = True
        for divisor in range(DIVISOR_LIMIT, 11, -1):
            if test_value % divisor != 0:
                test_value += DIVISOR_LIMIT
                found = False

    elapsed = time.time() - start
    print("Found: ", test_value)
    print("elapsed: ", elapsed)



main()