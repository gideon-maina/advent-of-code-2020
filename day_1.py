# coding: utf-8
def get_sum_to_2020_three_digits(l: list):
    for i in range(len(l)):
        num_a = l[i]
        remainining_list = l[i:]
        for j in range(len(remainining_list)):
            num_b = remainining_list[j]
            remainining_list_two = remainining_list[j:]
            for num_c in remainining_list_two:
                if num_a + num_b + num_c == 2020:
                    print(num_a, num_b, num_c)
                    print(f"Sum is {num_a + num_b + num_c}")
                    print(f"Product is {num_a * num_b * num_c}")
                    return
    print("No sum for 2020")


input_data = [1721, 979, 366, 299, 675, 1456]
