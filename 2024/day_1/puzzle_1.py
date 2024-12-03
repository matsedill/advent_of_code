input_as_lines = ""
with open("./puzzle_1_input.txt", "r") as f:
    input_as_lines = f.readlines()

list_1 = []
list_2 = []
for line in input_as_lines:
    splitted = line.split(" ")
    first_num = int(splitted[0].strip())
    second_num = int(splitted[-1].strip())
    list_1.append(first_num)
    list_2.append(second_num)


sum = 0
for first_num, second_num in zip(sorted(list_1), sorted(list_2)):
    sum += abs(second_num - first_num)

print(sum)
