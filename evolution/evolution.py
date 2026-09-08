from neural_network.neural_network import NeuralNetwork
import random

class Evolution:

    def __init__(self, population_size=500, elite_count=10):
        self.population_size = range(population_size)
        self.elite_count = elite_count

        self.population = []
        for population in self.population_size:
            self.population.append(NeuralNetwork())



    def next_generation(self, fitnnesses):
        # Fitnnesses has to be in same order as ANNs
        # we zip them with their fitness and sort for fitnesses in reverse order so highest is at the top
        ranked = sorted (zip(self.population, fitnnesses), key=lambda x: x[1], reverse= True)

        elites = [
            network
            for network, fitness in ranked[:self.elite_count]
        ]

        new_population = elites.copy()

        while len(new_population) < 500:
            parent = random.choice(elites)
            parent = elites[1]
            child = parent.copy()
            child.mutate()

            new_population.append(child)

        self.population = new_population
    