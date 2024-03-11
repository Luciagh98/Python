import random
suits = ('Corazones', 'Diamantes', 'Spades', 'Clubs')
ranks = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve',
'Diez', 'J', 'Q', 'K', 'As')
values = {'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 'Siete': 7,
'Ocho': 8, 'Nueve': 9, 'Diez': 10, 'J': 10, 'Q': 10, 'K': 10, 'As': 11}

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
  def __str__(self):
    return self.rank + ' de ' + self.suit
  
class Deck:
    def __init__(self):
      self.deck = []
      for suit in suits:
        for rank in ranks:
          self.deck.append(Card(suit,rank))
    def __str__(self):
      deck_comp = ''
      for card in self.deck:
        deck_comp += '\n'+card.__str__()
      return 'El deck tiene:' + deck_comp
    
    def shuffle(self):
      random.shuffle(self.deck)

    def deal(self):
      single_card = self.deck.pop()
      return single_card
    
class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def add_card(self, card):
    self.cards.append(card)
    self.value += values[card.rank]
    if card.rank == 'As':
      self.aces += 1

  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

class Chips:
  def __init__(self):
    self.total = 100
    self.bet = 0
  def win_bet(self):
    self.total += self.bet
  def lose_bet(self):
    self.total -= self.bet

def take_bet(chips):
  while True:
      try:
        chips.bet = int(input('Cuantas fichas querrías apostar?: '))
      except ValueError:
        print('Disculpe, exprese el valor en números enteros')
      else:
        if chips.bet > chips.total:
          print('Disculpe, no dispone de ese número de fichas, sus fichas suman: ', chips.total)
        else:
          return chips
        
def hit(deck, hand):
  hand.add_card(deck.deal())

def hit_or_stand(deck, hand, playing):
    while playing:
        x = input("¿Quiere otra carta?(S/N): ")
        if x[0].lower() == 's':
            hit(deck, hand)
            show_some(player_hand, dealer_hand)
            return True
        elif x[0].lower() == 'n':
            print("No va más. Juega el Dealer.")
            return False
        else:
            print('Seleccione una opción correcta.')
            return True

def show_some(player, dealer):
  print("\nMano del Dealer:")
  print(" <card_hidden>:")
  print('', dealer.cards[1])
  print("\nMano del Jugador:", *player.cards, sep = '\n')

def show_all(player, dealer):
  print("\nMano del Dealer:", *dealer.cards, sep = '\n')
  print("Mano del Dealer= ", dealer.value)
  print("\nMano del Jugador:", *player.cards, sep = '\n')
  print("Mano del Jugador= ", player.value)

def player_busts(chips):
  print("El Jugador Pierde!")
  chips.lose_bet()

def player_wins(chips):
  print("El Jugador Gana!")
  chips.win_bet()

def dealer_busts(chips):
  print("El Dealer Pierde!")
  chips.win_bet()

def dealer_wins(chips):
  print("El Dealer Gana!")
  chips.lose_bet()

def push():
  print("Es un Empate!")

player_chips = Chips()

while True:
  playing = True
  print("Bienvenido a BlackJack!")
  deck = Deck()
  deck.shuffle()

  player_hand = Hand()
  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())

  dealer_hand = Hand()
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

  take_bet(player_chips)

  show_some(player_hand, dealer_hand)

  while playing:
    playing = hit_or_stand(deck, player_hand, playing)
    if player_hand.value > 21:
      if player_hand.aces != 0:
          player_hand.adjust_for_ace()
      else:
          playing = False

  if player_hand.value <= 21:
      while dealer_hand.value < 17:
          hit(deck, dealer_hand)

  show_all(player_hand, dealer_hand)

  if dealer_hand.value > 21:
    dealer_busts(player_chips)
  elif player_hand.value > 21:
    player_busts(player_chips)
  elif dealer_hand.value > player_hand.value:
    dealer_wins(player_chips)
  elif player_hand.value > dealer_hand.value:
    player_wins(player_chips)
  else:
    push()

  print("\nLa cantidad de fichas del jugador es de: ", player_chips.total)

  new_game = input("Quieres jugar otra partida?(S/N): ")

  if new_game[0].lower() == 's':
    playing=True
    continue
  else:
    print('Gracias por jugar!!')
    break