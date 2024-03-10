import random

# Welcome Message
welcome_message = "Welcome to War!"
print(welcome_message.center(40))

print("\n--------------------------------------------")

# Print the rules
def print_rules():
    print("\nObjective: \n\tBe the first player to win all 52 cards.\n")
    print("Deal: \n\tEach player gets 26 cards.\n")
    print("Gameplay:")
    print("\t- Players simultaneously reveal the top card of their stack.")
    print("\t- The player with the higher card takes both and puts them face down at the bottom of their stack.")
    print("\t- In case of cards with the same rank, it's War.")
    print("\t- During War, each player puts one card face down and one face up.")
    print("\t- The player with the higher face-up card takes both piles (six cards).")
    print("\t- If there's another tie, repeat the process until a winner emerges.\n")
    print("\tScoring: The game ends when one player has won all 52 cards.\n")

print_rules()

print("--------------------------------------------")

# Get player's name
player_name = input("\nEnter your name: ").strip().title()
if not player_name:
    player_name = "Player"

# Get the number of facedown cards
while True:
    num_facedown_input = input("Enter the number of facedown cards during tiebreakers (default is 1): ")
    if not num_facedown_input:
        num_facedown = 1
        break
    try:
        num_facedown = int(num_facedown_input)
        if num_facedown >= 0:
            break
        else:
            print("Please enter a non-negative number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Create a deck of cards and assign values to each card rank
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
card_values = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}

# Create a deck of cards with assigned values
deck = [{'rank': rank, 'suit': suit, 'value': card_values[rank]} for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)
deck1 = deck[:26]
deck2 = deck[26:]

# Create in-play area
in_play = []

# Variable to keep track of rounds
round_number = 1

# Play multiple rounds
while deck1 and deck2:  # Continue until one of the decks is empty
    print("\n--------------------------------------------")
    print(f"\nRound: {round_number}")

    # Pop off the first card from each deck and put them in play
    player_card = deck1.pop(0)
    computer_card = deck2.pop(0)

    # Check if there are cards left in both decks
    if player_card and computer_card:
        # Put the cards in the in_play area
        in_play.append(player_card)
        in_play.append(computer_card)

        # Print who plays what
        print(f"\n\t{player_name} plays: \t\t{player_card['rank']} of {player_card['suit']}")
        print(f"\tComputer plays: \t{computer_card['rank']} of {computer_card['suit']}")

        # Determine the winner of the round
        while player_card['value'] == computer_card['value']:
            print("\n\tIt's a tie! This. Means. WAR!")

            # Each player plays facedown and faceup cards
            for _ in range(num_facedown):
                player_card_down = deck1.pop(0) if deck1 else None
                computer_card_down = deck2.pop(0) if deck2 else None
                in_play.extend([player_card_down, computer_card_down])

            # Each player plays faceup cards
            player_card_up = deck1.pop(0) if deck1 else None
            computer_card_up = deck2.pop(0) if deck2 else None

            # Check if there are enough cards for the tiebreaker
            if len(deck1) >= num_facedown and len(deck2) >= num_facedown:
                in_play.extend([player_card_up, computer_card_up])

                # Print the facedown and faceup cards
                print(f"\n\t{player_name} and Computer each play {num_facedown} cards facedown")
                print(f"\t{player_name} plays faceup: {player_card_up['rank']} of {player_card_up['suit']}")
                print(f"\tComputer plays faceup: {computer_card_up['rank']} of {computer_card_up['suit']}")
            else:
                # Not enough cards for tiebreaker, end the game
                print("\nNot enough cards for tiebreaker. Game Over.")
                break

            # Update the player and computer cards for comparison
            player_card = player_card_up
            computer_card = computer_card_up

        # Check the winner of the round and move cards accordingly
        if player_card['value'] > computer_card['value']:
            deck1.extend(in_play)
            print(f"\n\t{player_name} wins {len(in_play)} cards!")
        else:
            deck2.extend(in_play)
            print(f"\n\tComputer wins {len(in_play)} cards!")

        # Increment the round number
        round_number += 1

        # Print the current status of each player's deck
        print(f"\n\t{player_name} \t\tDeck: {len(deck1)} ({round((len(deck1) / 52) * 100)}%)")
        print(f"\tComputer \tDeck: {len(deck2)} ({round((len(deck2) / 52) * 100)}%)")

        # Prompt for Enter input before proceeding to the next round
        user_input = input("\nPress Enter to continue ('q' to quit): ").lower()
        if user_input == 'q':
            print("\n\tYou chose to quit.\n")
            break

        # Clear the in_play area for the next round
        in_play.clear()

    else:
        # Not enough cards to continue the game
        print("\nNot enough cards to continue. Game Over.")
        break

# Print the winner of the game
if not deck1:
    print("--------------------------------------------\n")
    print("Game Over.".center(50, ' '))
    print("\n" + "Computer wins War!".center(50, ' ') + "\n")
    print("--------------------------------------------")
else:
    print("--------------------------------------------\n")
    print("Game Over.".center(50, ' '))
    print("\n" + f"{player_name} wins War!".center(50, ' ') + "\n")
    print("--------------------------------------------")
