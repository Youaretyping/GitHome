class Game(object): # Capture name, then introduction.
	def __init__(self, name):
		self.name = name

    	def announce(self): # Prints the name chosen in a string.
        	print "Hi. I'm a player named", self.name + "\n"
