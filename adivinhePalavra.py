import random


class WordList:
	
	# words: list = ["girl", "children", "horse", "knife", "house", "elevator", "marshmallow", "table", "window", "script", "rainbow", "stone", "strong", "grandma", "glasses", "dinosaur", "pink", "banana", "apple", "orange", "chicken", "dog","cat", "eagle", "crocodile", "laze", "laundry", "gate", "world", "car", "truck", "mother"]
	words: list = ["garota","criança","janela","cavalo","faca","casa","elevador","mesa","carta","rocha","poder","vovó","óculos","dinossauro","rosa","vermelho","azul","verde","amarelo","laranja","galinha","cachorro","gato","águia","jacaré","preguiça","máquina","lavadoura","porta","mundo","carro","ônibus","mamãe","papai","menina","menino","planeta"]

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
		
		self.message: str = "Você tem {} {}.".format(self.trying, "chances" if self.trying > 1 else "chance")
		
		self.clearScreen: str = "\033[2J"
		self.locate = str = "\033[{};{}H"
	
	
	def gameBoard(self):
		print (self.clearScreen)
		print (self.locate.format(1,12)+"ADIVINHE A PALAVRA")
		print (self.locate.format(4,3)+"Palavra: {}".format(" ".join(self.wordChoice)))
		print (self.locate.format(4,33)+"Errou: {}".format("-".join(self.wrongs)))
		print (self.locate.format(10,3)+"Mensagem: {}".format(self.message))
	
	
	def changeWord(self):
		self.choice: str = random.choice(WordList.words)
		self.length: int = len(self.choice)
		self.wordChoice: list = ["_"] * self.length
	
	
	def playAgain(self):
		playAgain: str = input(self.locate.format(6,3)+"Jogar novamente (s/n)? ")
		if playAgain.lower() in ["sim", "s", "quero", "ok"]:
			self.trying = 5
			self.counter = 0
			self.wrongs = []
			self.message = "Você tem {} {}.".format(self.trying, "chances" if self.trying > 1 else "chance")
			self.changeWord()
			self.gameBoard()
		else:
			self.message = "Tchau!"
			self.gameBoard()
			self.run = False
	
	
	def gameOver(self):
		pass
	
	
	def startGame(self):
		
		self.changeWord()
		
		while self.run:
			
			self.gameBoard()
			
			
			character: str = input (self.locate.format(6,3)+"Digite uma letra: ").lower()[0]
			if character in self.wordChoice or character in self.wrongs:
				self.message = "Já foi digitada!"
				continue
			
			for i in range(self.length):
				if character == self.choice[i]:
					self.wordChoice[i] = self.choice[i]
					self.counter += 1
					self.found = True
			
			if self.counter == self.length:
				self.message = "Parabéns! Você Venceu."
				self.gameBoard()
				self.playAgain()
			
			if not self.found:
				self.wrongs.append(character)
				self.trying -= 1
				self.message = "Errou! Você tem {} {}. Tente de novo.".format(self.trying, "chances" if self.trying > 1 else "chance")
			else:
				self.message = "Você tem {} {}.".format(self.trying, "chances" if self.trying > 1 else "chance")
			
			if self.trying == 0:
				self.message = "Você perdeu! A palavra é: {}".format(self.choice)
				self.gameBoard()
				self.playAgain()
			
			self.found = False


if __name__ == "__main__":
	guess_word = GuessWord()
	guess_word.startGame()