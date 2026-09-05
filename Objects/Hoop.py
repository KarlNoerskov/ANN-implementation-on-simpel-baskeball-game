import pygame
HOOPCOLOR = (248, 129, 88)

class Hoop:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.rimWidth = 400
        self.rimHeight = 40
        self.rim_radius = 20
        self.left_rim = pygame.math.Vector2(start_x, start_y + (self.rimHeight/2))
        self.right_rim = pygame.math.Vector2(start_x + self.rimWidth, start_y + (self.rimHeight/2))
        

    def draw(self, background):
        pygame.draw.rect(background, HOOPCOLOR,( self.x, self.y, self.rimWidth, self.rimHeight))
        #left circle
        pygame.draw.circle(background, HOOPCOLOR, (self.left_rim), self.rim_radius)
        #right circle
        pygame.draw.circle(background, HOOPCOLOR, (self.right_rim), self.rim_radius)
