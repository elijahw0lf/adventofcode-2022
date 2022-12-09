import os

trees = []

def import_trees(tree_file):
    """
        Import the file containing "trees" which are numbers arranged in a grid.
        Each number is converted to an integer and stored into a multidimensional array.
        Eg: A 3x3 grid of incrementing numbers stores the following: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        Args:
            tree_file (str): The filename (or filepath) containing the "trees" to be imported
    """
    global trees
    try:
        with open(tree_file, "r") as f:
            # create a list of each line in the file
            file_lines = f.readlines()

            # loop through each line so we can break up the line into a list of numbers
            for line in file_lines:

                # in one foul swoop we strip the string of it's newline, convert each number to an integer and create a list containing those numbers
                # we go through the trouble of converting the integers because we want to be able to compare the tree heights against each other
                line_array = [int(x) for x in list(line.strip())]

                # now we just append this array to our multidimensional array
                trees.append(line_array)
    except Exception as e:
        print(f"Error opening tree file: {e}")
        exit(1)

def color_print(color, text, end = "\n"):
    """
        Prints the chosen message in a specific color to the terminal.
        Available colors are: purple, blue, cyan, green, orange, red, underline
        (PS: It pains me to type "color" instead of "colour" but that's how the cookie crumbles xD)

        Args:
            color (str) : The color used to print the message
            text (str)  : The text to print in the console
            end (str)   : The character to end the print with (default is newline)
    """
    all_colors = {
        "purple": "\033[95m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "green": "\033[92m",
        "orange": "\033[93m",
        "red": "\033[91m",
        "underline": "\033[4m"
    }
    print(f"{all_colors[color]}{text}"+"\033[0m", end = end)

def search_left_and_right(row):
    global trees
    visible_indexes = []

    # we search from left to right, counting the number of visible trees in that direction
    # the range is len(row)-2 because -1 ensures we stay within range of the array and -2 ensures we don't check the last tree in the row (it's always visible)
    biggest_index = 0
    for v in range(0, len(row)-2):
        # if the tree to the right is taller than the current tallest tree, set it as the tallest and remember it's index
        if row[v+1] > row[biggest_index]:
            biggest_index = v+1
            visible_indexes.append(v+1)

    # now we search from right to left, stopping if we encounter the tallest tree from the left-to-right search
    biggest_index = len(row)-1
    for v in range(len(row)-1, 1, -1):
        
        # if we encounter a tree that is already visible, we can stop checking the remaining trees in the row
        if (v-1) in visible_indexes:
            break
        
        # as before, we check if the tree to the left is taller than the current tallest tree
        if row[v-1] > row[biggest_index]:
            biggest_index = v-1
            visible_indexes.append(v-1)
    return visible_indexes

def calc_visible_trees():
    global trees
    visible_tree_coordinates = set()

    # # preview the tree layout
    # print("Tree Layout:\n")
    # for row in trees:
    #     for tree in row:
    #         print(tree, end="")
    #     print()
    # print(f"\n{'-'*48}\n")
    
    # search rows for trees
    for x in range(1, len(trees)-1):
        # pass each row to the search function and store tree coordinates into the main coord set
        for coord in search_left_and_right(trees[x]):
            visible_tree_coordinates.add((coord, x))

    # search columns for trees (we can re-use the same function used with rows by treating a top-and-bottom search as left-and-right)
    for x in range(1, len(trees[0])-1):
        # pass each column to the search function and store tree coordinates into the main coord set
        col = [row[x] for row in trees]
        for coord in search_left_and_right(col):
            visible_tree_coordinates.add((x, coord))

    
    color_print("underline", f"Final Tree Grid:")
    print("Edge trees are colored blue\nInternal visible trees are colored green\n")

    # print the final grid with colored trees, blue for edge trees and green for visible trees
    for row_index in range(0, len(trees)):
        for column_index in range(0, len(trees[row_index])):
            if row_index == 0 or row_index == len(trees)-1 or column_index == 0 or column_index == len(trees[0])-1:
                # this tree is on the edge, so it's visible (and we'll print in blue to signify this)
                color_print("blue", f"{trees[row_index][column_index]}", end=" ")
            else:
                # the tree isn't on an edge, check if we found its visible and if so, print it in green
                if (row_index, column_index) in visible_tree_coordinates:
                    color_print("green", f"{trees[row_index][column_index]}", end=" ")
                else:
                    print(f"{trees[row_index][column_index]}", end=" ")
        print()

    # calculate the number of visible trees, starting with the edge trees and adding the number of visible trees within the grid
    both_columns = len(trees[0]) * 2
    both_rows = (len(trees) - 2) * 2
    edge_tree_count = both_columns + both_rows
    color_print("underline", "\n\nVisible Tree Count:")
    print(f"Edge trees: {edge_tree_count}")
    print(f"Internal trees: {len(visible_tree_coordinates)}")
    print(f"Total visible: {len(visible_tree_coordinates) + edge_tree_count}\n\n\n")

def main():
    global trees

    # import trees from file
    import_trees("trees.txt")

    # calculate the number of visible trees
    calc_visible_trees()

    color_print("underline", "Part Two: Scenic Score\n")

    # loop through trees that are within the grid (ie: not edge trees) and calculate the scenic score for each
    biggest_scenic_score = 0

    for row_index in range(1, len(trees)-1):
        for column_index in range(1, len(trees)-1):
            left_score, right_score, top_score, bot_score = 0, 0, 0, 0
            # print(f"row_index: {row_index}, column_index: {column_index}, value: {trees[row_index][column_index]}")
            
            # left scenic score
            left_index = column_index - 1
            while True:
                # print(f"looking left to column index {left_index} at tree {trees[row_index][left_index]} ...")
                left_score += 1
                if trees[row_index][left_index] >= trees[row_index][column_index]:
                    # print(f"left tree is equal or bigger, breaking ...")
                    break
                elif left_index == 0:
                    # print("no more trees to the left, breaking ...")
                    break
                # print("left tree is smaller, moving to next tree ...")
                left_index -= 1
            
            # right scenic score
            right_index = column_index + 1
            while True:
                # print(f"looking right to column index {right_index} at tree {trees[row_index][right_index]} ...")
                right_score += 1
                if trees[row_index][right_index] >= trees[row_index][column_index]:
                    # print(f"right tree is equal or bigger, breaking ...")
                    break
                elif right_index == len(trees[0])-1:
                    # print("no more trees to the right, breaking ...")
                    break
                # print("right tree is smaller, moving to next tree ...")
                right_index += 1
            
            # top scenic score
            top_index = row_index - 1
            while True:
                # print(f"looking upwards to row index {top_index} at tree {trees[top_index][column_index]} ...")
                top_score += 1
                if trees[top_index][column_index] >= trees[row_index][column_index]:
                    # print(f"top tree is equal or bigger, breaking ...")
                    break
                elif top_index == 0:
                    # print("no more trees upwards, breaking ...")
                    break
                # print("top tree is smaller, moving to next tree ...")
                top_index -= 1

            # bot scenic score
            bot_index = row_index + 1
            while True:
                # print(f"looking downwards to row index {bot_index} at tree {trees[bot_index][column_index]} ...")
                bot_score += 1
                if trees[bot_index][column_index] >= trees[row_index][column_index]:
                    # print(f"bot tree is equal or bigger, breaking ...")
                    break
                elif bot_index == len(trees)-1:
                    # print("no more trees downwards, breaking ...")
                    break
                # print("bottom tree is smaller, moving to next tree ...")
                bot_index += 1

            this_scenic_score = left_score * right_score * top_score * bot_score
            # print(f"left score: {left_score}\nright score: {right_score}\ntop score: {top_score}\nbottom score: {bot_score}\nscenic score: {this_scenic_score}\n\n")
            if this_scenic_score > biggest_scenic_score:
                biggest_scenic_score = this_scenic_score
        # print()

    print(f"Biggest scenic score: {biggest_scenic_score}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main() # run main function
    print("\n\n")