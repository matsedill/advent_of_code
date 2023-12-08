import re

def find_first_digit(str_to_search):
    match = re.search(r'\d', str_to_search)
    if match:
        # get the first digit
        return match.group() 
    else:
        print("PANIC") 

str_input = ""
with open("input", "r") as f:
    str_input = f.read()

sum_of_number = 0
for line in str_input.splitlines():
    print("line:", line)
    # Find the first digit
    firstDigit = find_first_digit(line)
    print(firstDigit)

    # Find the first digit in the reverse string
    print("reverse line:", line[::-1])
    lastDigit = find_first_digit(line[::-1])
    print(lastDigit)

    # put them together
    number_str = firstDigit + lastDigit

    # make digit
    number = int(number_str)

    # add to sum
    sum_of_number += number

print(sum_of_number)
