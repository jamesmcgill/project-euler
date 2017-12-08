def arithmetic_series_sum(increment, max_range):
    series_count = max_range // increment
    last_of_series = increment * series_count
    return int(((increment + last_of_series) / 2) * series_count)


def main():
    sum_of_three_series = arithmetic_series_sum(3, 999)
    sum_of_five_series = arithmetic_series_sum(5, 999)
    sum_of_fifteen_series = arithmetic_series_sum(15, 999)  #lowest common multiple of 3 and 5 is 15

    print("The sum is:", (sum_of_three_series + sum_of_five_series - sum_of_fifteen_series))

main()