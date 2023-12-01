sumNumbers: int = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        digits = [i for i in line if i.isdigit()]
        first_digit = digits[0]
        last_digit = digits[-1]
        final_digit = first_digit + last_digit
        sumNumbers += int(final_digit)

print(sumNumbers)