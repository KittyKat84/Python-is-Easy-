import random

"""
Rules:
- Rummy: a card game based on making sets.
- From a hand of 13 cards, 4 sets must be created (3 sets of 3, 1 set of 4).
- A valid set can either be a run or a book.
- One set must be a run WITHOUT using a joker.
- A run is a sequence of numbers in a row, all from the same suit.
	eg: 4 of Hearts, 5 of Hearts, and 6 of Hearts
- A book is a set in which the cards all have the same rank but have different suits.
	eg: 3 of Diamonds, 3 of Spades, 3 of Clubs
- A Joker is a card randomly picked from the deck at the start of the game.
- All Jokers are considered free cards and can be used to complete sets.
- During each player's turn, the player may take a card from the face up pile or a card from the face down deck to help create sets.
  Immediately after, the player must drop a card into the face up pile so as not go over the 13 card limit.
- When a player has created all the sets, select the close game option and drop the excess card into the face up pile.
- Card with Rank 10 is represented as Rank T
"""
Symbols = ['♠', '♢', '♡', '♣']
Suit = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
Rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
RankValue = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
SuitSymbols = {'Hearts': '♡', 'Clubs': '♣', 'Spades': '♠', 'Diamonds': '♢'}

class Card:

	def __init__(self, rank, suit):
		""" Class Constructor
		Args: Rank: A valid Rank value - a single char
			  Suit: A valid Suit value - a string
		Returns: No return value
		"""
		self.rank = rank
		self.suit = suit
		self.isjoker = False

	def __str__(self):

		if self.isjoker:
			return (self.rank + SuitSymbols[self.suit] + '-J')
		return (self.rank + SuitSymbols[self.suit])

	def is_joker(self):

		return self.isjoker

class Deck:

	def __init__(self, packs):

		self.packs = packs
		self.cards = []
		self.joker = None

		for i in range(packs):
			for s in Suit:
				for r in Rank:
					self.cards.append(Card(r, s))

	def shuffle(self):

		random.shuffle(self.cards)

	def draw_card(self):

		a = self.cards[0]
		self.cards.pop(0)
		return a

	def set_joker(self):

		self.joker = random.choice(self.cards)

		self.cards.remove(self.joker)

		for card in self.cards:
			if self.joker.rank == card.rank:
				card.isjoker = True

