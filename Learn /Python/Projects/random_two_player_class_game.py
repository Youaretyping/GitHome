'''                             Random winner game.
            Two players face off for an intense game of epic randomness! 

Functionality of the game.

1. Start function will be called to welcome the user to this game. 
#DONE#

2. player_input will display to capture user name and preferences.
Here is the list of options for player customization. 
(a menu will print to screen with these choices)
Choose name, choose what type of being. human - alien - monster - prompt the player to enter a fourth being of their own choice
3. Have a choice of games both players can choose from. Write a way to store a win and losses to declare a winner, best of 5.

?? to use  classes for each player_input

After player has completed their customization 
'''
import random
from game_for_randomGOG import Game	

def start():
	print "\n\nWelcome to my random winning game! Pretend they are arm wrestling or something......... I don\'t know?!\n" # Welcome string for the user.

def player_input():
	name1 = raw_input("\nEnter a name for player 1 > ") 
	being1 = raw_input("\nWhat type of being would you like to be? > ")
	player1 = Game(name1) # Instantiate 
	player1.append(being1)
	player1.announce() # Invoking the method. The string prints.

	name2 = raw_input("\nEnter a name for player 2 > ") 
	player2 = Game(name2)
	being2 = raw_input("\nWhat type of being would you like to be? > ")
	player2.append(being2)
	player2.announce()

def determin_winner():	
	roll = [player1.name, player2.name] # Creates variable with players chosen names.
	winner = random.choice(roll) # Creates variable, randomly picks the winner.
	print "Winner is %s" % (winner) + "\n\n" # Announces winner to the user.

def menu():
	start()
	player_input()
	determin_winner()
	menu()

menu()
#print "Directly accessing player1.name from Game." # TEST
#print player1.name # TEST

# TODO - Create customization option for each player.
# TODO - Create another mini game to choose from.
# TODO - Create a competition between the two players. Best out of 5 wins the Game of Games. 