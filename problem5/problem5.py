import time

DIVISOR_LIMIT = 20

def main():
    start = time.time()
    test_value = 10

    found = False
    while not found:

        found = True
        for divisor in range(1, DIVISOR_LIMIT):
            if test_value % divisor != 0:
                test_value += 1
                found = False

    elapsed = time.time() - start
    print("Found: ", test_value)
    print("elapsed: ", elapsed)


main()