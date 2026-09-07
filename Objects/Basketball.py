import pygame
import random

#Colors
HOOPORANGE = (255, 165, 0)


class Basketball:
    def __init__(self, start_x, start_y, hoop):
        # Physics
        self.radius = 24
        self.bounce_factor = -0.8
        self.gravity = 0.5

        # Random start position
        #Randomx = random.randint(self.radius, 400-self.radius)
        #Randomy = random.randint(self.radius, 600- self.radius)

        # Position
        self.startx = start_x
        self.starty = start_y
        self.x = start_x
        self.y = start_y
        self.old_x = 0
        self.old_y = 0

        # Start Position
        self.StartPos = pygame.math.Vector2(self.x, self.y)
        
        # Velocity
        self.vel_x = 0
        self.vel_y = 0
        
        
        # Gamestate
        self.Hoop = hoop
        self.scored = False
        self.scoreTimer = 0

    def draw(self, background):
        pygame.draw.circle(background, HOOPORANGE, (self.x, self.y), self.radius)

    def shoot(self, powerx, powery):
        self.vel_y -= powery
        self.vel_x += powerx

    def update(self, floor_y, floor_x):
        V_pos = pygame.math.Vector2(self.x, self.y)
        V_vel = pygame.math.Vector2(self.vel_x, self.vel_y)
        
        self.vel_y += self.gravity
        
        self.old_y = self.y
        self.old_x = self.x
        
        self.y += self.vel_y
        self.x += self.vel_x
        
        self.collisionChecker(floor_y, floor_x, V_pos, V_vel)
        self.has_scored()

    def collisionChecker(self, floor_y, floor_x, V_pos, V_vel):
        self.collisionWall(floor_y, floor_x)
        self.collisionHoop(V_pos, V_vel)

    def collisionWall(self, floor_y, floor_x):
        if self.y + self.radius >= floor_y:
            self.y = floor_y - self.radius
            self.vel_y = self.vel_y * self.bounce_factor

        if self.x + self.radius >= floor_x:
            self.x = floor_x - self.radius
            self.vel_x = self.vel_x * self.bounce_factor
        elif self.x - self.radius <= 0:
            self.x = 0 + self.radius
            self.vel_x = self.vel_x * self.bounce_factor

    def collisionHoop(self, V_pos, V_vel):
        distanceLeftRim = V_pos.distance_to(self.Hoop.left_rim)
        if distanceLeftRim <= self.radius + self.Hoop.rim_radius:
            normal = (V_pos - self.Hoop.left_rim).normalize()
            distance = self.radius + self.Hoop.rim_radius + 1
            self.x = self.Hoop.left_rim.x + normal.x * distance
            self.y = self.Hoop.left_rim.y + normal.y * distance
            
            newVel = V_vel.reflect(normal)
            self.vel_x = newVel.x * -self.bounce_factor
            self.vel_y = newVel.y * -self.bounce_factor

        distanceRightRim = V_pos.distance_to(self.Hoop.right_rim)
        if distanceRightRim <= self.radius + self.Hoop.rim_radius:
            normal = (V_pos - self.Hoop.right_rim).normalize()
            distance = self.radius + self.Hoop.rim_radius + 1
            self.x = self.Hoop.right_rim.x + normal.x * distance
            self.y = self.Hoop.right_rim.y + normal.y * distance
            
            newVel = V_vel.reflect(normal)
            self.vel_x = newVel.x * -self.bounce_factor
            self.vel_y = newVel.y * -self.bounce_factor

    def has_scored(self):
        if self.scoreTimer != 0 and pygame.time.get_ticks() - self.scoreTimer < 1000:
            return
        else:
            BetweenGoalPoast = False
            if self.x >= self.Hoop.left_rim.x + self.Hoop.rim_radius and self.x <= self.Hoop.right_rim.x + self.Hoop.rim_radius:
                if self.y > self.Hoop.y and self.old_y <= self.Hoop.y:
                    BetweenGoalPoast = True
                    
            if self.vel_y > 0 and BetweenGoalPoast:
                self.scored = True
                self.scoreTimer = pygame.time.get_ticks()

    def reset(self):
        self.x = random.randint(self.radius, 400-self.radius)
        self.y = random.randint(self.radius, 600- self.radius)

        self.vel_x = 0
        self.vel_y = 0

        self.scored = False
        self.scoreTimer = 0