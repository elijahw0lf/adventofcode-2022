import os

class Elf:
    def __init__(self):
        self.calorie_total = 0
    
    def add_food(self, food):
        try:
            self.calorie_total += int(food)
        except Exception as e:
            print(f"Failed to convert food of \"{food}\" to int and add to calorie_total: {e}\n\n")
            exit(1)

def load_food(filepath):
    """
        Load a list of food from a file, with each line containing the calories for a food item. A blank line separates each elf's inventory.
        A list containing the values of each line (stripped of newlines and whitepsace) is returned.

        Args:
            filepath (str): The filepath to the file to load.
    """
    try:
        with open(filepath, "r") as f:
            return [x.strip() for x in f.readlines()]
    except Exception as e:
        print(f"Failed to read file: {e}\n\n")
        exit(1)

def main():
    all_elves = [Elf()] # holds a list of Elf objects, starting with one
    all_food = load_food("01/food.txt") # import the food from file

    # create Elf objects and add food items until the all_food list is empty
    while True:
        if len(all_food) == 0:
            break # no food remaining, break the loop
        
        # if the food value is blank, create a new Elf for the next cycle, otherwise add the food to the last elf
        food = all_food.pop(0)
        if food == "":
            all_elves.append(Elf())
        else:
            all_elves[-1].add_food(food)

    # sort the Elf objects in all_elves by their calorie total
    all_elves.sort(key=lambda v: v.calorie_total, reverse=True)

    # print the Elves with the top 3 calorie totals
    top_3_total = 0
    print(f"\033[4m" + "Parts One and Two:\n\n" + "\033[0m" + "Top 3 Elves by calorie total:")
    for i in range(3):
        top_3_total += all_elves[i].calorie_total
        print(f"#{i+1}: {all_elves[i].calorie_total} calories")
    print(f"\nTotal calories of top 3 elves: {top_3_total}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    main()
    print("\n\n")