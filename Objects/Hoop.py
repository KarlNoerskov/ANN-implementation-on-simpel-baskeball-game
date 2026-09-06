import pygame

# Colors
HOOPCOLOR = (248, 129, 88)


class Hoop:
    def __init__(self, start_x, start_y):
        # Position
        self.x = start_x
        self.y = start_y
        
        # Dimensions and Collisions
        self.rimWidth = 90
        self.rimHeight = 3
        self.rim_radius = 1.5
        
        # Rim Vectors
        self.left_rim = pygame.math.Vector2(start_x, start_y + (self.rimHeight / 2))
        self.right_rim = pygame.math.Vector2(start_x + self.rimWidth, start_y + (self.rimHeight / 2))

    def draw(self, background):
        # Draw Backboard / Rim Structure
        pygame.draw.rect(background, HOOPCOLOR, (self.x, self.y, self.rimWidth, self.rimHeight))
        
        # Draw Left Rim Collision Point
        pygame.draw.circle(background, HOOPCOLOR, (self.left_rim), self.rim_radius)
        
        # Draw Right Rim Collision Point
        pygame.draw.circle(background, HOOPCOLOR, (self.right_rim), self.rim_radius)