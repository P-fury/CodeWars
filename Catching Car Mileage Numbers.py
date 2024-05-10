"""
Catching Car Mileage Numbers
https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python
"""
import re

def is_interesting(number, awesome_phrases):
    def check_awesome(n):
        if n in awesome_phrases:
            return 2
        elif n + 1 in awesome_phrases or n + 2 in awesome_phrases:
            return 1
        return 0

    def check_conditions(n):
        input_str = str(n)
        if len(input_str) <= 2:
            return 0
        return any([
            re.match(r'^[1-9]0*$', input_str),
            all(input_str[0] == digit for digit in input_str),
            all(
                int(input_str[i]) + 1 == int(input_str[i + 1]) or
                (input_str[i] == '9' and input_str[i + 1] == '0')
                for i in range(len(input_str) - 1)
            ),
            all(
                int(input_str[i]) - 1 == int(input_str[i + 1]) or
                (input_str[i] == '1' and input_str[i+1] == '0')
                for i in range(len(input_str)-1)
            ),
            input_str == input_str[::-1],
        ])


    if check_awesome(number) == 2 or (check_conditions(number) and check_awesome(number) != 1):
        return 2
    elif check_awesome(number) == 1 or any(check_conditions(n) for n in [number + 1, number + 2]):
        return 1
    return 0


print(is_interesting(678290,[]))