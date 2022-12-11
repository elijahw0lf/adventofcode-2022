import os

def load_rucksacks(filepath):
    """
        Load rucksacks from file, each line contains alphabetic characters representing the items in each rucksack.

        Args:
            filepath (str): The filepath to the file to load.
        
        Returns:
            list: A list containing the values of each line in the file, stripped of newlines and whitespace.
    """
    try:
        with open(filepath, "r") as f:
            return [x.strip() for x in f.readlines()]
    except Exception as e:
        print(f"Failed to read file: {e}\n\n")
        exit(1)

def main():
    # load all rucksacks from file
    all_rucksacks = load_rucksacks("03/rucksacks.txt")

    # the priority value of each letter below is that character's index + 1
    priority_guide = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # string decoration for printing
    underline = "\033[4m"
    reset = "\033[0m"

    # calculate priority total for part one of the puzzle
    priority_total = 0
    for contents in all_rucksacks:
        # we create this variable of the string's middle position to tidy up the two variables below
        halfway = int(len(contents)/2)

        # create a set of each compartment (the first and last halves of the string)
        compartment_one = set(contents[:halfway])
        compartment_two = set(contents[halfway:])

        # to find the common letter in both compartments, we can use the intersection function since we used sets
        # at the end we must pop the value to get the result as a string because the intersection function returns a set
        common = compartment_one.intersection(compartment_two).pop()
        
        # find and add the common letter's priority within the priority_guide string to the total, remembering to add 1 since indexes start at 0
        priority_total += priority_guide.index(common)+1

    print(f"{underline}Part One\n{reset}")
    print(f"Priority total: {priority_total}")

    # calculate priority total for badges in part two of the puzzle
    # since every 3 lines relates to a single group, we use range to iterate in steps of 3
    priority_total = 0
    for r in range(0, len(all_rucksacks), 3):
        # the rucksacks for this group are in index r, r+1 and r+2 of all_rucksacks, we'll make a set of these like in part one
        bag1 = set(all_rucksacks[r])
        bag2 = set(all_rucksacks[r+1])
        bag3 = set(all_rucksacks[r+2])
        
        # to find the common letter (the badge item type) we find the intersection of all 3 sets
        common = bag1.intersection(bag2, bag3).pop()

        # just as before we find and add the common letter's priority to the total
        priority_total += priority_guide.index(common)+1


    print(f"\n\n{underline}Part Two\n{reset}")
    print(f"Priority total: {priority_total}")
    


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    main()
    print("\n\n")