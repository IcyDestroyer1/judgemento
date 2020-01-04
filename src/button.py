# ./src/button.py
"""
  This file exports the menuAtivo states for all buttons on screen

  The current commented out code doesn't work... I think 🧐
"""

# import pygame

# pygame.init();
# screen = pygame.display.set_mode((400,300));
# menuAtivo = True;

# switch_button = pygame.draw.rect(screen,(0,0,2),(150,90,100,50));


# pygame.display.flip();

# def startGame():
#     screen.fill((0,0,0));
#     pygame.display.flip();
#     import nemesis.py;

# while menuAtivo:
#     for evento in pygame.event.get():
#         print(evento);
#         if evento.type == pygame.MOUSEBUTTONDOWN:
#             if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
#                 if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
#                         print("I QUIT")
#                         #pygame.quit()
#             if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
#                 if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
#                         print("YOU LICKED ME ;)")
#                         #startGame();