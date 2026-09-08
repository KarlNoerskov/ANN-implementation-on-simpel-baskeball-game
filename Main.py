from environment.basketball_environment import BasketballEnvironment
from evolution.evolution import Evolution
from rendering.rendering import Renderer

def main():
    renderer = Renderer()
    environment = BasketballEnvironment(renderer=renderer)
    evolution = Evolution(population_size=500, elite_count=10)
    scenariosPrGen = 10
    scenariosLastTest = 50
    best_overall_fitness = float("-inf")

    for generation in range(200):
        gen_number = generation + 1

        scenarios = [
            environment.create_scenario()
            for _ in range(scenariosPrGen)
        ]

        total_fitnesses = [0.0] * len(evolution.population)

        for s_idx, scenario in enumerate(scenarios):
            scenario_number = s_idx + 1

            scenario_fitnesses = environment.evaluate_population_parallel(evolution.population, scenario, gen_number, scenario_number, best_overall_fitness)

            for i, fit in enumerate(scenario_fitnesses):
                total_fitnesses[i] += fit

        avg_fitnesses = [fit / scenariosPrGen for fit in total_fitnesses]

        current_best = max(avg_fitnesses)
        if current_best > best_overall_fitness:
            best_overall_fitness = current_best

        evolution.next_generation(avg_fitnesses)
        print(f"Generation {gen_number}: best average fitness = {current_best:.2f}")


    scenarios = [
                environment.create_scenario()
                for _ in range(scenariosLastTest)
            ]
    
    total_fitnesses = [0.0] * len(evolution.population)

    for s_idx, scenario in enumerate(scenarios):
        scenario_number = s_idx + 1

        scenario_fitnesses = environment.evaluate_population_parallel(evolution.population, scenario, 999, scenario_number, best_overall_fitness)

        for i, fit in enumerate(scenario_fitnesses):
            total_fitnesses[i] += fit

    avg_fitnesses = [fit / scenariosLastTest for fit in total_fitnesses]

    current_best = max(avg_fitnesses)
    if current_best > best_overall_fitness:
        best_overall_fitness = current_best

    champion_index = avg_fitnesses.index(current_best)
    champion_network = evolution.population[champion_index]
    showcase_scenario_number = 1
    
    while True:
        nyt_scenario = environment.create_scenario()

        environment.evaluate_population_parallel([champion_network], nyt_scenario, 1000, showcase_scenario_number, best_overall_fitness)
        
        showcase_scenario_number += 1


    
    
    
if __name__ == "__main__":
    main()