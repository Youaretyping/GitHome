'''                             Random winner game.
            Two players face off for an intense game of epic randomness! 

    Eventually describe how the game operates.        
'''
import random
from game_for_randomGOG import Game	

def start():
	print "\n\nWelcome to my random winning game! Pretend they are arm wrestling or something......... I don\'t know?!\n" # Welcome string for the user.

def player_input():
	name1 = raw_input("\nEnter a name for player 1 > ") 
	player1 = Game(name1) # Instantiate 
	player1.announce() # Invoking the method. The string prints.

	name2 = raw_input("\nEnter a name for player 2 > ") 
	player2 = Game(name2)
	player2.announce()

	roll = [player1.name, player2.name] # Creates variable with players chosen names.
	winner = random.choice(roll) # Creates variable, randomly picks the winner.

	print "Winner is %s" % (winner) + "\n\n" # Announces winner to the user.

def menu():
	start()
	player_input()

menu()
#print "Directly accessing player1.name from Game." # TEST
#print player1.name # TEST

# TODO - Create customization option for each player.
# TODO - Create another mini game to choose from.
# TODO - Create a competition between the two players. Best out of 5 wins the Game of Games. 