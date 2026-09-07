import pygame
import numpy

class ANN:
    def __init__(self, Hoop, Basketball):
        # Basketball Y and X
        self.basketball = Basketball
        self.BasketballX = Basketball.x
        self.BasketballY = Basketball.y
        self.BasketballVec = pygame.math.Vector2(self.BasketballX, self.BasketballY)

        # Weights
        self.W_1 = numpy.random.randn(2, 10)
        self.W_2 = numpy.random.randn(10, 1)

        # Hoop X and Y
        self.hoop = Hoop
        self.hoopX = Hoop.x
        self.hoopY = Hoop.y
        self.HoopVec = pygame.math.Vector2(self.hoopX - Hoop.rimWidth / 2, self.hoopY)

        # Delta distance to hoop
        self.deltaX = self.BasketballX - self.hoopX
        self.deltaY = self.BasketballY - self.hoopY
        self.deltaArray = numpy.array([self.deltaX, self.deltaY])

        # Smallest distance
        self.smallestDistance = None
        self.fitnessScore = 0

    def update(self):
        self.BasketballVec =  self.BasketballVec = pygame.math.Vector2(self.basketball.x, self.basketball.y)
        self.smallestDistanceToRimFromBall()
        

    def smallestDistanceToRimFromBall(self):
        if self.smallestDistance == None or self.BasketballVec.distance_to(self.HoopVec) < self.smallestDistance:
            self.smallestDistance = pygame.math.Vector2(self.basketball.x, self.basketball.y).distance_to(self.HoopVec)
            #we want the succes score to be posetive, so we minus by 1000 pixels to get that a good score i positive
            #we put in power to make it eksponentielly better to be close
        fitness = (self.smallestDistance - 1000)**2
        if self.basketball.scored:
            fitness = fitness * 10000 
        if fitness > self.fitnessScore:
            self.fitnessScore = fitness
            #print (fitness)

        
    def calculate_shot_power(self):
        first = numpy.dot(self.deltaArray, self.W_1)
        second = numpy.dot(first, self.W_2)
        
        power = float(second[0])
        
        if power < 0:
            power = 0

        self.basketball.shoot(self.sigmoid(power, 20.0))

    def reset(self):
        self.BasketballX = self.basketball.x
        self.BasketballY = self.basketball.y
        self.BasketballVec = pygame.math.Vector2(self.BasketballX, self.BasketballY)

        # Hoop X and Y
        self.hoopX = self.hoop.x
        self.hoopY = self.hoop.y
        self.HoopVec = pygame.math.Vector2(self.hoopX - self.hoop.rimWidth / 2, self.hoopY)

        self.deltaX = self.BasketballX - self.hoopX
        self.deltaY = self.BasketballY - self.hoopY
        self.deltaArray = numpy.array([self.deltaX, self.deltaY])

        self.smallestDistance = None

    def sigmoid(self, floaty, x):
        return 1/(1 + numpy.exp(-floaty)) * x

