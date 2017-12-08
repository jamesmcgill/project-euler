def main():
    accumulator = 0
    y = 1
    x = 2

    #print(y)
    while x <= 4000000:
        #print(x)
        if x % 2 == 0:
            accumulator += x
        y, x = x, y + x

    print("Sum -> ", accumulator)

main()