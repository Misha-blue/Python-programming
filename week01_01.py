import sys

digit_string = sys.argv[1]

print(sum(int(digit) for digit in digit_string))