class Player:

	def __init__(self, name, deck, game):

		self.stash = []
		self.name = name
		self.deck = deck
		self.game = game

	def deal_card(self, card):

		try:
			self.stash.append(card)
			if len(self.stash) > 14:
				raise ValueError('ERROR: Player cannot have more than 14 cards during turn')
		except ValueError as err:
			print(err.args)

	def drop_card(self, card):

		card = get_object(self.stash, card)

		if card not in self.stash:
			return False

		self.stash.remove(card)

		self.game.add_pile(card)

		return True


	def close_game(self):

		set_array = [self.stash[:3], self.stash[3:6], self.stash[6:9], self.stash[9:]]

		count = 0
		for s in set_array:
			if is_valid_run(s):
				count += 1
		if count == 0:
			return False

		for s in set_array:
			if is_valid_run(s) == False and is_valid_book(s) == False and is_valid_run_joker(s) == False:
				return False

		return True

	def play(self):

		while True:
			print(chr(27)+"[2J")
			print("***",self.name,"your cards are:")
			print(print_cards(self.stash))
			self.game.display_pile()

			action = input("*** " + self.name + ", What would you like to do? ***, \n(M)ove Cards, (P)ick from pile, (T)ake from deck, (D)rop, (S)ort, (C)lose Game, (R)ules: ")

			if action == 'M' or action == 'm':
				move_what = input("Enter which card you want to move. \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts): ")
				move_what.strip()
				if get_object(self.stash, move_what.upper()) not in self.stash:
					input("ERROR: That card is not in your stash.  Enter to continue")
					continue

				move_where = input("Enter where you want move card to (which card the moving card will go before) Enter Space to move to end \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts):" )
				move_where.strip()
				if move_where != "" and get_object(self.stash, move_where.upper()) not in self.stash:
					input("ERROR: This is an invalid location.  Enter to continue")
					continue

				move_what = get_object(self.stash, move_what.upper())
				if move_where != "":
					move_where = get_object(self.stash, move_where.upper())
					location = self.stash.index(move_where)
					if location > self.stash.index(move_what):
						location = location - 1
					self.stash.remove(move_what)
					self.stash.insert(location, move_what)
				else:
					self.stash.remove(move_what)
					self.stash.append(move_what)

			if action == 'P' or action == 'p':
				if len(self.stash) < 14:
					c = self.game.draw_pile()
					self.stash.append(c)
				else:
					input("ERROR: You have " + str(len(self.stash)) + " cards. Cannot pick anymore. Enter to continue")

			if action == 'T' or action == 't':
				if len(self.stash) < 14:
					c = self.deck.draw_card()
					self.stash.append(c)
				else:
					input("ERROR: You have " + str(len(self.stash)) + " cards. Cannot take anymore. Enter to continue")

			if action == 'D' or action == 'd':
				if len(self.stash) == 14:
					drop = input("Which card would you like to drop? \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts): ")
					drop = drop.strip()
					drop = drop.upper()
					if self.drop_card(drop):
						return False
					else:
						input("ERROR: Not a valid card, Enter to continue")
				else:
					input("ERROR: Cannot drop a card. Player must have 13 cards total. Enter to continue")

			if action == 'S' or action == 's':
				sort_sequence(self.stash)

			if action == 'C' or action == 'c':

				if len(self.stash) == 14:
					drop = input("Which card would you like to drop? \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts): ")
					drop = drop.strip()
					drop = drop.upper()
					if self.drop_card(drop):
						if self.close_game():
							print(print_cards(self.stash))
							return True
						else:
							input("ERROR: The game is not over. Enter to Continue playing.")
							self.stash.append(self.game.draw_pile())
					else:
						input("ERROR: Not a valid card, Enter to continue")
				else:
					input("ERROR: You do not have enough cards to close the game. Enter to Continue playing.")

			if action == 'R' or action == 'r':
				print("------------------ Rules --------------------",
					"\n- Rummy: a card game based on making sets.",
					"\n- From a hand of 13 cards, 4 sets must be created (3 sets of 3, 1 set of 4).",
					"\n- The set of 4 must always be at the end"
					"\n- A valid set can either be a run or a book.",
					"\n- One set must be a run WITHOUT using a joker."
					"\n- A run is a sequence of numbers in a row, all with the same suit. ",
					"\n \tFor example: 4 of Hearts, 5 of Hearts, and 6 of Hearts",
					"\n- A book of cards must have the same rank but may have different suits.",
					"\n \tFor example: 3 of Diamonds, 3 of Spades, 3 of Clubs",
					"\n- Jokers are randomly picked from the deck at the start of the game.",
					"\n- Joker is denoted by '-J' and can be used to complete sets.",
					"\n- During each turn, the player may take a card from the face up pile or from the face down deck.",
					"Immediately after, the player must drop any one card into the face up pile so as not go over the 13 card limit.",
					"\n- When a player has created all the sets, select Close Game option and drop the excess card into the face  up pile.",
					"\n- Card with Rank 10 is represented as Rank T"
					"\n--------------------------------------------" )
				input("Enter to continue ....")

class Game:

	def __init__(self, hands, deck):

		self.pile = []
		self.players = []

		for i in range(hands):
			name = input("Enter name of Player " + str(i) + ": ")
			self.players.append(Player(name, deck, self))

	def display_pile(self):

		if len(self.pile) == 0:
			print("Empty pile.")
		else:
			print("The card at the top of the pile is: ", self.pile[0])

	def add_pile(self, card):

		self.pile.insert(0, card)

	def draw_pile(self):

		if len(self.pile) != 0:
			return self.pile.pop(0)
		else:
			return None

	def play(self):

		i = 0
		while self.players[i].play() == False:
			print(chr(27)+"[2J")
			i += 1
			if i == len(self.players):
				i = 0
			print("***", self.players[i].name, "to play now.")
			input(self.players[i].name + " hit enter to continue...")

		print("*** GAME OVER ***")
		print("*** ", self.players[i].name, " Won the game ***")

