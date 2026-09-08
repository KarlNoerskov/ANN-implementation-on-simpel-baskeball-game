# Artificial Neural Network used on a simple basketball game

An artificial neural network (ANN) used on a simple basketball game.

The ANN trains using neuro-evolution. From generation to generation, the ANN with the best fitness score is selected and randomly mutated by a small amount.

In this implementation, 500 ANNs are running at the same time. Each generation runs for 400 frames before the fitness scores are compared and the next generation is created.

![ANN playing the basketball game](https://github.com/user-attachments/assets/7281f8f3-df9b-4f9e-a064-3729cbacd7d4)

## How it works

Each generation starts with 500 ANNs.

The ANNs all play the game for 400 frames. After the 400 frames, each ANN gets a fitness score based on how well it performed.

The ANN with the highest fitness score is then selected. This ANN is copied and the copies are randomly mutated by a small amount to create the next generation.

This process is repeated over and over, allowing the ANN to gradually improve its performance.

The basic process is:

1. Create 500 ANNs.
2. Run each ANN for 400 frames.
3. Calculate the fitness score for each ANN.
4. Select the ANN with the highest fitness score.
5. Copy the best ANN.
6. Randomly mutate the copies.
7. Use the mutated ANNs as the next generation.
8. Repeat.

## Training

The current implementation uses:

- 500 ANNs per generation
- 400 frames per generation
- Neuro-evolution
- Fitness-based selection
- Random mutation

The ANN is not trained using backpropagation. Instead, the weights of the network are changed through random mutations and the network that perform better are kept for the next generation.

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
