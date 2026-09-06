import pygame

# Colors
BLACK = (0, 0, 0)


class GameManager:
    def __init__(self, Ball, Hoop, ANN):
        # References and State
        self.ball = Ball
        self.score = 0
        self.hoop = Hoop
        self.ann = ANN

    def update(self):
        # Score Tracking Logic
        if self.ball.scored:
            self.score += 1
            self.ball.scored = False
            print("{score}", self.score)

    def reset(self):
        self.score = 0
        self.ball.reset()
        self.hoop.reset()
        self.ann.reset()
        self.ann.calculate_shot_power()