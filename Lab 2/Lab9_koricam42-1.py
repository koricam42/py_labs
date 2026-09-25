"""
Program Name: Match Coins (Main)
Author: Jordan Mensah
Purpose: Runs main game loop, creates the objects, and manages the rules/winners
Starter Code: N/A
Date: 9/21/26
"""

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("\nMatch Coin Game")

    while True:        
            print(f"Player 1 has {player1.get_wallet()} coins")
            print(f"Player 2 has {player2.get_wallet()} coins")
            print()

            player_choice = input("Do you want to flip the coins?\nInput 'Y' or 'y' to flip, 'N' or 'n' to exit the game")
            print()

            if player_choice == 'Y' or player_choice == 'y':
                print("Tossed!")
                player1.toss_coin()
                player2.toss_coin()

                p1_side = player1.get_coin_side()
                p2_side = player2.get_coin_side()
                
                print(f'Player 1 tossed {p1_side}')
                print(f'Player 2 tossed {p2_side}')
                print()

                if p1_side == p2_side:
                    print("It's a match! Player 1 wins!")
                    print()
                    player1.win_coin()
                    player2.lose_coin()
                else:
                    print("It's not a match! Player 2 wins!")
                    print()
                    player1.lose_coin()
                    player2.win_coin()


            elif player_choice == "N" or player_choice == "n":
                break
            else:  
                print("Invalid input.")


    print("Current Score")
    print(f'Player 1: {player1.get_wallet()}')
    print(f'Player 2: {player2.get_wallet()}')

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 finished with more coins.")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 finished with more coins.")
    else:
         print("It's a draw.")
main()