import os

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.move = 0 # holds the player's current move, 1 = rock, 2 = paper, 3 = scissors
    
    def add_points(self, points):
        """
            Add points to the player's total score. When this function is called, the player's current move score is also added to the total score.

            Args:
                points (int): The amount of points to be added to the player's score.
        """
        self.score += points + self.move
    
    def assign_move(self, move):
        """
            Assign the player's move based on the single letter in the provided string. We store the move as an integer that is equal to that move's score.
            A or X is rock, B or Y is paper, C or Z is scissors

            Args:
                move (str): The single character from the strategy list representing the player's move.
        """
        if move == "A" or move == "X":
            self.move = 1
        elif move == "B" or move == "Y":
            self.move = 2
        elif move == "C" or move == "Z":
            self.move = 3

def load_strategy(filepath):
    """
        Load a rock, paper, scissors strategy from a file, with each line containing a string of two letters separated by a space.
        A list containing the values of each line (stripped of newlines and whitespace) is returned.

        Args:
            filepath (str): The filepath to the file to load.
    """
    try:
        with open(filepath, "r") as f:
            return [x.strip() for x in f.readlines()]
    except Exception as e:
        print(f"Failed to read file: {e}\n\n")
        exit(1)

def play_game(strategy, mode):
    """
        Play all games of rock, paper, scissors from the provided strategy. The mode variable decides whether we play using rules from part one or part two of the puzzle.
        The only difference between parts one and two of the puzzle is what move is assigned to our player object.

        Args:
            strategy (list): A list of strings loaded from load_strategy().
            mode (int): Chooses the rules of the puzzle, 1 = part one, 2 = part two.
        
        Returns:
            list: A list containing both player objects, index 0 is the opponent and index 1 is the player.
    """


    # create two players, allowing us to assign the player's move and their score
    opponent, you = Player("opponent"), Player("you")
    
    # we place both players in a list so we can sort it by the player's move value, allowing us to find the winner without if statements
    # eg: if we know one player threw scissors (move=3) and the other threw rock (move=1), the player in index 0 threw rock and is the winner
    match = [opponent, you]

    # for part two, the 3d dict below will provide us with the correct move to play
    # index 1 is the opponent's move and index 2 is the chosen strategy ("Y" is draw so it's ignored)
    strategy_guide = {
        1: {"X": "C", "Z": "B"},
        2: {"X": "A", "Z": "C"},
        3: {"X": "B", "Z": "A"}
    }

    # loop through each game in the strategy list
    for game in strategy:

        # assign the opponent's move
        opponent.assign_move(game[0])

        # assign the player's move depending on the chosen mode
        if mode == 1:
            you.assign_move(game[2])
        elif mode == 2:
            # if the strategy is to draw, assign the same move as the opponent, otherwise assign the strategy from strategy_guide
            if game[2] == "Y":
                you.assign_move(game[0])
            else:
                you.assign_move(strategy_guide[opponent.move][game[2]])
        
        # sort the match list by the value of the player's move
        match.sort(key=lambda v: v.move)

        # check if there was a draw or not
        if opponent.move == you.move:
            # the game was a draw, award both players 3 points
            opponent.add_points(3)
            you.add_points(3)
        else:
            # not a draw, if the players threw rock + scissors then the winner is in match[0], otherwise the winner is in match[1]
            winner = match.pop(0) if opponent.move in [1,3] and you.move in [1,3] else match.pop(1)
            loser = match.pop() # the remaining user in match is the loser
            
            # add points to the winner and loser
            winner.add_points(6)
            loser.add_points(0)

            # reload the match list for the next game since we popped them earlier
            match = [opponent, you]
    
    # return both player objects so we can print their scores
    return [opponent, you]

def main():
    strategy = load_strategy("02/strategy.txt")

    # string decoration for printing
    underline = "\033[4m"
    reset = "\033[0m"

    # play the game using rules from part one of the puzzle
    part_one = play_game(strategy, 1)
    print(f"{underline}Part One\n{reset}")
    print(f"Opponent's score: {part_one[0].score}")
    print(f"Your score: {part_one[1].score}")
    
    # play the game using rules from part two of the puzzle
    part_two = play_game(strategy, 2)
    print(f"\n\n{underline}Part Two\n{reset}")
    print(f"Opponent's score: {part_two[0].score}")
    print(f"Your score: {part_two[1].score}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    main()
    print("\n\n")