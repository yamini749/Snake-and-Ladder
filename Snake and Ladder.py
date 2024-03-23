import random
BOARD_SIZE = 10
WINNING_POSITION = BOARD_SIZE * BOARD_SIZE
SNAKES = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def create_board():
    """Create the game board with borders."""
    board = [[" " for _ in range(BOARD_SIZE + 2)] for _ in range(BOARD_SIZE + 2)]
    
    # Fill in borders
    for i in range(BOARD_SIZE + 2):
        board[i][0] = "|"
        board[i][-1] = "|"
    for j in range(BOARD_SIZE + 2):
        board[0][j] = "-"
        board[-1][j] = "-"
    
    # Fill in numbers
    count = 1
    for i in range(1, BOARD_SIZE + 1):
        for j in range(1, BOARD_SIZE + 1):
            if i % 2 == 0:
                board[i][j] = count
            else:
                board[i][BOARD_SIZE - j + 1] = count
            count += 1
    
    return board

def print_board(board, player1_position, player2_position):
    """Print the game board with player positions."""
    for i in range(BOARD_SIZE + 2):
        for j in range(BOARD_SIZE + 2):
            if (i == (player1_position-1) // BOARD_SIZE + 1 and j == (player1_position-1) % BOARD_SIZE + 1):
                print("P1", end="\t")
            elif (i == (player2_position-1) // BOARD_SIZE + 1 and j == (player2_position-1) % BOARD_SIZE + 1):
                print("P2", end="\t")
            else:
                print(board[i][j], end="\t")
        print("\n")

def roll_dice():
    """Simulate rolling a six-sided dice."""
    return random.randint(1, 6)

def move_player(position, dice_value):
    """Move the player based on the dice roll."""
    new_position = position + dice_value
    return min(new_position, WINNING_POSITION)

def check_snake_or_ladder(position):
    """Check if the player encounters a snake or ladder."""
    if position in SNAKES:
        print("Oops, you encountered a snake! Moving down to", SNAKES[position])
        return SNAKES[position]
    elif position in LADDERS:
        print("Hooray, you climbed a ladder! Moving up to", LADDERS[position])
        return LADDERS[position]
    return position

def main():
    print("Welcome to Snake and Ladder Game!")
    print("Let's begin!")

    board = create_board()
    player1_position = 1
    player2_position = 1
    player1_turn = True

    while True:
        print_board(board, player1_position, player2_position)

        if player1_turn:
            print("Player 1's turn")
            input("Press Enter to roll the dice...")
            dice_value = roll_dice()
            print("Player 1 rolled a", dice_value)
            player1_position = move_player(player1_position, dice_value)
            player1_position = check_snake_or_ladder(player1_position)
            if player1_position == WINNING_POSITION:
                print("Player 1 wins!")
                break
        else:
            print("Player 2's turn")
            input("Press Enter to roll the dice...")
            dice_value = roll_dice()
            print("Player 2 rolled a", dice_value)
            player2_position = move_player(player2_position, dice_value)
            player2_position = check_snake_or_ladder(player2_position)
            if player2_position == WINNING_POSITION:
                print("Player 2 wins!")
                break

        player1_turn = not player1_turn

if __name__ == "__main__":
    main()
