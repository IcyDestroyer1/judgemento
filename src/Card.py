
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
from ActualGame import *
from pygame import display
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Card(object):
    def __init__(self):
        self.image_path = 'English_pattern_playing_cards_deck.svg.png'
        self.origin1 = (0,0)
        self.origin2 = (0,70)
        self.seperation = 20
        self.img = pygame.image.load(self.image_path)
        self.width = self.img.get_width()/ 12
        self.height = self.img.get_height() / 4
        self.suite_index = 3
        self.card_index = 2
        self.source_area = pygame.Rect((self.card_index * 61, self.suite_index * 90), (self.width, self.height))

    def half_card(self):
        self.image_path = 'English_pattern_playing_cards_deck.svg.png'
        self.origin1 = (0,0)
        self.origin2 = (0,70)
        self.separation = 20
        # Load the image
        self.img = pygame.image.load(self.image_path)

        self.width = self.img.get_width()/ 12
        self.height = self.img.get_height()/ 4
        # this code will split out cards and stuff
    def split_card(self, card_index, suite_index):
        import pdb; pdb.set_trace()
        self.source_area = pygame.Rect((self.card_index * 61, self.suite_index * 90), (self.width, self.height))
        return self.source_area

    def display_card(self, source_area, card_position):
        #pygame.display.blit(img, card_position, source_area)
        import pdb; pdb.set_trace()
        pygame.display.flip(self.img, card_position, source_area)

    def print_hand(self, Card, player1):
        pass

'''
pygame.init()

 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Judgemento | V.1")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
'''
'''
my_card = Card()
card_1 = my_card.split_card(0, 0)
my_card.display_card(card_1, (0,0))
'''