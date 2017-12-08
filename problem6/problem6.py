import time
LIMIT = 100

def sum_of_squares(limit):
    sum = 0
    for i in range(1, limit+1):
        sum += i * i
    return sum

def square_of_sequence(limit):
    sum = 0
    for i in range (1, limit+1):
        sum += i
    return sum * sum

def main():
    start = time.time()

    result = square_of_sequence(LIMIT) - sum_of_squares(LIMIT)
    elapsed = time.time() - start

    print("result: ", result)
    print("elapsed: ", elapsed)



main()