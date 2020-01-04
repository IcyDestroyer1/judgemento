class Card2:
  def __init__(self, rank, suit, val):
    self.rank = rank
    self.suit = suit
    self.val = val
    self.trump_val = 0
    self.name = rank + " of " + suit