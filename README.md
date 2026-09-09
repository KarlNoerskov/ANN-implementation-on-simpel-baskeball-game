# Artificial Neural Network in a Simple Basketball Game

This project implements an Artificial Neural Network (ANN) that learns to play a simple 2D basketball game using **neuroevolution**.

<img width="800" height="450" alt="Training Process" src="https://github.com/user-attachments/assets/a7129cd3-f2be-4bea-a57c-9f86f5b52e30" />

## Overview & Training Process

Instead of using backpropagation, the model trains through a genetic algorithm relying on fitness-based selection and random mutation. 

The training pipeline follows these steps:

1. **Initialization:** A population of 500 ANNs is created.
2. **Simulation:** Each ANN plays through 10 randomly generated scenarios with varying hoop locations and ball spawn points.
3. **Evaluation:** After the 10 scenarios, each ANN receives an average fitness score based on its performance. The score is calculated using the following formula, where the 1000-point bonus is only awarded if the ball successfully goes through the hoop:
   `Fitness = -SmallestDistance + (1000 * Scored)`
4. **Selection:** The top 10 ANNs (the "elites") with the highest fitness scores are selected.
5. **Mutation:** The elites are carried over to the next generation and copied. The copies undergo random small mutations to their weights.
6. **Iteration:** This cycle repeats for 200 generations (evaluating 1,000,000 shots in total) to allow the ANNs to gradually improve their performance.
7. **Final Evaluation:** The final generation battles across 50 scenarios to crown a single champion, which is then displayed in an endless showcase loop.

<img width="800" height="450" alt="Champion Network" src="https://github.com/user-attachments/assets/7a72ac47-7078-4495-b74a-3bcd71492be2" />

## Performance & Future Improvements

Currently, the neuroevolution model successfully hits the target approximately 9 out of 10 times after 200 generations. 

**Planned Version 2.0 Features:**
* Implementing **backpropagation** to compare training speeds and efficiency against the current neuroevolution approach.
* Modifying the fitness evaluation to train the network on dynamic generalization (hitting any hoop from any distance) rather than specializing in fixed scenarios.

## Installation

Python can be downloaded from [python.org](https://www.python.org/downloads/). 

It is recommended to use a virtual environment so the installed packages do not affect other Python projects on your computer.

**1. Clone this repository:**
```bash
git clone [https://github.com/KarlNoerskov/artificial-neural-network-implemented-on-simple-basketballgame.git](https://github.com/KarlNoerskov/artificial-neural-network-implemented-on-simple-basketballgame.git)
cd artificial-neural-network-implemented-on-simple-basketballgame
