# Artificial Neural Network used on a simple basketball game

An artificial neural network (ANN) used on a simple basketball game.

The ANN trains using neuro-evolution. From generation to generation, the ANN with the best fitness score is selected and randomly mutated by a small amount.

In this implementation, 500 ANNs are running at the same time. Each generation runs through ten scenarios before the average fitness scores are compared and the next generation is created.

<img width="800" height="450" alt="basketball gif" src="https://github.com/user-attachments/assets/a7129cd3-f2be-4bea-a57c-9f86f5b52e30" />


## How it works

Each generation starts with 500 ANNs.

The ANNs all play the game for 10 different scenario. All 10 scenarios are randomly created with a random hoop location and ball spawn. After the 10 scenarios, each ANN gets an average fitness score based on how well it performed.

the fitnessscore is calculated by:
$fitness = -smallest_distances[i] + 1000 * scored$

where scored only gets added if the artifical network scored the ball in the basket.

The 10 ANN's (the elites) with the highest fitness score are then selected. These ANN are copied and the copies are randomly mutated by a small amount to create the next generation. We still keep the elites in the population, untill they are no longer the best.

This process is repeated over and over, allowing the ANN to gradually improve its performance.

The basic process is:

1. Create 500 ANNs.
2. Run each ANN through 10 scenarios.
3. Calculate the fitness score for each ANN.
4. Select the 10 ANN's with the highest fitness score.
5. Copy the best ANN's.
6. Randomly mutate the copies.
7. Use the mutated ANNs as the next generation + the elite ANN's from the last generation.
8. Repeat untill 200 generations have been played through.
9. the last badge of ANN's battle it out over 50 scenarios to find the champion wich then goes on a endless showcase
loop while not changing

## Training

The current implementation uses:

- 500 ANNs per generation
- 10 scenarios pr generation
- Neuro-evolution
- Fitness-based selection
- Random mutation

The ANN is not trained using backpropagation. Instead, the weights of the network are changed through random mutations and the network that perform better are kept for the next generation. Next step is probably to try and compare the results of a backpropagation model, with the current implementation. Neuroevolution does create a fairly good result, wich hits the target about 9/10 times (see gif below), but it takes 200 generations with 500 anns in each generation and 10 scenarios; 1.000.000 shots too do so. it would be interesting to see if this could be done faster with another method.


<img width="800" height="450" alt="championbasketballgifd" src="https://github.com/user-attachments/assets/7a72ac47-7078-4495-b74a-3bcd71492be2" />


## Installation
Python can be downloaded from:
https://www.python.org/downloads/

See `requirements.txt` for the required Python packages.

It is recommended to use a virtual environment so the installed packages do not affect other Python projects on your computer.

Create a virtual environment:

    python3 -m venv venv

Activate it on Linux/macOS:

    source venv/bin/activate

On Windows:

    venv\Scripts\activate


Clone this repository:

    git clone https://github.com/KarlNoerskov/ANN-implementation-on-simpel-baskeball-game.git

Go into the project directory:

    cd ANN-implementation-on-simpel-baskeball-game

Install the requirements:

    pip install -r requirements.txt

Run the program:

    python3 Main.py

If `python3` does not work on your system, try:

    python Main.py

## Project structure

    ANN-implementation-on-simpel-baskeball-game/
    │
    ├── Objects/
    │   ├── Basketball.py
    │   └── Hoop.py
    │
    ├── .gitignore
    ├── ANN.py
    ├── GameManager.py
    ├── Main.py
    ├── README.md
    └── requirements.txt

## Version 2.0?

In the future, a version 2.0 should either use backpropagation, or the fitness score should be determined over three multiple hoop positions.

Right now, the ANNs are training to hit a specific hoop from a specific distance, instead of training to hit any hoop from any distance.

## Author

Karl August Nørskov
