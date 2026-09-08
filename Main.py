import sys
import pygame
from Objects.Basketball import Basketball
from Objects.Hoop import Hoop
from GameManager import GameManager
from ANN import ANN

# Initialization
pygame.init()

# Screen Setup
WIDTH = 1400
HEIGHT = 800
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ANN Basketball")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
my_font = pygame.font.SysFont(None, 48)

# Time and Framerate
clock = pygame.time.Clock()

# Game Objects
hoop1 = Hoop(700, 200)



gamemanager1 = GameManager(hoop1, WIDTH, HEIGHT)
gamemanager1.createFirstGen()



# Game State Variables
running = True
framesTillReset = 400
frames = 0

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
    for ball in gamemanager1.balls:
        ball.update(HEIGHT, WIDTH)
    for ann in gamemanager1.anns:
        ann.update()
    gamemanager1.update()

    
    # 3. Rendering
    Screen.fill(WHITE)
    for ball in gamemanager1.balls:
        ball.draw(Screen)
    hoop1.draw(Screen)
    
    score_text = my_font.render(f"Score: {gamemanager1.score}", True, BLACK)
    Screen.blit(score_text, (20, 10))
    fitnessscore = my_font.render(f"Score: {ann.fitnessScore}", True, BLACK)
    Screen.blit(fitnessscore, (400, 10))
    generation = my_font.render(f"Gen: {gamemanager1.generation}", True, BLACK)
    Screen.blit(generation, (200, 10))

    framesTillReset -= 1
    if framesTillReset == 0:
        framesTillReset = 400
        gamemanager1.newgen()
    pygame.display.flip()

    if gamemanager1.generation < 100:
        clock.tick(2000)
    else:
        clock.tick(60)


pygame.quit()
sys.exit()