# coding: utf-8
def check_valid_pwds(passwords: list):
    valid = 0

    for pwd in passwords:
        text = pwd.split(":")[1].strip()
        rules, letter = pwd.split(":")[0].split()
        min_, max_ = rules.split("-")
        count = text.count(letter)
        if count >= int(min_) and count <= int(max_):
            valid += 1
    return valid


def check_valid_pwds_2(passwords: list):
    valid = 0

    for pwd in passwords:
        text = pwd.split(":")[1].strip()
        rules, letter = pwd.split(":")[0].split()
        index_one, index_two = rules.split("-")
        if text[int(index_one) - 1] == letter and text[int(index_two) - 1] != letter:
            valid += 1
        elif text[int(index_two) - 1] == letter and text[int(index_one) - 1] != letter:
            valid += 1
    return valid


input_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
