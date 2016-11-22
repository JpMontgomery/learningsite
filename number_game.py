import random
def game():
	guesses = []
	x = random.randint(1,10)
	while len(guesses) < 5:
		try:
			y = int(input('Guess a number between 1 and 10: \n'))
		except ValueError:
			print('{} is not a number!'.format(y))
		else:
			if y == x:
				print('You got it! My secret number was {}.'.format(x))
				break
			else:
				print("That's not it!")
				if y < x:
					print('Too low!')
				else:
					print('Too high!')
				guesses.append(y)

	else:
		print('You lose! My number was {}.'.format(x))
	playagain = int(input('Would you like to play again? 1 for yes, 0 for no\n'))
	if playagain == 1:
		game()
	else:
		print('Bye!')
game()