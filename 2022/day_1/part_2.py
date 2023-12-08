
def read_input():
    with open("./input1", "r") as f:
        return f.read()

def main():
    input = read_input()

    counter = 0
    counters = []
    for line in input.splitlines():
        if line == "":
            counters.append(counter)
            counter = 0
        else:
            counter += int(line)
    counters.append(counter) 
    print(sum(sorted(counters, reverse=True)[:3]))



if __name__ == "__main__":
    main()
