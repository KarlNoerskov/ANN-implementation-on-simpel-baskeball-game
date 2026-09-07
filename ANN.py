import pygame
import numpy

class ANN:
    def __init__(self, Hoop, Basketball, SCREENWIDTH, SCREENHEIGHT):
        # Basketball Y and X
        self.basketball = Basketball
        self.BasketballX = Basketball.x
        self.BasketballY = Basketball.y
        self.BasketballVec = pygame.math.Vector2(self.BasketballX, self.BasketballY)

        # Weights
        self.W_1 = numpy.random.randn(2, 10)
        self.W_2 = numpy.random.randn(10, 2)

        # Hoop X and Y
        self.hoop = Hoop
        self.hoopX = Hoop.x
        self.hoopY = Hoop.y
        self.HoopVec = pygame.math.Vector2(self.hoopX - Hoop.rimWidth / 2, self.hoopY)

        # Delta distance to hoop
        self.screenwidth = SCREENWIDTH
        self.screenheight = SCREENHEIGHT
        self.deltaX = (self.BasketballX - self.hoopX) / self.screenwidth * 2 - 1
        self.deltaY = (self.BasketballY - self.hoopY) / self.screenheight * 2 - 1
        self.deltaArray = numpy.array([self.deltaX, self.deltaY])

        # Smallest distance
        self.smallestDistance = None
        self.fitnessScore = 0

    def update(self):
        self.BasketballVec = pygame.math.Vector2(self.basketball.x, self.basketball.y)
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
        
        powerx = float(second[0])
        powery = float(second[1])

        #print(self.sigmoid(powerx, 20))
        self.basketball.shoot(self.sigmoid(powerx, 20.0), self.sigmoid(powery, 20.0))

    def reset(self):
        self.BasketballX = self.basketball.x
        self.BasketballY = self.basketball.y
        self.BasketballVec = pygame.math.Vector2(self.BasketballX, self.BasketballY)

        # Hoop X and Y
        self.hoopX = self.hoop.x
        self.hoopY = self.hoop.y
        self.HoopVec = pygame.math.Vector2(self.hoopX - self.hoop.rimWidth / 2, self.hoopY)

        self.deltaX = (self.BasketballX - self.hoopX) / self.screenwidth * 2 - 1
        self.deltaY = (self.BasketballY - self.hoopY) / self.screenheight * 2 - 1
        self.deltaArray = numpy.array([self.deltaX, self.deltaY])

        self.smallestDistance = None

    def sigmoid(self, floaty, x):
        return 1/(1 + numpy.exp(-floaty)) * x

    def updateBasketball(self, Basketball):
        self.basketball = Basketball
        self.BasketballX = Basketball.x
        self.BasketballY = Basketball.y
        self.BasketballVec = pygame.math.Vector2(self.BasketballX, self.BasketballY)


        # Delta distance to hoop
        self.deltaX = (self.BasketballX - self.hoopX) / self.screenwidth * 2 - 1
        self.deltaY = (self.BasketballY - self.hoopY) / self.screenheight * 2 - 1
        self.deltaArray = numpy.array([self.deltaX, self.deltaY])

        # Smallest distance
        self.smallestDistance = None
        self.fitnessScore = 0

    def mutation(self, mutationrate):
        W_1mutation = numpy.random.randn(2, 10) * mutationrate
        w_2mutation = numpy.random.randn(10, 2) * mutationrate
        self.W_1 = self.W_1 + W_1mutation
        self.W_2 = self.W_2 + w_2mutation

