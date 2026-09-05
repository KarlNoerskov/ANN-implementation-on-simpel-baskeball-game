import pygame
from Objects.Basketball import Basketball
from Objects.Hoop import Hoop
import sys

pygame.init()

#Screen
WIDTH = 800
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ANN Basketball")

#Colors
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

#Control Framerate
clock = pygame.time.Clock()
#objects
hoop1 = Hoop(300, 200)
basketball1 = Basketball(100, 100, hoop1)
#parameters
shotCharging = False
shotPower = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shotCharging = True
        if event.type == pygame.MOUSEBUTTONUP:
            shotCharging = False
            basketball1.shoot(shotPower)
            shotPower = 0

    # --- 2. LOGIK ---
    basketball1.update(HEIGHT, WIDTH)
    if shotCharging == True:
        shotPower += 0.5

    # --- 3. RENDER (Tegn skærmen) ---
    Screen.fill(WHITE) # Start altid med at viske tavlen ren
    basketball1.draw(Screen)
    hoop1.draw(Screen)
    # TODO: Tegn bolden her!
    # Tip: Kig evt. på pygame.draw.circle()

    # Opdater skærmen, så vi kan se, hvad vi har tegnet
    pygame.display.flip()
    
    # Begræns til 60 frames per sekund
    clock.tick(60)

pygame.quit()
sys.exit()