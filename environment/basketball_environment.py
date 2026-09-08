import random
from game.Objects.Basketball import Basketball
from game.Objects.Hoop import Hoop

class Scenario:
    def __init__(self, ball_x, ball_y, hoop_x, hoop_y):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.hoop_x = hoop_x
        self.hoop_y = hoop_y


class BasketballEnvironment:

    def __init__(self, renderer):
        self.renderer = renderer

    def create_scenario(self):
        ball_x = random.randint(24, 400 - 24)
        ball_y = random.randint(24, 600 - 24)
        hoop_x = random.randint(600, 800 - 90)
        hoop_y = random.randint(50, 300)

        return Scenario(ball_x, ball_y, hoop_x, hoop_y)

    def evaluate_population_parallel(self, population, scenario, generation_num, scenario_idx, best_fitness):
        hoop = Hoop(scenario.hoop_x, scenario.hoop_y)
        
        balls = []
        smallest_distances = []

        for network in population:
            ball = Basketball(scenario.ball_x, scenario.ball_y, hoop)
            
            delta_x = (hoop.x + hoop.rim_width / 2 - ball.x)
            delta_y = hoop.y - ball.y
            state = [delta_x / 800, delta_y / 600]

            action = network.forward(state)
            power_x, power_y = action
            ball.shoot(power_x, power_y)

            balls.append(ball)
            smallest_distances.append(float("inf"))

        for _ in range(200):
            for i, ball in enumerate(balls):
                ball.update(600, 800)
                
                hoop_x = hoop.x + hoop.rim_width / 2
                hoop_y = hoop.y
                dx = ball.x - hoop_x
                dy = ball.y - hoop_y
                distance = (dx ** 2 + dy ** 2) ** 0.5

                smallest_distances[i] = min(smallest_distances[i], distance)

            if self.renderer:
                self.renderer.draw_everything(balls, hoop, generation_num, scenario_idx, best_fitness)

        fitnesses = []
        for i, ball in enumerate(balls):
            fitness = -smallest_distances[i]
            if ball.scored:
                fitness += 1000
            fitnesses.append(fitness)

        return fitnesses