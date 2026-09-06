import pygame

BLACK = (0, 0, 0)

class GameManager:
    def __init__(self, Ball):
        self.ball = Ball
        self.score = 0

    def update(self):
        if self.ball.scored:
            self.score += 1
            self.ball.scored = False
            print("{score}", self.score)
        