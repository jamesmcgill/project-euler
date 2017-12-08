def is_palindrome(x):
    number_string = str(x)
    num_digits = len(number_string)
    for i in range(num_digits // 2):
        if number_string[i] != number_string[-i-1]:
            return False
    return True


def main() :
    left = 999
    right = 999
    max_product = 1

    while True:
        #print("Test {}x{} = {}".format(left, right, left*right))
        product = left * right
        if is_palindrome(product):
            print("--->Palindrom found {}x{} = {}".format(left, right, product))
            if product > max_product:
                max_product = product
       
        if left > 1:
            left -= 1
        elif right > 1:
            right -= 1
            left = right
        else:
            print("MAX -->{}".format(max_product))
            return
main()