def is_valid_book(sequence):

	while(sequence[0].isjoker == True):
		sequence.append(sequence.pop(0))

	for card in sequence:
		if card.is_joker() == True:
			continue
		if card.rank != sequence[0].rank:
			return False

	return True

def is_valid_run(sequence):

	RankValue["A"] = 1
	sort_sequence(sequence)

	for card in sequence:
		if card.suit != sequence[0].suit:
			return False

	if sequence[0].rank == "A":
		if sequence[1].rank == "Q" or sequence[1].rank == "J" or sequence[1].rank == "K":
			RankValue[sequence[0].rank] = 14
			sort_sequence(sequence)

	for i in range(1,len(sequence)):
		if RankValue[sequence[i].rank] != RankValue[(sequence[i-1].rank)]+1:
			return False

	return True

def is_valid_run_joker(sequence):

	RankValue["A"] = 1
	sort_sequence(sequence)
	push_joker_toend(sequence)
	joker_count = 0
	for card in sequence:
		if card.is_joker() == True:
			joker_count += 1

	for card in sequence:
		if card.is_joker() == True:
			continue
		if card.suit != sequence[0].suit:
			return False

	if sequence[0].rank == "A":
		if sequence[1].rank == "Q" or sequence[1].rank == "J" or sequence[1].rank == "K":
			RankValue[sequence[0].rank] = 14
			sort_sequence(sequence)
			push_joker_toend(sequence)

	rank_inc = 1
	for i in range(1,len(sequence)):
		if sequence[i].is_joker() == True:
			continue
		while (RankValue[sequence[i].rank] != RankValue[(sequence[i-1].rank)]+rank_inc):
			if joker_count > 0:
				rank_inc += 1
				joker_count -= 1
				continue
			else:
				if RankValue[sequence[i].rank] != RankValue[(sequence[i-1].rank)]+1:
					return False
				else:
					break
	return True

def push_joker_toend(sequence):

	sort_sequence(sequence)
	joker_list = []
	for card in sequence:
		if card.is_joker()== True:
			sequence.remove(card)
			joker_list.append(card)
	sequence += joker_list
	return sequence

def get_object(arr, str_card):

	if len(str_card) != 2:
		return None

	for item in arr:
		if item.rank == str_card[0] and item.suit[0] == str_card[1]:
			return item

	return None

def print_cards(arr):

	s = ""
	for card in arr:
		s = s + " " + str(card)
	return s

def sort_sequence(sequence):

	is_sort_complete = False

	while is_sort_complete == False:
		is_sort_complete = True
		for i in range(0, len(sequence)-1):
			if RankValue[sequence[i].rank] > RankValue[sequence[i+1].rank]:
				a = sequence[i+1]
				sequence[i+1] = sequence[i]
				sequence[i] = a
				is_sort_complete = False
	return sequence

