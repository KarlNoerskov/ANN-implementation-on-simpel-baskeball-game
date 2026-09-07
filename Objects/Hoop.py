import pygame
import random

# Colors
HOOPCOLOR = (248, 129, 88)


class Hoop:
    def __init__(self, start_x, start_y):
        # --- Dimensions and Collisions ---
        self.rimWidth = 90
        self.rimHeight = 3
        self.rim_radius = 1.5

        # --- Random start position ---
        Randomx = random.randint(600, 800 - self.rimWidth)
        Randomy = random.randint(50, 300)
        

        # --- Position ---
        self.x = Randomx
        self.y = Randomy
        
        
        # --- Rim Vectors ---
        self.left_rim = pygame.math.Vector2(self.x, self.y + (self.rimHeight / 2))
        self.right_rim = pygame.math.Vector2(self.x + self.rimWidth, self.y + (self.rimHeight / 2))

    def draw(self, background):
        # Draw Backboard / Rim Structure
        pygame.draw.rect(background, HOOPCOLOR, (self.x, self.y, self.rimWidth, self.rimHeight))
        
        # Draw Left Rim Collision Point
        pygame.draw.circle(background, HOOPCOLOR, (self.left_rim), self.rim_radius)
        
        # Draw Right Rim Collision Point
        pygame.draw.circle(background, HOOPCOLOR, (self.right_rim), self.rim_radius)

    def reset(self):
        self.x = random.randint(600, 800 - self.rimWidth)
        self.y = random.randint(50, 500)
        self.left_rim = pygame.math.Vector2(self.x, self.y + (self.rimHeight / 2))
        self.right_rim = pygame.math.Vector2(self.x + self.rimWidth, self.y + (self.rimHeight / 2))