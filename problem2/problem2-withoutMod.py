def main():
    x = 1
    y = 1
    total = 0

    while x <= 4000000:
        total += x + y
        y, x = y + (2 * x), (2 * y) + (3 * x)

    print(total)

main()