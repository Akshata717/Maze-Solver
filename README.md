# Maze-Solver
Maze Solver - Python
This Python project generates and solves 2D grid-based mazes with random obstacles.

## Features

- Generates a 9x9 maze with random obstacles, start (`S`), and end (`E`) points.
- Implements **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to explore valid paths.
- Tracks visited cells to avoid revisiting positions.
- Reconstructs and visualizes the solution path from start to end using backtracking.

## Example Output

  S 0 X 0 0 0 X 0 0
  * * X 0 X 0 X 0 0
  X * 0 0 0 0 0 0 X
  0 * 0 0 0 0 0 0 0
  X * 0 0 0 0 X 0 0
  0 * 0 X X 0 0 X 0
  0 * 0 0 0 X X 0 X
  0 * * * E 0 X 0 0
  0 0 X 0 0 0 0 0 0
