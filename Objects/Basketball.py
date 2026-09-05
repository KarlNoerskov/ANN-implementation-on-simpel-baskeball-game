import pygame

ORANGE = (255, 165, 0)

class Basketball:
    def __init__(self, start_x, start_y, hoop):
        self.x = start_x
        self.y = start_y
        self.radius = 24
        self.farve = ORANGE
        self.vel_x = 0
        self.vel_y = 0
        self.bounce_factor = -0.8
        self.gravity = 0.5
        self.Hoop = hoop

    def draw(self, background):
        pygame.draw.circle(background, self.farve, (self.x, self.y), self.radius)

    def shoot(self, power):
        self.vel_y -= power
        self.vel_x += power


    def update(self, floor_y, floor_x):
        V_pos = pygame.math.Vector2(self.x, self.y)
        V_vel = pygame.math.Vector2(self.vel_x, self.vel_y)
        
        # 1. Update vel with gravity
        self.vel_y += self.gravity
        
        
        # 2. update pos
        self.y += self.vel_y
        self.x += self.vel_x
        
        # 3. check collision
        self.collisionChecker(floor_y, floor_x, V_pos, V_vel)


    def collisionChecker(self, floor_y, floor_x, V_pos, V_vel):
        self.collisionWall (floor_y, floor_x)
        self.collisionHoop(V_pos, V_vel)

    def collisionWall(self, floor_y, floor_x):
        # Y logic
        if self.y + self.radius >= floor_y:
            self.y = floor_y - self.radius
            self.vel_y = self.vel_y * self.bounce_factor

        # X logic
        if self.x + self.radius >= floor_x:
            self.x = floor_x - self.radius
            self.vel_x = self.vel_x * self.bounce_factor
        elif self.x - self.radius <= 0:
            self.x = 0 + self.radius
            self.vel_x = self.vel_x * self.bounce_factor

    def collisionHoop(self, V_pos, V_vel):
        distanceLeftRim = V_pos.distance_to(self.Hoop.left_rim)
        if distanceLeftRim <= self.radius + self.Hoop.rim_radius:
            #move ball out
            normal = (V_pos - self.Hoop.left_rim).normalize()
            distance = self.radius + self.Hoop.rim_radius + 1
            self.x = self.Hoop.left_rim.x + normal.x * distance
            self.y = self.Hoop.left_rim.y + normal.y * distance
            #move ball opposite way of impact
            newVel = V_vel.reflect(normal)
            self.vel_x = newVel.x * -self.bounce_factor
            self.vel_y = newVel.y * -self.bounce_factor

        distanceRightRim = V_pos.distance_to(self.Hoop.right_rim)
        if distanceRightRim <= self.radius + self.Hoop.rim_radius:
            #move ball out
            normal = (V_pos - self.Hoop.right_rim).normalize()
            distance = self.radius + self.Hoop.rim_radius + 1
            self.x = self.Hoop.right_rim.x + normal.x * distance
            self.y = self.Hoop.right_rim.y + normal.y * distance
            #move ball opposite way of impact
            newVel = V_vel.reflect(normal)
            self.vel_x = newVel.x * -self.bounce_factor
            self.vel_y = newVel.y * -self.bounce_factor


