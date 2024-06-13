import random


class WordList:
	
	words: dict = {"english": ["girl", "children", "horse", "knife", "house", "elevator", "marshmallow", "table", "window", "script", "rainbow", "stone", "strong", "grandma", "glasses", "dinosaur", "pink", "banana", "apple", "orange", "chicken", "dog", "cat", "eagle", "crocodile", "laze", "laundry", "gate", "world", "car", "truck", "mother"],
				   "portuguese": ["garota", "menino", "cavalo", "adaga", "apartamento", "elevador", "guloseima", "departamento", "janela", "carta", "fantasia", "rocha", "poder", "parente", "luneta", "dinossauro", "rosa", "banana", "pera", "laranja", "galinha", "cachorro", "gato", "coruja", "crocodilo", "lento", "lavagem", "porta", "mundo", "carro", "companheira"]}
	
	messages: dict = {"english": {"change": "You have {} {}.",
								  "choice": ["changes", "change"],
								  "titles": ["  GUESS THE WORD  ", "Word: ", "Wrongs: ", "Message: "],
								  "try_question": "Play again (y/n)? ",
								  "try_answer": ["yes", "y", "ok"],
								  "bye": "Bye!",
								  "entry": "Entry one character: ",
								  "typed": "Was typed!",
								  "win": "Congratulations! You Win.",
								  "wrong": "Wrong! now you have {} {}. Try again.",
								  "loose": "You loose! The word is: {}"},
					  "portuguese": {"change": "Você tem {} {}.",
					  			   "choice": ["chances", "chance"],
					  			   "titles": ["  ACHE A PALAVRA  ", "Palavra: ", "Erros: ", "Mensagem: "],
					  			   "try_question": "Jogar novamente (s/n)? ",
					  			   "try_answer": ["sim", "s", "vamos", "ok"],
					  			   "bye": "Tchau!",
					  			   "entry": "Digite uma letra: ",
					  			   "typed": "Já foi digitada!",
					  			   "win": "Parabéns, Você Venceu.",
					  			   "wrong": "Errado! Agora você tem {} {}.",
					  			   "loose": "Você perdeu! a palavra é: {}"}}
		
	
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
		
		self.choice: str = ""
		self.length: int = 0
		self.wordChoice: list = []
		self.wrongs: list = []
		
		self.language: str = "english"
		self.message: str = WordList.messages[self.language]["change"].format(self.trying, WordList.messages[self.language]["choice"][0] if self.trying > 1 else WordList.messages[self.language]["choice"][-1])
		
		self.clearScreen: str = "\033[2J"
		self.locate = str = "\033[{};{}H"
	
	
	def gameBoard(self):
		print (self.clearScreen)
		print (self.locate.format(1,1)+WordList.colorBright.format(WordList.foregroundColors["green"])+"=================["+WordList.messages[self.language]["titles"][0]+"]=================="+WordList.colorReset)
		print (self.locate.format(4,3)+WordList.messages[self.language]["titles"][1]+WordList.colorBright.format(WordList.foregroundColors["yellow"])+"{}".format(" ".join(self.wordChoice))+WordList.colorReset)
		print (self.locate.format(4,36)+WordList.messages[self.language]["titles"][2]+WordList.colorDimmed.format(WordList.foregroundColors["red"])+"{}".format("-".join(self.wrongs))+WordList.colorReset)
		print (self.locate.format(10,3)+WordList.messages[self.language]["titles"][3]+WordList.colorDimmed.format(WordList.foregroundColors["red"])+"{}".format(self.message)+WordList.colorReset)
		print (self.locate.format(12,1)+WordList.colorBright.format(WordList.foregroundColors["green"])+"======================================================="+WordList.colorReset)
	
	
	def changeWord(self):
		self.choice: str = random.choice(WordList.words[self.language])
		self.length: int = len(self.choice)
		self.wordChoice: list = ["_"] * self.length
	
	
	def playAgain(self):
		playAgain: str = input(self.locate.format(6,3)+WordList.messages[self.language]["try_question"])
		if playAgain.lower() in WordList.messages[self.language]["try_answer"]:
			self.trying = 5
			self.counter = 0
			self.wrongs = []
			self.message = WordList.messages[self.language]["change"].format(self.trying, WordList.messages[self.language]["choice"][0] if self.trying > 1 else WordList.messages[self.language]["choice"][-1])
			self.changeWord()
			self.gameBoard()
		else:
			self.message = WordList.messages[self.language]["bye"]
			self.gameBoard()
			self.run = False
	
	
	def gameOver(self):
		pass
	
	
	def startGame(self):
		
		print(self.clearScreen)
		
		select: str = ""
		
		while select not in ["1", "2"]:
			select: str = input("(1) English  (2) Portuguese: ")
			select = select.lower().lstrip().rstrip()
			if select in ["1", "us", "uk", "en", "english", "inglês"]:
				select = "1"
				self.language = "english"
			elif select in ["2", "br", "po" "pt", "portuguese", "português"]:
				select ="2"
				self.language = "portuguese"
		
		self.changeWord()
		
		while self.run:
			
			self.gameBoard()
			
			
			character: str = input (self.locate.format(6,3)+WordList.messages[self.language]["entry"]).lower()
			if not character:
				continue
			if character in self.wordChoice or character in self.wrongs:
				self.message = WordList.messages[self.language]["typed"]
				continue
			
			for i in range(self.length):
				if character == self.choice[i]:
					self.wordChoice[i] = self.choice[i]
					self.counter += 1
					self.found = True
			
			if self.counter == self.length:
				self.message = WordList.messages[self.language]["win"]
				self.gameBoard()
				self.playAgain()
			
			if not self.found:
				self.wrongs.append(character)
				self.trying -= 1
				self.message = WordList.messages[self.language]["wrong"].format(self.trying, WordList.messages[self.language]["choice"][0] if self.trying > 1 else WordList.messages[self.language]["choice"][-1])
			else:
				self.message = WordList.messages[self.language]["change"].format(self.trying, WordList.messages[self.language]["choice"][0] if self.trying > 1 else WordList.messages[self.language]["choice"][-1])
			
			if self.trying == 0:
				self.message = WordList.messages[self.language]["loose"].format(self.choice)
				self.gameBoard()
				self.playAgain()
			
			self.found = False


if __name__ == "__main__":
	guess = GuessWord()
	guess.startGame()