# Random winner game with class.
import random

class Game(object):# Class used to capture name.
    def __init__(self, name):
#        print "init test"
        self.name = name

    def announce(self): # Prints the name chosen in a string.
        print "Hi. I'm a player named", self.name + "\n"

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
#print "Directly accessing player1.name from Game."
#print player1.name

# TODO - Create customization option for each player.
# TODO - Create another mini game to choose from.