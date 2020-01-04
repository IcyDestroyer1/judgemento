import random
import time
from src.Card2 import *
from src.Deck import *
def ActualGame():
  p1_score=0
  p2_score=0
  p3_score=0
  p4_score=0
  rounds = 13

  def display(player): 
    for i in range(len(player)):
      print(player[i].name)

  Players = int(input("How many players do you want to play with?"))
  print ("Okay, we will play with " + str(Players) + " players.")

  for i in range(13):
    p1_sets_made=0
    p2_sets_made=0
    p3_sets_made=0
    p4_sets_made=0
    
    deck = Deck()
    deck.shuffle()
    
    # Check if total number of players playing is 3.
    if int(Players) == 3:
      
      
      # Split deck into 3 seperate players.
      player1 = deck.cards[0:rounds] 
      player2 = deck.cards[rounds:(rounds*2)] 
      player3 = deck.cards[(rounds * 2):(rounds * 3)]
      # Check if total number of players playing is 4.


    elif int(Players) == 4:
      # Split deck into 4 seperate players.
      player1 = deck.cards[0:rounds]
      player2 = deck.cards[rounds:(rounds * 2)]
      player3 = deck.cards[(rounds * 2):(rounds * 3)]
      player4 = deck.cards[(rounds * 3):(rounds * 4)]


    if Players == 3:
      trump = ['spades','hearts','clubs','diamonds']
      deck.trump_suit = trump[i%4]
      print("The trump suit is " + deck.trump_suit + ".")


      print("everyone except player 1 look away, you have 5 seconds")
      time.sleep(5)
      print('Player 1, this is your hand.') 
      display(player1)
      player1_sets_called = int(input("how many sets are you going to make?\n>"))#implement click event thing
      for i in range(50):
        print(" ")

      
      print("everyone except player 2 look away, you have 5 seconds")
      print("player 1 called " + str(player1_sets_called) + ". How many will you make?")
      time.sleep(5)
      print('Player 2, this is your hand.') 
      display(player2)
      player2_sets_called = int(input("how many sets are you going to make?\n>"))#implement click event thing
      for i in range(50):
        print(" ")



      print("everyone except player 3 look away, you have 5 seconds")
      print("player 1 called " + str(player1_sets_called) + ".")
      print("player 2 called " + str(player2_sets_called) + ". How many will you make?")
      time.sleep(5)
      print('Player 3, this is your hand.') 
      display(player3)
      player3_sets_called = int(input("how many sets are you going to make?\n>"))#implement click event thing
      for i in range(50):
        print(" ")


      print(" everyone look away while player 1 plays his card, ")
      time.sleep(3)
      print('Player 1, this is your hand.') 
      display(player1)
      player1_play_card = input("what card do you want to play?")
      if player1_play_card in player1:
        print("\n" * 50)
        print(player1_play_card)
        time.sleep(3)
      

      print(" everyone look away while player 2 plays his card, ")
      time.sleep(3)
      print('Player 1 played ' + str(player1_play_card) + ".")
      print('Player 2, this is your hand.') 
      
      display(player2)
      player2_play_card = input("what card do you want to play?")
      if player2_play_card in player2:
        print("\n" * 50)
        print(player2_play_card)
        time.sleep(3)

      print(" everyone look away while player 3 plays his card, ")
      time.sleep(3)
      print('Player 1 played ' + str(player1_play_card) + ".")
      print('Player 2 played ' + str(player2_play_card) + ".")
      print('Player 3, this is your hand.') 
      
      display(player3)
      player3_play_card = input("what card do you want to play?")
      if player3_play_card in player3:
        print("\n" * 50)
        print(player3_play_card)
        time.sleep(3)


    
      rounds = rounds - 1
      #sets called compare to sets made
