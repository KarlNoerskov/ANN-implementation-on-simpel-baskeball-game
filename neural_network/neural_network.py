import numpy as np

class NeuralNetwork:

    def __init__(self, input_size=2, hidden_size=10, output_size=2):
        self.w1 = np.random.randn(input_size, hidden_size)
        self.w2 = np.random.randn(hidden_size, output_size)

    def forward(self, inputs):
        hidden = np.dot(inputs, self.w1)
        hidden = np.tanh(hidden)

        output = np.dot(hidden, self.w2)

        return output

    def copy(self):
        network = NeuralNetwork()

        network.w1 = self.w1.copy()
        network.w2 = self.w2.copy()

        return network

    def mutate(self, mutation_rate=0.1):
        self.w1 += np.random.randn(*self.w1.shape) * mutation_rate
        self.w2 += np.random.randn(*self.w2.shape) * mutation_rate