def unit_tests():

	print("Running Unit Tests")

	#test 1 - check players deal card exception handling

	player = Player("Karen", None, None)
	player.deal_card(Card("5", "Hearts"))
	player.deal_card(Card("6", "Hearts"))
	player.deal_card(Card("7", "Hearts"))
	player.deal_card(Card("6", "Spades"))
	player.deal_card(Card("6", "Diamonds"))
	player.deal_card(Card("6", "Clubs"))
	player.deal_card(Card("Q", "Clubs"))
	player.deal_card(Card("8", "Diamonds"))
	player.deal_card(Card("9", "Spades"))
	player.deal_card(Card("4", "Diamonds"))
	player.deal_card(Card("2", "Spades"))
	player.deal_card(Card("3", "Clubs"))
	player.deal_card(Card("2", "Hearts"))
	player.deal_card(Card("T", "Spades"))
	player.deal_card(Card("T", "Hearts"))


	#test 2 - check close game
 
	player1 = Player("Karen", None, None)
	player1.deal_card(Card("3", "Hearts"))
	player1.deal_card(Card("4", "Hearts"))
	player1.deal_card(Card("5", "Hearts"))
	player1.deal_card(Card("4", "Spades"))
	player1.deal_card(Card("4", "Diamonds"))
	player1.deal_card(Card("4", "Clubs"))
	player1.deal_card(Card("T", "Clubs"))
	player1.deal_card(Card("T", "Hearts"))
	player1.deal_card(Card("T", "Spades"))
	player1.deal_card(Card("4", "Diamonds"))
	player1.deal_card(Card("A", "Diamonds"))
	player1.deal_card(Card("2", "Diamonds"))
	player1.deal_card(Card("3", "Diamonds"))
	assert (player1.close_game() == True)


	player2 = Player("Leon", None, None)
	player2.deal_card(Card("4", "Diamonds"))
	player2.deal_card(Card("5", "Hearts"))
	player2.deal_card(Card("6", "Hearts"))
	player2.deal_card(Card("6", "Clubs"))
	player2.deal_card(Card("6", "Diamonds"))
	player2.deal_card(Card("T", "Clubs"))
	player2.deal_card(Card("J", "Clubs"))
	player2.deal_card(Card("Q", "Clubs"))
	player2.deal_card(Card("K", "Clubs"))
	player2.deal_card(Card("2", "Spades"))
	player2.deal_card(Card("3", "Hearts"))
	player2.deal_card(Card("2", "Hearts"))
	player2.deal_card(Card("2", "Spades"))
	assert (player2.close_game() == False)

	#test 3 - testing ace values
 
	player3 = Player("Tobias", None, None)
	player3.deal_card(Card("T", "Diamonds"))
	player3.deal_card(Card("9", "Diamonds"))
	player3.deal_card(Card("8", "Diamonds"))
	player3.deal_card(Card("J", "Diamonds"))
	sort_sequence(player3.stash)
	print(print_cards(player3.stash))

	#test 4 - testing joker in a book

	player4 = Player("Tenica", None, None)
	player4.deal_card(Card("2", "Spades"))
	player4.deal_card(Card("7", "Diamonds"))
	player4.deal_card(Card("7", "Clubs"))
	player4.deal_card(Card("7", "Hearts"))
	player4.stash[0].isjoker=True
	assert (is_valid_book(player4.stash) == True)

	#test 5 - testing joker in a run

	player5 = Player("Leonie", None, None)
	player5.deal_card(Card("5", "Diamonds"))
	player5.deal_card(Card("3", "Diamonds"))
	player5.deal_card(Card("9", "Hearts"))
	player5.deal_card(Card("6", "Diamonds"))
	player5.stash[0].isjoker=True
	player5.stash[2].isjoker=True
	print(print_cards(player5.stash))
	assert (is_valid_run_joker(player5.stash) == True)
	
    	#test 6 - testing is_valid_run

	player6 = Player("Nobby", None, None)
	player6.deal_card(Card("8", "Diamonds"))
	player6.deal_card(Card("J", "Diamonds"))
	player6.deal_card(Card("9", "Diamonds"))
	player6.deal_card(Card("T", "Diamonds"))
	print(print_cards(player6.stash))
	assert (is_valid_run(player6.stash) == True)

	#test 7 - testing push_joker_toend function

	player7 = Player("Clara", None, None)
	player7.deal_card(Card("4", "Spades"))
	player7.deal_card(Card("9", "Diamonds"))
	player7.deal_card(Card("T", "Hearts"))
	player7.deal_card(Card("Q", "Diamonds"))
	player7.stash[0].isjoker=True
	player7.stash[2].isjoker=True
	print(print_cards(player7.stash))
	push_joker_toend(player7.stash)
	print(print_cards(player7.stash))

def main():

	deck = Deck(2)
	deck.shuffle()
	g = Game(2, deck)

	for i in range(13):
		for hand in g.players:
			card = deck.draw_card()
			hand.deal_card(card)

	first_card = deck.draw_card()
	g.add_pile(first_card)
	g.play()

if __name__ == "__main__":
    main()
