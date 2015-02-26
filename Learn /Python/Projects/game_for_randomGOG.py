''' Each mini game will use this module to create

'''
'''
class Game(object): # Capture name, then introduction.
	def __init__(self, name):
		self.name = name

    	def announce(self): # Prints the name chosen in a string.
        	print "Hi. I'm a player named", self.name + "\n"


# Below is a work in progress to expand the Game class in order to create player customizations.
'''

class Game(object): 	
	def __init__(self, name, being):
		self.name = name
		self.being = being

    	def announce(self): # Prints the name chosen in a string.
        	print "Hi. I'm a player named", self.name + "who is a", self.being
        	+ "\n"
        

