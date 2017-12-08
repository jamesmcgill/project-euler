sum = 0
multiple_of_three = 0
multiple_of_five = 0

MAX_RANGE = 1000

is_in_range = lambda x: x < MAX_RANGE

while  is_in_range(multiple_of_three) or is_in_range(multiple_of_five):
    if multiple_of_five < multiple_of_three:
        multiple_of_five += 5
        if is_in_range(multiple_of_five):
            if multiple_of_five != multiple_of_three:
                sum += multiple_of_five

    else:
        multiple_of_three += 3
        if is_in_range(multiple_of_three):
            if multiple_of_five != multiple_of_three:
                sum += multiple_of_three

    print("iter threes:{}, fives{}, sum{}", multiple_of_three, multiple_of_five, sum)

print(sum)
