import pygame
import random
from random import shuffle

from src.Game import Game
from src.Config import Config

def main():
    display = pygame.display.set_mode((Config['game']['width'], Config['game']['width']))
    pygame.display.set_caption(Config['game']['caption'])

    game = Game(display)
    game.initialize_pygame()
    game.loop()

if __name__ == '__main__':
    main()