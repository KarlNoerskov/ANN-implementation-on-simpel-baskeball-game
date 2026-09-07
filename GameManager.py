import pygame
import copy
import random
from ANN import ANN
from Objects.Basketball import Basketball

# Colors
BLACK = (0, 0, 0)


class GameManager:
    def __init__(self, Hoop, SCREENWIDTH, SCREENHEIGHT):
        self.numberOfANNS = range(500)
        # References and State
        #self.balls = Ball
        self.balls = []
        self.score = 0
        self.hoop = Hoop
        self.anns = []
        self.generation = 1
        self.resetTimer = pygame.time.get_ticks()
        self.bestANN = None
        self.screenwidth = SCREENWIDTH
        self.screenheight = SCREENHEIGHT

    def update(self):
        # Score Tracking Logic
        for ball in self.balls:
            if ball.scored:
                self.score += 1
                ball.scored = False
        if pygame.time.get_ticks() - self.resetTimer > 1500: 
            print("{generation}", self.generation)
            print("{score}", self.score)
            self.score = 0
            self.generation += 1
            self.createNewANNSFromBest()
            self.resetTimer = pygame.time.get_ticks()

        

    def reset(self):
        self.score = 0
        for ball in self.balls:
            ball.reset()
        if self.score < 100:
            self.hoop.reset()
        for ann in self.anns:
            ann.reset()
            ann.calculate_shot_power()
        self.generation += 1

    def createFirstGen(self):
        for x in self.numberOfANNS:
            newBall = Basketball(100, 100, self.hoop)
            self.balls.append(newBall)
            newAnn = ANN(self.hoop, newBall, self.screenwidth, self.screenheight)
            self.anns.append(newAnn)
        for x in self.anns:
            x.calculate_shot_power()


    def chooseBest(self):
        for ann in self.anns:
            if self.bestANN == None or ann.fitnessScore > self.bestANN.fitnessScore:
                self.bestANN = ann

    def createNewANNSFromBest(self):
        self.chooseBest()
        self.anns = []
        oldball = self.balls[0]
        self.balls = []
        if self.score > 100:
            self.hoop.reset()
        if self.score > 100:
            ballx = random.randint(oldball.radius, 400-oldball.radius)
            bally = random.randint(oldball.radius, 600 - oldball.radius)
        else:
            ballx = oldball.startx
            bally = oldball.starty

        for x in self.numberOfANNS:
            newBall = Basketball(ballx, bally, self.hoop)
            self.balls.append(newBall)
            newAnn = copy.deepcopy(self.bestANN)
            newAnn.updateBasketball(newBall)
            newAnn.fitnessScore = 0
            self.anns.append(newAnn)
            if self.score == 0:
                newAnn.mutation(1)
            else:
                newAnn.mutation(1 * 0.95**self.generation)
        print(1 * (0.95**self.generation))
        newBall1 = Basketball(ballx, bally, self.hoop)
        self.balls.append(newBall1)
        self.bestANN.updateBasketball(newBall1)
        self.anns.append(self.bestANN)

        for x in self.anns:
            x.calculate_shot_power()

