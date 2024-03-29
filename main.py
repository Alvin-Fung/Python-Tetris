import pygame,sys
from game import Game

# Game loop
pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600)) # Width, Height
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
running = True

game = Game()

while running:
    for event in pygame.event.get():
        # pygame.QUIT event allows the user to click X to close the game window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            
    # Game Rendering/Drawing
    screen.fill(dark_blue)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # Limits the game to run at 60 FPS.
    

