# We import the random module because we will be using this for the Computer to generate moves (that is, choose rock,
# paper, or scissors)
import random


# This list stores the possible moves the player and computer can make
rpscomp = ["Rock", "Paper", "Scissors"]


# This dictionary stores the player's response to whether they want to play again.  In the beginning of the program,
# we assume that the answer to this question is 'yes' because we want them play this super cool and simple game
play_game = {"answer": "yes"}


# This function finds the name of the player
def player_name_finder():
    global player_name
    player_name = input("\n\nWhat is your name, user?\n")


# This function introduces the game to the player.  The main reason this was not included in the funtion game() was
# because it would interefere with the game flow if the player put an invalid input.  That is, after putting the invalid
# input, the game would again say "Come on, player_name!  Let's play Rock–Paper–Scissors!".  This was not an ideal
# situation, hence, the game introdution has its own function.
def game_introduction():
    print("\nCome on, " + player_name + "!" + "\nLet's play Rock–Paper–Scissors!")


# This function is the game itself.  It collects the player's name, their move, it generates the computer's move,
# determines who won or whether it is a tie.  Finally, the function prints out the winner and asks the user if they want
# to play the game again.
def game():
    global player_name
    while play_game["answer"] == "yes":
        if play_game["answer"] == "yes":
            player_input = input("\n\nDo you choose 'Rock', 'Paper', or 'Scissors'?\n")
            computer = str(random.choice(rpscomp))
            print("The computer chose: " + computer)
            if player_input == computer:
                print("Whoa!  That's a tie, " + player_name + "!")
            elif player_input == "Rock":
                if computer == "Paper":
                    print("\nOh no!  You lose, " + player_name + "!")
                elif computer == "Scissors":
                    print("\nCongratulations, " + player_name + "!" + "  You won!")
            elif player_input == "Paper":
                if computer == "Rock":
                    print("\nCongratulations, " + player_name + "!" + "  You won!")
                elif computer == "Scissors":
                    print("\nOh no!  You lose, " + player_name + "!")
            elif player_input == "Scissors":
                if computer == "Rock":
                    print("\nOh no!  You lose, " + player_name + "!")
                elif computer == "Paper":
                    print("\nCongratulations, " + player_name + "!" + "  You won!")

        # for first letter not capitalized

            elif player_input == "rock":
                if computer == "Rock":
                    print("Whoa!  That's a tie, " + player_name + "!")
                elif computer == "Paper":
                    print("\nOh no!  You lose, " + player_name + "!")
                elif computer == "Scissors":
                    print("\nCongratulations, " + player_name + "!" + "  You won!")
            elif player_input == "paper":
                if computer == "Paper":
                    print("Whoa!  That's a tie, " + player_name + "!")
                elif computer == "Rock":
                    print("\nCongratulations, " + player_name + "!" + "  You won!")
                elif computer == "Scissors":
                    print("\nOh no!  You lose, " + player_name + "!")
            elif player_input == "scissors":
                if computer == "Scissors":
                    print("Whoa!  That's a tie, " + player_name + "!")
                elif computer == "Rock":
                    print("\nOh no!  You lose, " + player_name + "!")
                elif computer == "Paper":
                    print("\nCongratulations, " + player_name + "!" + "  You won!")
            else:
                print("Sorry!  Looks like that was an invalid input, " + player_name + ".")
                print("\nMaybe check your answer and try again")
                game()

        play_game["answer"] = input("\n\nDo you want to play again, " + player_name + "?\n").lower()

        if play_game["answer"] != "yes":
            print("\n\nThanks for playing, " + player_name + "!")


# This function runs the game
def game_initiate():
    player_name_finder()

    game_introduction()

    game()


# Let's play!
game_initiate()
