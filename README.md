# MDP Maze Exploration & Traversal

A Python-based robot maze exploration and pathfinding simulator designed for MDP (Multi-Disciplinary Project) robotic competitions. The simulator allows a virtual robot to explore an unknown maze environment, discover obstacles through sensors, and find the fastest path to a goal destination.

## Features

- **Interactive GUI Simulator**: Visual tkinter-based interface to watch the robot explore and navigate the maze in real-time
- **Multiple Exploration Algorithms**:
  - Left Wall Hugging (default)
  - Spelunking (targeted exploration of unreachable areas)
  - Image Recognition mode for obstacle detection
- **Advanced Pathfinding**: A* algorithm with support for both 4-way (orthogonal) and 8-way (diagonal) movement
- **Flexible Configuration**: Customizable coverage goals, time limits, and exploration strategies
- **Map Management**: Dynamic map with explored/unexplored tracking, obstacle detection, and map descriptor encoding/decoding
- **Sensor Simulation**: Simulates multiple sensors (front-left, front-middle, front-right, left-front, left-middle, right) with configurable ranges

## Project Structure

```
.
├── main.py                 # Entry point for the simulator
├── simulator.py            # GUI simulator with tkinter
├── core.py                 # Core orchestration for exploration and pathfinding
├── robot.py                # Robot base class with position, bearing, and sensor data
├── simulated_robot.py      # Simulated robot implementation
├── real_robot.py           # Real robot interface (for physical robot)
├── map.py                  # Map management with multiple layers
├── exploration_algo.py     # Exploration algorithms implementation
├── fastest_path_algo.py    # A* pathfinding algorithm
├── handler.py              # Handles communication between components
├── comms.py                # Communication protocols
├── config.py               # Configuration settings (map size, sensors, images)
├── constants.py            # Constants and enumerations
├── utils.py                # Utility functions
└── images/                 # Image assets for GUI
```

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- Standard library modules: `time`, `logging`, `argparse`, `queue`, `threading`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SeaBoiii/mdp-maze-exploration-traversal.git
cd mdp-maze-exploration-traversal
```

2. Ensure Python 3.x is installed:
```bash
python --version
```

3. Run the simulator:
```bash
python main.py
```

## Usage

### Basic Usage

Run the simulator with default settings:
```bash
python main.py
```

Run with verbose debug logging:
```bash
python main.py --verbose
```

or

```bash
python main.py -v
```

### GUI Controls

The simulator provides an interactive control panel where you can:
- Configure exploration parameters (coverage %, time limit, steps per second)
- Select exploration algorithms
- Set goal and waypoint coordinates for fastest path
- Load custom map configurations
- View real-time robot movement and map updates

### Map Configuration

The default map is a 20×15 grid (height × width). The robot starts at position (1, 18) facing North.

You can configure custom maps by editing `config.py` or loading map descriptors through the GUI.

## Algorithms

### Exploration Algorithms

1. **Left Wall Hugging**: The robot follows the left wall while exploring, checking for obstacles in front and to the left. This is a systematic approach that guarantees complete exploration in simply-connected mazes.

2. **Spelunking**: Targeted exploration strategy that identifies unreachable areas and finds adjacent free spaces to reach them. Useful for maximizing coverage in complex maze layouts.

3. **Image Recognition**: Special mode where the robot captures obstacle positions for image recognition tasks. Supports both full and partial IR coverage modes.

### Pathfinding Algorithm

**A* (A-Star)**: Efficient pathfinding algorithm that finds the optimal path from start to goal.
- Supports waypoints for multi-point navigation
- Two movement modes:
  - 4-way: Orthogonal movement only (up, down, left, right)
  - 8-way: Includes diagonal movement for shorter paths
- Cost-based optimization considering turns and movement

## Configuration

Key configuration parameters in `config.py`:

- **Map Size**: 20×15 grid (height × width)
- **Sensor Ranges**: 
  - Front sensors: 3 cells
  - Left sensors: 3 cells
  - Right sensor: 5 cells
- **Robot Starting Position**: (1, 18) facing North

## Development

### Component Overview

- **Robot**: Manages position, bearing (direction), and sensor data. Handles movement commands (forward, turn left/right, diagonal).
- **Map**: Maintains three map layers (explored status, simulation map, virtual map) for tracking obstacles and exploration progress.
- **Explorer**: Implements exploration strategies to discover the maze.
- **Fastest Path**: Computes optimal routes using A* algorithm.
- **Core**: Orchestrates the exploration and pathfinding phases.
- **Handler**: Bridges communication between GUI, robot, and algorithms.

### Extending the Simulator

To add new exploration algorithms:
1. Implement the algorithm in `exploration_algo.py`
2. Add algorithm type to constants
3. Update the GUI to include the new option

To modify pathfinding:
1. Edit `fastest_path_algo.py`
2. Adjust cost functions or movement rules

## License

This project is open-source and available for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Authors

Developed for MDP (Multi-Disciplinary Project) robotic competitions.
