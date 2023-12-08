import re

def find_first_digit(str_to_search):
    match = re.search(r'(\d|zero|one|two|three|four|five|six|seven|eight|nine)', str_to_search)
    print(match)
    if match:
        # get the first digit
        return match.group() 
    else:
        print("PANIC") 

def find_last_digit(str_to_search):
    match = re.search(r'(\d|orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', str_to_search)
    if match:
        # get the last digit
        return match.group() 
    else:
        print("PANIC reverse") 

def convert_string_to_number(str_input):
    lookup = {
        "one": "1",
        "eno": "1",
        "two": "2",
        "owt": "2",
        "three": "3",
        "eerht": "3",
        "four": "4",
        "ruof": "4",
        "five": "5",
        "evif": "5",
        "six": "6",
        "xis": "6",
        "seven": "7",
        "neves": "7",
        "eight": "8",
        "thgie": "8",
        "nine": "9",
        "enin": "9",
        "zero": "0",
        "orez": "0",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }
    return lookup[str_input]

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
    lastDigit = find_last_digit(line[::-1])
    print(lastDigit)

    firstDigit = convert_string_to_number(firstDigit)
    lastDigit = convert_string_to_number(lastDigit)
    print(firstDigit, lastDigit)

    # put them together
    number_str = firstDigit + lastDigit

    # make digit
    number = int(number_str)

    # add to sum
    sum_of_number += number

print(sum_of_number)
