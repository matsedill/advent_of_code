"""
This is the solution to advent of code 2nd december 2024
"""

# Open the file and retrieve it contents
input_as_lines = ""
with open("./puzzle_1_input.txt", "r", encoding="utf-8") as f:
    input_as_lines = f.readlines()


def going_the_same_way(list_of_num_str):
    """
    This function goes through a list of integers to see if they are all descending/ascending
    """

    # Change the list of strings to integers
    list_of_num = [int(x) for x in list_of_num_str]

    # We have a counter for when the difference meets our criteria
    iterated_elements = len(letters) - 1

    # We have a list to collect whether they are ascending or not
    ascending = []

    # We use the enumerate function to get the index, so we can lookup the next element
    for index, number in enumerate(list_of_num):

        # To prevent us from going outside the list let's check if this is the last element
        if index < iterated_elements:

            # Get the next number in the list
            next_number = list_of_num[index + 1]

            # Collect whether the difference is ascending or descending
            if number < next_number:
                ascending.append(True)
            else:
                ascending.append(False)

    # We change the list into a set to get the number of unique elements in the list
    ascending_set = set(ascending)

    # There is only one value (True or False), meaning it goes the same way
    return len(ascending_set) == 1


def increasing_by_one_to_three(list_of_num_str):
    """
    This function goes through a list of integers to see if their difference is between 1 and 3
    """
    # Change the list of strings to integers
    list_of_num = [int(x) for x in list_of_num_str]

    # We have a counter for when the difference meets our criteria
    counter = 0

    # We iterate over N - 1, N being the length of the list. We skip the last element because it
    # can't be compared to the next element in the list
    iterated_elements = len(letters) - 1

    # We use the enumerate function to get the index, so we can lookup the next element
    for index, number in enumerate(list_of_num):
        # To prevent us from going outside the list let's check if this is the last element
        if index < iterated_elements:
            # Get the next number in the list
            next_number = list_of_num[index + 1]
            # Get the absolute diffeerence of the two numbers
            difference = abs(next_number - number)
            # If the difference is in this range we count it
            if 0 < difference < 4:
                counter += 1

    # if the counter is equal to the iterated elements all elements met the criteria
    return counter == iterated_elements


counter_for_true = 0
# Go Line by line through the file
for line in input_as_lines:
    # We need to get each letter as well as the next one
    # we start by putting the ltters in a list named letters
    letters = line.split(" ")

    # If the numbers are going the same way and increasing by one to three we count it
    if going_the_same_way(letters) and increasing_by_one_to_three(letters):
        counter_for_true += 1

print("Counter for true: ", counter_for_true)
