import pygame
import random

#Colors
HOOPORANGE = (255, 165, 0)


class Basketball:
    def __init__(self, start_x, start_y, Hoop):
        # --- Physics ---
        self.radius = 24
        self.bounce_factor = -0.8
        self.gravity = 0.5

        # --- Position ---
        self.start_x = start_x
        self.start_y = start_y

        self.x = start_x
        self.y = start_y

        self.old_x = start_x
        self.old_y = start_y

        
        # --- Velocity ---
        self.vel_x = 0
        self.vel_y = 0
        
        # --- Gamestate ---
        self.hoop = Hoop
        self.scored = False

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
        distanceLeftRim = V_pos.distance_to(self.hoop.left_rim)
        if distanceLeftRim <= self.radius + self.hoop.rim_radius:
            normal = (V_pos - self.hoop.left_rim).normalize()
            distance = self.radius + self.hoop.rim_radius + 1
            self.x = self.hoop.left_rim.x + normal.x * distance
            self.y = self.hoop.left_rim.y + normal.y * distance
            
            newVel = V_vel.reflect(normal)
            self.vel_x = newVel.x * -self.bounce_factor
            self.vel_y = newVel.y * -self.bounce_factor

        distanceRightRim = V_pos.distance_to(self.hoop.right_rim)
        if distanceRightRim <= self.radius + self.hoop.rim_radius:
            normal = (V_pos - self.hoop.right_rim).normalize()
            distance = self.radius + self.hoop.rim_radius + 1
            self.x = self.hoop.right_rim.x + normal.x * distance
            self.y = self.hoop.right_rim.y + normal.y * distance
            
            newVel = V_vel.reflect(normal)
            self.vel_x = newVel.x * -self.bounce_factor
            self.vel_y = newVel.y * -self.bounce_factor

    def has_scored(self):
        # Ball must be moving downwards
        if self.vel_y <= 0:
            return

        # Ball must cross the height of the hoop
        crossed_hoop = (self.old_y <= self.hoop.y and self.y > self.hoop.y)

        if not crossed_hoop:
            return

        # Ball must be between the rims
        inside_rim = (self.x >= self.hoop.left_rim.x and self.x <= self.hoop.right_rim.x)

        if inside_rim:
            self.scored = True

    def reset(self, x, y):

            self.start_x = x
            self.start_y = y

            self.x = x
            self.y = y

            self.old_x = x
            self.old_y = y

            self.vel_x = 0
            self.vel_y = 0

            self.scored = False
