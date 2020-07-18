import random as random

class Deck:
    def __init__(self):
        self.deck = []
        for suit in ['Diamonds', 'Clubs', 'Hearts', 'Spades']:
            for value in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
                self.deck.append([value, suit])


    def get_deck(self):
        return self.deck

    def pick_random_card(self):
        choice = random.choice(self.deck)
        self.deck.remove(choice)
        return choice

class Table:
    def __init__(self, n_players):
        self.n_players = n_players
        self.players_left = n_players
        self.players = {}
        self.current_buttons = {}
        self.community_cards = []
        for player in range(self.n_players):
            playerdict = {
                'playerid': player,
                'wallet': 100,
                'hand': []
            }
            self.players[player] = playerdict
            # self.players.append(playerdict)

        buttons = ['dealer', 'small blind', 'big blind'] # Place dealer and blind buttons
        number = 0
        last_number = self.n_players
        for button in buttons:
            self.current_buttons[button] = number
            number += 1
            if number == last_number:
                number = 0

    # Getters
    def get_players(self):
        return self.players
    def get_buttons(self):
        return self.current_buttons
    def get_community_cards(self):
        return self.community_cards


    # Table actions
    def move_buttons(self):
        for button in self.current_buttons:
            self.current_buttons[button] += 1
            if self.current_buttons[button] == self.players_left:
                self.current_buttons[button] = 0
        return "Buttons have been moved"
    def remove_bankrupt_players(self):
        removed_players = []
        for player in self.players:
            if self.players[player].wallet <= 0:
                self.players[player].pop()
                removed_players.append(player)
        return "Removed bankrupt players: " + removed_players
    def deal_cards(self, deckofcards): # deckofcards should be an instance of the class Deck.
        for player in self.players:
            card1 = deckofcards.pick_random_card()
            card2 = deckofcards.pick_random_card()
            self.players[player]['hand'].append(card1)
            self.players[player]['hand'].append(card2)
    def deal_flop(self, deckofcards):
        deckofcards.pick_random_card() # Burn card
        for _ in range(3):
            self.community_cards.append(deckofcards.pick_random_card())
    def deal_river_turn(self, deckofcards):
        deckofcards.pick_random_card() # Burn card
        self.community_cards.append(deckofcards.pick_random_card())


card = [10, 'Spades']

hand0 = [
    [10, 'Spades'],
    [9, 'Spades'],
    [7, 'Spades'],
    [5, 'Spades'],
    [2, 'Spades']
]
hand4 = [
    [5, 'Spades'],
    [5, 'Diamonds'],
    [7, 'Spades'],
    [5, 'Spades'],
    [5, 'Spades']
]
hand5 = [
    [10, 'Spades'],
    [7, 'Diamonds'],
    [7, 'Spades'],
    [7, 'Spades'],
    [6, 'Spades']
]
hand1 = ['8S', 'AC', '8C', '9S', '10D']
hand2 = ['8S', 'AS', '7S', '9S', '10S']

# def pair_check(hand): # Checks if there are a 4, 3 or 2 of a kind.

def is_flush(hand):
    # print(hand[0][-1])
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return True
    else:
        return False

def is_straight(hand):
    sorted_hand = sorted(hand)
    if sorted_hand[0][0] + 4 == sorted_hand[1][0] + 3 == sorted_hand[2][0] + 2 == sorted_hand[3][0] + 1 == sorted_hand[4][0]:
        return True
    else:
        return False

def is_royal(hand):
    if sorted(hand)[0][0] == 10:
        return True
    else:
        return False

def is_4_of_a_kind(hand):
    sorted_hand = sorted(hand)
    if sorted_hand[0][0] == sorted_hand[1][0] == sorted_hand[2][0] == sorted_hand[3][0] or sorted_hand[1][0] == sorted_hand[2][0] == sorted_hand[3][0] == sorted_hand[4][0]:
        return True
    else:
        return False

def is_3_of_a_kind(hand):
    sorted_hand = sorted(hand)
    if sorted_hand[0][0] == sorted_hand[1][0] == sorted_hand[2][0] or sorted_hand[1][0] == sorted_hand[2][0] == sorted_hand[3][0] or sorted_hand[2][0] == sorted_hand[3][0] == sorted_hand[4][0]:
        return True
    else:
        return False

print(is_4_of_a_kind(hand4))
print(is_4_of_a_kind(hand0))

# print(hand0)
# print(sorted(hand5))
# print(hand5)


# print(is_straight(hand0))
# print(is_straight(hand5))


#
# t = Table(4)
#
# d = Deck()
#
# print(t.get_players())
#
# print(len(d.get_deck()))
#
# t.deal_cards(d)
#
# print(t.get_players())
#
# t.deal_flop(d)
# t.deal_river_turn(d)
# t.deal_river_turn(d)
#
# print(t.get_community_cards())
#
# print(len(d.get_deck()))
#
# print(t.get_players())
