def get_multiplied_digits(number = 1986):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    return int(str_number[0])

print(get_multiplied_digits())
