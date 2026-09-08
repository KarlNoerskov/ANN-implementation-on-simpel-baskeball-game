import pygame

class Renderer:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Basketball ANN")
        self.clock = pygame.time.Clock()
        
        self.WHITE = (255, 255, 255)
        self.BALL_ORANGE = (255, 140, 0)
        self.HOOP_DARK_ORANGE = (200, 100, 0)
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Times New Roman', 22)
        self.generation = 0

    def draw_everything(self, balls, hoop, generation, scenario_idx, best_fitness):
        self.generation = generation
        self.handle_events()
        self.clear()
        self.draw_hoop(hoop)
        self.draw_balls(balls)
        self.draw_info(generation, scenario_idx, best_fitness)
        self.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def clear(self):
        self.screen.fill(self.WHITE)

    def draw_balls(self, balls):
        for basketball in balls:
            pygame.draw.circle(self.screen, self.BALL_ORANGE, (int(basketball.x), int(basketball.y)), basketball.radius)

    def draw_hoop(self, hoop):
        if hoop:
            pygame.draw.rect(self.screen, self.HOOP_DARK_ORANGE, (hoop.x, hoop.y, hoop.rim_width, hoop.rim_height))

    def draw_info(self, generation, scenario_idx, best_fitness):
        if generation <= 200:
            text = f"TRAINING | Gen: {generation}/200 | Scenario: {scenario_idx}/10 | Best Fitness: {best_fitness:.1f}"
            color = (0, 0, 0)

        elif generation == 999:
            text = f"FINAL EVALUATION | Evaluating Population | Scenario: {scenario_idx}/50"
            color = (0, 0, 200)

        else: 
            text = f"SHOWCASE MODE | Champion Network | Scenarios Completed: {scenario_idx}"
            color = (0, 150, 0) 

        text_surface = self.my_font.render(text, False, color)
        self.screen.blit(text_surface, (10, 10))

    def update(self):
        pygame.display.flip()
        if self.generation <= 200 or self.generation == 999:
            self.clock.tick(12000)
        else:
            self.clock.tick(60)