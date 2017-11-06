import random

def shuffle_deck(deck):
    '''
    (list of str)->None
    '''
    for i in range(6):
    	print("\n")

    print("Shuffling the deck...")
    random.shuffle(deck)
    print("\n\n\n\n\n\n")


def create_deck():
	deck = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
	deck *= 4

	for i in range(len(deck)):
		if i < 13:
			deck[i] += " D"
		elif i < 26:
			deck[i] += " S"
		elif i < 39:
			deck[i] += " H"
		elif i < 52:
			deck[i] += " C"

	deck *= 4

	shuffle_deck(deck)
	return deck

def adjust_values(a):
	if "K" in a:
		return 10
	elif "Q" in a:
		return 10
	elif "J" in a:
		return 10    
	elif "A" in a:
		return 11 
	elif "10" in a:
		return 10  
	else:
		return int(a[0])


def play_game():
	game = "deal"
	deck = create_deck()
	i = 0

	while game.strip().lower() == "deal":
		if i > len(deck):
			shuffle_deck()


		a = adjust_values(deck[i])
		b = adjust_values(deck[i+2])
		c = adjust_values(deck[i+1])
		d = adjust_values(deck[i+3])

		cardsUsed = 4

		totalPlayer = a+b
		totalDealer = c+d

		acesPlayer = 0
		acesDealer = 0

		if a == 11:
			acesPlayer += 1

		if b == 11:
			acesPlayer += 1

		if c == 11:
			acesDealer += 1

		if d == 11:
			acesDealer += 1
			print("\n\n\n\n\n\n")

		if totalPlayer == 21:
			print("You have obtained "+str(deck[i])+" and "+str(deck[i+2])+". Blackjack!")
		else:

			print("You have obtained "+str(deck[i])+" and "+str(deck[i+2])+".")
			if acesPlayer > 0:
				print("Your total is "+str(totalPlayer)+" or "+str(totalPlayer-10)+".")
			else:
				print("Your total is "+str(totalPlayer)+".")

			print()
			print("The dealer has obtained "+str(deck[i+1])+" and an unknown card")
			print("\n\n")
			if totalDealer == 21:
				print("The dealer has obtained "+str(deck[i+1])+" and "+str(deck[i+3]+". Dealer has a blackjack! You lose!"))
				action = "over"
			else:
				action = input("Would you like to hit or stand? ")

			while action == "hit":
				temp = adjust_values(deck[i+cardsUsed])
				totalPlayer += temp
				print("You have obtained "+str(deck[i+cardsUsed])+".")
				cardsUsed += 1
				print()
				if temp == 11:
					acesPlayer += 1

				if totalPlayer > 21 and acesPlayer > 0:
					totalPlayer -= 10
					acesPlayer -= 1
					print("Your new total is "+str(totalPlayer)+".")
					action = input("\nWould you like to hit or stand? ")

				elif totalPlayer > 21:
					print("Your new total is "+str(totalPlayer)+".")
					print("\nYou busted!\n")
					action = "over"

				elif totalPlayer < 21 and acesPlayer > 0:
					print("Your new total is "+str(totalPlayer)+" or "+str(totalPlayer-10)+".")
					action = input("\nWould you like to hit or stand? ")

				elif totalPlayer == 21:
					print("Your new total is "+str(totalPlayer)+".")
					action = "stand"
				else:
					print("Your new total is "+str(totalPlayer)+".")
					action = input("\nWould you like to hit or stand? ")


			if action.strip().lower() == "stand":
				print("The dealer has "+str(deck[i+1])+" and "+str(deck[i+3])+".")
				if totalDealer > 21 and acesDealer > 0:
						totalDealer -= 10
						acesDealer -= 1
						x
				while totalDealer < 17:
					temp = adjust_values(deck[i+cardsUsed])
					totalDealer += temp

					if temp == 11:
						acesDealer += 1

					if totalDealer > 21 and acesDealer > 0:
						totalDealer -= 10
						acesDealer -= 1

					print("The dealer obtained "+str(deck[i+cardsUsed])+" and his new total is "+str(totalDealer))
					cardsUsed += 1

				print("The dealer has obtained "+str(totalDealer))
				print("You have obtained "+str(totalPlayer))

				if totalDealer > 21 or totalPlayer > totalDealer:
					print("\nYou win!\n")
				elif totalPlayer == totalDealer:
					print("\nYou push!\n")
				else:
					print("\nYou lose.\n")
			if action == "over":
				print()
				pass
		i+=cardsUsed
		game = input("\nType 'deal' if you would like to play again ")
	
