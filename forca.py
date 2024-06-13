import random

wordList = ["girl", "children", "horse", "knife", "house", "elevator", "marshmallow", "table", "window", "script", "rainbow", "stone", "strong", "grandma", "grandpa", "glasses", "dinosaur", "pink"]


choice = random.choice(wordList)

trying = 5
counter = 0
found = 0
word = []
wrong = []
run = True

length = len(choice)
word = ["_"] * length

while run:
    
    print (" ".join(word))
    character = input ("Type one letter: ")

    for i in range(length):
    	if character == choice[i]:
    		word[i] = choice[i]
    		counter += 1
    		found = 1

    if found == 0:
    	wrong.append(character)
    	trying -= 1
    	print ("You wrong, have {} change. Try again.".format(trying))
    
    if trying == 0:
    	print ("You loose. Game over.")
    	print ("The word is {}".format(choice))
    	run = False
    	break
    
    if counter == length:
    	print (" ".join(word))
    	print ("Congratulations! You win.")
    	run = False
    	break
    
    print ("Wrong letters: {}".format("-".join(wrong)))
    print ("You have {} change!".format(trying))
    found = 0

