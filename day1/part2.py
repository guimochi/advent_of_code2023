import re


def convert_to_int_value(*args):
    # create a dictionary that maps words to digits
    word_to_digit = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    # use a dictionary comprehension to create a list of converted values
    converted_values = [word_to_digit.get(arg, arg) for arg in args]
    # return the list of converted values unpacked into separate values
    return converted_values


def search_number(line: str):
    # defines patterns
    word_pattern = r'one|two|three|four|five|six|seven|eight|nine'
    digit_pattern = r'\d'
    normal_pattern = r'({}|{})'.format(word_pattern, digit_pattern)
    reversed_pattern = r'({}|{})'.format(word_pattern[::-1], digit_pattern)

    # finds first and last digit
    first_digit = re.search(normal_pattern, line).group()
    last_digit = re.search(reversed_pattern, line[::-1]).group()[::-1]

    # combines first and last digit
    first_int_value, last_int_value = convert_to_int_value(first_digit, last_digit)
    final_value = first_int_value + last_int_value

    return int(final_value)


sumLines: int = 0
with open('input.txt') as f:
    for line in f:
        sumLines += search_number(line)

print(sumLines)