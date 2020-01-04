from src.Card import *
import pygame

from pygame import display
from src.spritesheet import *
from src.Config import Config

class Game:
    def __init__(self, display):
        self.display = display
    
    def get_card_image(self,sprite_sheet,card):
        width = 70
        margin = 5
        x = 6
        y = 4
        if card.rank == "2":
            x = 83
        elif card.rank == "3":
            x = 159
        elif card.rank == "4":
            x = 235
        elif card.rank == "5":
            x = 311
        elif card.rank == "6":
            x = 388
        elif card.rank == "7":
            x = 464
        elif card.rank == "8":
            x = 541
        elif card.rank == "9":
            x = 617
        elif card.rank == "10":
            x = 694
        elif card.rank == "Jack":
            x = 770
        elif card.rank == "Queen":
            x = 847
        elif card.rank == "King":
            x = 923

        if card.suit == "hearts":
            y = 117
        elif card.suit == "diamonds":
            y = 229
        elif card.suit == "clubs":
            y = 341
        '''
        if card.suit == "hearts":
            y = 120
        
        elif card.suit == "clubs":
            y = 230
        '''
        """
        image = sprite_sheet.get_image(x[str(card.rank)],y[str(card.suit)],width,109.2)
        return image
        """
        image = sprite_sheet.get_image(x,y,width,109.2)
        return image
        
    def old_loop(self):
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                print(event)
            #my_card_position = (10,20)
            #mycard = Card()
            #half_card() #ERROR (display)
            #mycard.display_card(my_card_position)
            pygame.display.update()

        clock.tick(Config['game']['fps'])

    def display_hand(self, player):

        x = 0
        for card in player:
            image = self.get_card_image(self.sprite_sheet,card)
            self.screen.blit(image,(x,0))
            x +=25

    def trump_suit(self, trump_suit):
        if trump_suit == "spades":
            x = 600
            card = Card2("Ace","spades",14)
            image = self.get_card_image(self.sprite_sheet,card)
            self.screen.blit(image,(x,0))
            #display ace of spades
        elif trump_suit == "hearts":
            pass
            #display ace of hearts
        elif trump_suit == "clubs":
            pass
            #display ace of clubs
        elif trump_suit == "diamonds":
            pass
            #display ace of diamonds
    def loop(self):
        current_player = 0
        deck = Deck()
        deck.shuffle()
        # Hard code to 3 players for now (we will add more players soon)
        # Split deck into 3 seperate players.
        rounds = 13
        players = []

        player1 = deck.cards[0:rounds]
        players.append(player1) 
        player2 = deck.cards[rounds:(rounds*2)]
        players.append(player2)
        player3 = deck.cards[(rounds * 2):(rounds * 3)]
        players.append(player3)
        
        

        player_num = 0

        current_player = player1

        trump = ['spades','hearts','clubs','diamonds']
        deck.trump_suit = trump[0]#replace 0 with i%4
        
        
        font = pygame.font.SysFont("TimeNewRoman", 40)
    
        # Check if total number of players playing is 4.

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
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] >= 448 and mouse[1] >= 89:
                        if mouse[0] <= 546 and mouse[1] <= 139:
                            player_num += 1
                            if player_num >= len(players):
                                player_num = 0
                            current_player = players[player_num]

            #print(event)
        
            # --- Game logic should go here
            # --- Screen-clearing code goes here
        
            # Here, we clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
        
            # If you want a background image, replace this clear with blit'ing the
            # background image.
            self.screen.fill(RED)
        
            # --- Drawing code should go here
            self.display_hand(current_player)

            self.trump_suit(deck.trump_suit)
            '''
            x = 0
            for card in player2:
                image = self.get_card_image(sprite_sheet,card)
                self.screen.blit(image,(x,115))
                x +=25
            x = 0
            for card in player3:
                image = self.get_card_image(sprite_sheet,card)
                self.screen.blit(image,(x,225))
                x +=25
            '''
            menuAtivo = True;
                
            def draw_sets(self):
                # draw button
                switch_button = pygame.draw.rect(self.screen,(0, 0, 255),(450,90,100,50));
                text = font.render("Next", True, WHITE)
                self.screen.blit(text, (500 - text.get_width() // 2, 110 - text.get_height() // 3))

                # pygame.display.flip();
                
                # sets how many? button
                switch_button = pygame.draw.rect(self.screen,(0, 120, 120),(450,150,240,50));
                text = font.render("How many sets?", True, WHITE)
                self.screen.blit(text, (570 - text.get_width() // 2, 170 - text.get_height() // 3))

                # pygame.display.flip();

                # + button
                switch_button = pygame.draw.rect(self.screen,(0, 240, 0),(450,200,50,50));
                text = font.render("+", True, WHITE)
                self.screen.blit(text, (475 - text.get_width() // 2, 220 - text.get_height() // 3))

                # pygame.display.flip();

                # - button
                switch_button = pygame.draw.rect(self.screen,(0, 240, 0),(640,200,50,50));
                text = font.render("-", True, WHITE)
                self.screen.blit(text, (665 - text.get_width() // 2, 220 - text.get_height() // 3))

                pygame.display.flip();

                numofplayer1_sets = 0
                
                # number of sets button
                switch_button = pygame.draw.rect(self.screen,(0, 240, 0),(546,200,50,50));
                text = font.render(str(numofplayer1_sets), True, WHITE)
                self.screen.blit(text, (570 - text.get_width() // 2, 220 - text.get_height() // 3))

                pygame.display.flip();
            draw_sets(self)    
            
            # while menuAtivo:
            #     mouse = pygame.mouse.get_pos()
            #     click = pygame.mouse.get_pressed()
            #     for evento in pygame.event.get():
            #         print(evento);
            #         if click[0] == 1:
                        
            #             if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
            #                 # This is the event line if you click it:
                        
            #                 # for now just go to player 2
            #                 print("hi")
            #                 current_player = player2
            #                 #pygame.quit();

            #             if mouse[0] >= 448 and mouse[1] >= 89:
            #                 if mouse[0] <= 546 and mouse[1] <= 139:
            #                     current_player = player2
            #                     print("testing test test")
            
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()
    
    def initialize_pygame(self):
        pygame.init()

        
        # Set the width and height of the screen [width, height]
        self.size = (700, 500)
        self.screen = pygame.display.set_mode(self.size)
        
        pygame.display.set_caption("Judgemento | V.1")
        
        # Used to manage how fast the screen updates
        #clock = pygame.time.Clock()
        self.sprite_sheet = SpriteSheet('English_pattern_playing_cards_deck.svg.png')

#ActualGame()