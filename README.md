# PuzzleSolver

### Background
Originally a part of the Introduction to Artificial Intelligence course at UCR (CS170), this project started as a C++ implementation and has since evolved. It now includes Python versions of the algorithms and a web interface for visualizing puzzle solutions.

### Description
The Advanced Puzzle Solver project focuses on efficient algorithms for solving the Eight Piece Puzzle and its larger variations. Three algorithms were implemented and tested:

#### Key Features

- **Uniform Cost Search**: Expands nodes based on cost, resembling a breadth-first search for uniform costs. Memory-intensive for complex puzzles.
- **A\* with Misplaced Tile Heuristic**: Evaluates cost based on depth and misplaced tiles, using tree data structures for efficient performance.
- **A\* with Euclidean Distance Heuristic**: Employs Euclidean distance to calculate costs, significantly reducing search costs.

#### Key Findings
- The A* algorithms were more efficient and less memory-intensive compared to Uniform Cost Search, especially for complex puzzles.
- The success of the A* algorithms was attributed to their consideration of both transition costs and cumulative costs.

### Author's Note
This project is an exploration of AI principles and their application in solving complex puzzles. It showcases the transition from theoretical algorithms to practical, user-friendly web applications.

### Web Visualization
Navigate to PuzzleSolver and explore the interactive web interface that visually demonstrates the efficiency and effectiveness of the implemented algorithms in solving complex puzzles. The interface allows users to input puzzle configurations, select an algorithm, and view the step-by-step solution process. (More details to be added)

### Local Exploration
For those interested in diving deeper into the algorithms, the C++ and Python versions are available within this repository. You can explore these files locally to understand the algorithms' functionality in more detail:

- C++ files: Navigate to the `algorithms_cpp` directory.
- Python files: Explore the `algorithms_py` directory.

Feel free to experiment with different puzzle configurations and observe how each algorithm tackles the problem.

### Author
Majd Kawak