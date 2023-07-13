def evaluate_domino_move(left, right, domino):
    """
    Evaluates a domino move and returns a score.
    Adjust the scoring criteria based on your strategy.
    """
    # Example scoring criteria:
    score = 0

    # Prefer moves that connect to the ends with matching numbers
    if domino[0] == left or domino[1] == left:
        score += 1
    if domino[0] == right or domino[1] == right:
        score += 1

    # Other scoring criteria can be added here

    return score


def find_best_domino_move(left, right, player_hand):
    """
    Finds the best domino move from the player's hand.
    """
    best_move = None
    best_score = -1

    for domino in player_hand:
        score = evaluate_domino_move(left, right, domino)
        if score > best_score:
            best_move = domino
            best_score = score

    return best_move


# ANSI escape sequences for text formatting
ANSI_RED = "\033[31m"
ANSI_YELLOW = "\033[33m"
ANSI_RESET = "\033[0m"


# Example usage:
player_hand = []
played_cards = []

# Input the initial hand of 7 cards
print("Enter your initial hand of 7 cards:")
for _ in range(7):
    while True:
        card = input("Enter a card (0-6): ")
        if len(card.split('-')) != 2:
            print(ANSI_RED + "Invalid input format. Please enter a valid card in the format 'x-y'." + ANSI_RESET)
        else:
            num1, num2 = map(int, card.split('-'))
            if 0 <= num1 <= 6 and 0 <= num2 <= 6:
                player_hand.append((num1, num2))
                break
            else:
                print(ANSI_RED + "Invalid input. Please enter a valid card with numbers between 0 and 6." + ANSI_RESET)

while True:
    left_end = int(input("Enter the left end number (0 if starting the game): "))
    right_end = int(input("Enter the right end number (0 if starting the game): "))

    if left_end == 0 and right_end == 0:
        played_cards = []
    else:
        played_input = input(ANSI_YELLOW + "Enter the recently played cards (e.g., 2-3 4-5): " + ANSI_RESET)
        played_cards.extend(tuple(map(int, pair.split('-'))) for pair in played_input.split())

    # Remove already played cards from player's hand
    player_hand = [domino for domino in player_hand if domino not in played_cards]

    best_move = find_best_domino_move(left_end, right_end, player_hand)
    if best_move:
        print(ANSI_RED + "Best move:", str(best_move) + ANSI_RESET)
    else:
        print("No valid move found.")

    withdraw_input = input("Enter the dominoes you've withdrawn (e.g., 2-3 4-5), or press Enter to skip: ")
    if withdraw_input:
        withdrawn_cards = [tuple(map(int, pair.split('-'))) for pair in withdraw_input.split()]
        player_hand.extend(withdrawn_cards)

    if len(player_hand) == 0:
        print("You have no more cards. You won!")
        break
