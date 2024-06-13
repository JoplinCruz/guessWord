import random


class WordList:
	
	words: list = ["girl", "children", "horse", "knife", "house", "elevator", "marshmallow", "table", "window", "script", "rainbow", "stone", "strong", "grandma", "glasses", "dinosaur", "pink", "banana", "apple", "orange", "chicken", "dog","cat", "eagle", "crocodile", "laze", "laundry", "gate", "world", "car", "truck", "mother"]
	
	clearScreen: str = "\033[2J"
	locate: str = "\033[{};{}H"
		
	foregroundColors: dict = {"black": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "magenta": 35, "cyan": 36, "white": 37, "none": 38, "default": 39, "reset": 0}
	backgroundColors: dict = {"black": 40, "red": 41, "green": 42, "yellow": 43, "blue": 44, "magenta": 45, "cyan": 46, "white": 47, "none": 48, "default": 49, "reset": 0}
	colorBright_FB: str = "\033[1;{};{}m"
	colorBright: str = "\033[1;{}m"
	colorDimmed: str = "\033[2;{}m"
	colorItalic: str = "\033[3;{}m"
	colorUnderline: str = "\033[4;{}m"
	colorBlinking: str = "\033[5;{}m"
	colorNone: str = "\033[6;{}m"
	colorInverse: str = "\033[7;{}m"
	colorHidden: str = "\033[8;{}m"
	colorStrikeThrough: str = "\033[9;{}m"
	colorReset: str = "\033[0m"
		
	foreColor256: str = "\033[38;5;{}m"
	backColor256: str = "\033[48;5;{}m"


class GuessWord:
	
	def __init__(self):
		self.trying: int = 5
		self.counter: int = 0
		self.found: bool = False
		self.run: bool = True
		
		self.choice = ""
		self.length: int = 0
		self.wordChoice: list = []
		self.wrongs: list = []
		
		self.message = "You have {} {}.".format(self.trying, "changes" if self.trying > 1 else "change")
		
		self.clearScreen: str = "\033[2J"
		self.locate = "\033[{};{}H"
	
	
	def gameBoard(self):
		print (self.clearScreen)
		print (self.locate.format(1,1)+WordList.colorBright.format(WordList.foregroundColors["green"])+"=================[  GUESS THE WORD  ]=================="+WordList.colorReset)
		print (self.locate.format(4,3)+"Word: "+WordList.colorBright.format(WordList.foregroundColors["yellow"])+"{}".format(" ".join(self.wordChoice))+WordList.colorReset)
		print (self.locate.format(4,33)+"Wrongs: "+WordList.colorDimmed.format(WordList.foregroundColors["red"])+"{}".format("-".join(self.wrongs))+WordList.colorReset)
		print (self.locate.format(10,3)+"Message: "+WordList.colorDimmed.format(WordList.foregroundColors["red"])+"{}".format(self.message)+WordList.colorReset)
		print (self.locate.format(12,1)+WordList.colorBright.format(WordList.foregroundColors["green"])+"======================================================="+WordList.colorReset)
	
	
	def changeWord(self):
		self.choice: str = random.choice(WordList.words)
		self.length: int = len(self.choice)
		self.wordChoice: list = ["_"] * self.length
	
	
	def playAgain(self):
		playAgain: str = input(self.locate.format(6,3)+"Play again (y/n)? ")
		if playAgain.lower() in ["yes", "y", "ok"]:
			self.trying = 5
			self.counter = 0
			self.wrongs = []
			self.message = "You have {} {}.".format(self.trying, "changes" if self.trying > 1 else "change")
			self.changeWord()
			self.gameBoard()
		else:
			self.message = "Bye!"
			self.gameBoard()
			self.run = False
	
	
	def gameOver(self):
		pass
	
	
	def startGame(self):
		
		self.changeWord()
		
		while self.run:
			
			self.gameBoard()
			
			
			character: str = input (self.locate.format(6,3)+"Entry one character: ").lower()
			if character in self.wordChoice or character in self.wrongs:
				self.message = "Was typed!"
				continue
			
			for i in range(self.length):
				if character == self.choice[i]:
					self.wordChoice[i] = self.choice[i]
					self.counter += 1
					self.found = True
			
			if self.counter == self.length:
				self.message = "Congratulations! You Win."
				self.gameBoard()
				self.playAgain()
			
			if not self.found:
				self.wrongs.append(character)
				self.trying -= 1
				self.message = "Wrong! now you have {} {}. Try again.".format(self.trying, "changes" if self.trying > 1 else "change")
			else:
				self.message = "You have {} {}.".format(self.trying, "changes" if self.trying > 1 else "change")
			
			if self.trying == 0:
				self.message = "You loose! The word is: {}".format(self.choice)
				self.gameBoard()
				self.playAgain()
			
			self.found = False


if __name__ == "__main__":
	guess_word = GuessWord()
	guess_word.startGame()