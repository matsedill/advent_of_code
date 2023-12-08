test_input = """30373
25512
65332
33549
35390"""

# Game Plan
## How will we account for found trees?
### - Two lists
###     - x -> indexes of trees that can be seen horizontally
###     - y -> indexes of trees that can be seen vertically
## How do we find visible trees?
### - Looping through each axis from both sides
###     - The first tree on the axis must set a minimum
###         - If we find a tree that is higher we
###             - We add the calculated index to the correct axis
###             - Raise the minimum 
###         - If the minimum is 9 we continue to the next line
### - Finally, we find the intersection between the axes



def go_through_axis(trees, visible_trees, axis, index_offset, reversed):
    minimum = int(trees[0])
    for i, str_tree in enumerate(trees):
        tree = int(str_tree)
        if minimum == 9:
            return visible_trees
        elif minimum < tree or i == 0:
            if reversed:
                if "x" == axis:
                    visible_trees[axis].add(len(trees) - (i + 1) + index_offset)
                elif "y" == axis:
                    visible_trees[axis].add(len(trees) * (len(trees) - (i + 1)) + index_offset)
            else: 
                if "x" == axis:
                    visible_trees[axis].add(i + index_offset)
                elif "y" == axis:
                    visible_trees[axis].add(i*len(trees) + index_offset)
                    pass


            minimum = tree

    return visible_trees


def collect_y_axis(input):
    y_axis = []
    lines = input.splitlines()
    for i in range(len(lines[0])):
        collect_line = []
        for line in lines:
            collect_line.append(line[i])
        y_axis.append(collect_line)
    return y_axis

def main(input):
    visible_trees = {
        "x": set(),
        "y": set()
    }
    for i, line in enumerate(input.splitlines()):
        visible_trees = go_through_axis(list(line), visible_trees, "x", i*len(line), False)
        visible_trees = go_through_axis(list(line[::-1]), visible_trees, "x", i*len(line), True)

    for i, line in enumerate(collect_y_axis(input)):
        visible_trees = go_through_axis(line, visible_trees, "y", i, False)
        visible_trees = go_through_axis(line[::-1], visible_trees, "y", i, True)
 
    print(len(visible_trees["x"].union(visible_trees["y"])))

if __name__ == "__main__":
    # main(test_input)
    with open("input", "r") as f:
        main(f.read())