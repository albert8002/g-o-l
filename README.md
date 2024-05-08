# Game of Life Simulation

This Python script implements Conway's Game of Life, a cellular automaton devised by the mathematician John Conway. The Game of Life is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. Despite its simplicity, the Game of Life exhibits complex behavior and is Turing complete.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- Seaborn

## Usage

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Run the script using the following command:

```bash
python3 main.py
```
## Description

The script defines two classes: `Generate` and `Animate`. Here's a brief overview of each:

### Generate Class

- **canvas(self: int) -> np.ndarray[int]:** Returns a numpy array initialized with zeros, representing the canvas/grid for the Game of Life simulation.

- **neighbours_sum(self: list[int], args: np.ndarray[int]) -> int:** Calculates the sum of neighbors for a given cell on the canvas.

- **next_gen(self: np.ndarray[int]) -> np.ndarray[int]:** Computes the next generation of cells based on the rules of the Game of Life.

- **position(self: np.ndarray[int]) -> np.ndarray[int]:** Initializes the canvas/grid with predefined starting positions for the simulation.

### Animate Class

- **plot(self: np.ndarray[int]) -> None:** Plots the current state of the canvas using Seaborn's heatmap.

- **run(self: int):** Executes a single iteration of the simulation, updating the canvas and plotting the result.

- **exec(self: str, args: int, interval: int = 100):** Executes the simulation for the specified number of frames and saves the result as an MP4 video file.

## Example

The main section of the script initializes the canvas/grid, defines the number of frames for the animation, and executes the simulation.

```python
if __name__ == '__main__':
    Animate.exec('anim.mp4', frames)