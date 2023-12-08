test_input = """30373
25512
65332
33549
35390"""

# Game plan
## Parse the input into a 2D matrix
## Make functions that can navigate in any direction to its edge
## Loop over each tree except the outer rim
## Look in all directions and count visible trees
###     - That is, loop through all trees
###         - For each tree
###             - Look up, down, side to side
###                 -  If on edge then 0
###                 -  The first tree always counts no matter the height
###                 -  Count until the next tree is 
###         -  
###         -  
###         -  

def look_for_eaves(line):


def main(input):
    for line in input.splitlines():
        visible_trees = go_through_axis(list(line), visible_trees), False)

if __name__ == "__main__":
    main(test_input)
    # with open("input", "r") as f:
    #     main(f.read())