from src.Card2 import *
from random import randint

class Deck:
  cards = []
  suits = ["spades", "hearts", "clubs", "diamonds"]
  ranks = ["2","3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  rank_val = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  trump_suit = ""

  for i in range(4):
    for j in range(13):
      card = Card2(ranks[j], suits[i], rank_val[j])
      cards.append(card)

  def display(self):
    for i in range(52):
      print(self.cards[i].name)

  def shuffle(self):
    for i in range(100):
      rand = randint(0, 51)
      rand2 = randint(0, 51)
      temp = self.cards[rand]
      self.cards[rand] = self.cards[rand2]
      self.cards[rand2] = temp