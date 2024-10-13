# Turing Machine Simulator

This project is an interactive **Turing Machine Simulator** built using Python's `tkinter` library. It visually simulates the behavior of a Turing machine, allowing users to load input, compile machine instructions, and see the machine process step-by-step.

## Features
- **Input loading**: Users can load a sequence of characters that the Turing machine will process.
- **State transitions visualization**: The simulator displays the machine's tape and head movements as it processes the input based on the given instructions.
- **Custom Turing machines**: Users can write their own machine instructions and compile them directly into the simulator.
- **Control buttons**: Start, pause, and stop the simulation, along with adjustable speed control.
- **Output display**: The machine will either accept or reject the input based on the defined states and transitions.

## How It Works
1. **Load Input**: You can input a string into the provided text box and press the "Load" button. This input will be displayed on the Turing machine's tape.
2. **Write Instructions**: Define the Turing machine in the provided text area with specific transitions and states.
3. **Compile Instructions**: Press the "Compile" button to process and validate your instructions.
4. **Run Simulation**: Press "Run" to start the machine. The tape will be updated step by step, showing how the machine processes the input.
5. **Pause or Cancel**: You can pause the simulation or cancel it at any time using the provided buttons.
6. **Adjust Speed**: Use the speed slider to control how fast the Turing machine runs.

## Instructions Syntax
1. **Machine Name**: The first line should define the machine's name.
2. **Initial State**: The second line defines the initial state.
3. **Accept State**: The third line defines the accepting state.
4. **Transitions**: Subsequent lines define the transition rules. Each transition consists of:
- Current state and symbol on tape
- Next state, symbol to write, and head direction (left `<`, right `>`)

## Controls
- **Load**: Loads the input string onto the tape.
- **Compile**: Compiles the Turing machine instructions into the simulator.
- **Run**: Starts the machine. The machine will process the input string based on the compiled instructions.
- **Pause**: Pauses the machine during its execution.
- **Cancel**: Stops the machine's execution and resets the interface.
- **Speed Slider**: Adjusts the simulation speed.

## Prerequisites
- Python 3.x
- Tkinter (Comes pre-installed with most Python distributions)

## Installation & Running
To run the simulator, follow these steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/turing-machine-simulator.git
   ```
2. Navigate to the project directory:
   ```bash
    cd Turing_Machine_Simulator
   ```
3. Run the program:
   ```bash
   python3 app.py
   ```

