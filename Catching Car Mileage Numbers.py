import re


def is_interesting(number, awesome_phrases):
    lst = [number, number + 1, number + 2]
    input_str = str(number)
    if len(input_str) <= 1:
        return 0

    def check_awesome(number, awesome_phrases):
        if number in awesome_phrases:
            return 2
        elif number + 2 in awesome_phrases or number + 1 in awesome_phrases:
            return 1
        else:
            return 0

    def check_zeros(number):
        def check_zero(number):
            if len(str(number)) == 2:
                return 0
            return re.match(r'^[1-9]0*$', str(number))

        zero_result = [check_zero(number) for number in lst]
        if zero_result[0]:
            return 2
        if zero_result[1] or zero_result[2]:
            return 1
        else:
            return 0

    def conf_same_digit(number):
        def same_digit(number):
            if len(str(number)) == 2:
                return 0
            for digit in str(number)[1:]:
                if str(number)[0] != digit:
                    return False
            return True

        same_result = [same_digit(nbr) for nbr in lst]
        if same_result[0]:
            return 2
        if same_result[1] or same_result[2]:
            return 1
        else:
            return 0

    def incementing(number):
        if len(input_str) < 3:
            return 0

        def inc(number):
            input_str = str(number)
            if input_str[-1] == '0' and input_str[-2] == '9':
                input_str = input_str[:-2]

            for digit in range(len(input_str) - 1):
                if int(input_str[digit]) + 1 != int(input_str[digit + 1]):
                    return False
            return True

        inc_result = [inc(nbr) for nbr in lst]
        if inc_result[0]:
            return 2
        if inc_result[1] or inc_result[2]:
            return 1
        else:
            return 0

    def decementing(number):
        if len(input_str) < 3:
            return 0

        def dec(number):
            input_str = str(number)
            if input_str[-1] == '0' and input_str[-2] == '1':
                input_str = input_str[:-1]

            for digit in range(len(input_str) - 1):
                if int(input_str[digit]) - 1 != int(input_str[digit + 1]):
                    return False

            return True

        dec_result = [dec(nbr) for nbr in lst]
        if dec_result[0]:
            return 2
        if dec_result[1] or dec_result[2]:
            return 1
        else:
            return 0

    def palindrome(number):
        def pal(number):
            input_str = str(number)
            if len(input_str) == 2:
                return 0
            if input_str != input_str[::-1]:
                return False
            return True

        pal_result = [pal(nbr) for nbr in lst]
        if pal_result[0]:
            return 2
        if pal_result[1] or pal_result[2]:
            return 1
        else:
            return 0

    return max(check_awesome(number, awesome_phrases), check_zeros(number), conf_same_digit(number),
               incementing(number),
               decementing(number), palindrome(number))


print(is_interesting(30, [1337, 256]))
