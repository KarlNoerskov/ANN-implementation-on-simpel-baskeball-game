import sys
import pygame
from Objects.Basketball import Basketball
from Objects.Hoop import Hoop
from GameManager import GameManager

# Initialization
pygame.init()

# Screen Setup
WIDTH = 800
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ANN Basketball")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

# Fonts
my_font = pygame.font.SysFont(None, 48)

# Time and Framerate
clock = pygame.time.Clock()

# Game Objects
hoop1 = Hoop(700, 200)
basketball1 = Basketball(100, 100, hoop1)
gamemanager1 = GameManager(basketball1)

# Game State Variables
shotCharging = False
shotPower = 0
running = True

# Main Game Loop
while running:
    
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shotCharging = True
        if event.type == pygame.MOUSEBUTTONUP:
            shotCharging = False
            basketball1.shoot(shotPower)
            shotPower = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                gamemanager1.reset()
                shotCharging = False
                shotPower = 0

    # 2. Logic Update
    basketball1.update(HEIGHT, WIDTH)
    gamemanager1.update()
    
    if shotCharging == True:
        shotPower += 0.5

    # 3. Rendering
    Screen.fill(WHITE)
    
    basketball1.draw(Screen)
    hoop1.draw(Screen)
    
    score_text = my_font.render(f"Score: {gamemanager1.score}", True, BLACK)
    Screen.blit(score_text, (20, 20))
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()