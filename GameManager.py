import pygame

# Colors
BLACK = (0, 0, 0)


class GameManager:
    def __init__(self, Ball, Hoop, ANN):
        # References and State
        self.balls = Ball
        self.score = 0
        self.hoop = Hoop
        self.anns = ANN
        self.generation = 0
        self.resetTimer = pygame.time.get_ticks()

    def update(self):
        # Score Tracking Logic
        for ball in self.balls:
            if ball.scored:
                self.score += 1
                ball.scored = False
                print("{score}", self.score)
        if pygame.time.get_ticks() - self.resetTimer > 4000: 
            bestANN = None
            for ann in self.anns:
                if bestANN == None or ann.fitnessScore > bestANN.fitnessScore:
                    bestANN = ann
            print (bestANN.fitnessScore)
            self.resetTimer = pygame.time.get_ticks()
            self.reset()

        

    def reset(self):
        self.score = 0
        for ball in self.balls:
            ball.reset()
        self.hoop.reset()
        for ann in self.anns:
            ann.reset()
            ann.calculate_shot_power()
        self.generation += 1