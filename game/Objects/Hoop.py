import pygame


class Hoop:

    def __init__(self, x, y):

        # Dimensions
        self.rim_width = 90
        self.rim_height = 3
        self.rim_radius = 1.5

        # Position
        self.x = x
        self.y = y

        self.update_rim_positions()

    def update_rim_positions(self):

        self.left_rim = pygame.math.Vector2(self.x, self.y + self.rim_height / 2)
        self.right_rim = pygame.math.Vector2(self.x + self.rim_width, self.y + self.rim_height / 2)