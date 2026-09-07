import sys
import pygame
from Objects.Basketball import Basketball
from Objects.Hoop import Hoop
from GameManager import GameManager
from ANN import ANN
import random

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
numberOfANNs = range(200)
hoop1 = Hoop(700, 200)
balls = []
anns = []
for x in numberOfANNs:
    newBall = Basketball(100, 100, hoop1)
    balls.append(newBall)
    newAnn = ANN(hoop1, newBall)
    anns.append(newAnn)

    

gamemanager1 = GameManager(balls, hoop1, anns)
gamemanager1.reset()


# Game State Variables
shotCharging = False
shotPower = 0
running = True
hasShot = True

# Main Game Loop
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                hasShot = True
                gamemanager1.reset()
                shotCharging = False
                shotPower = 0

    # 2. Logic Update
    for ball in balls:
        ball.update(HEIGHT, WIDTH)
    for ann in anns:
        ann.update()
    gamemanager1.update()

    
    # 3. Rendering
    Screen.fill(WHITE)
    for ball in balls:
        ball.draw(Screen)
    hoop1.draw(Screen)
    
    score_text = my_font.render(f"Score: {gamemanager1.score}", True, BLACK)
    Screen.blit(score_text, (20, 20))
    score_text = my_font.render(f"Score: {ann.fitnessScore}", True, BLACK)
    Screen.blit(score_text, (400, 20))
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()