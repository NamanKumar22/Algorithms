**Description**
This repository contains the solution to Leetcode problem 490 - "The Maze." The problem requires finding a valid path from the starting point to the destination in a given maze, where a ball can roll in four cardinal directions until it hits a wall. The maze is represented as a 2D grid, with walls denoted as 1 and open paths as 0.

**Solution Approach**
The solution to the "Maze" problem is implemented using Depth-First Search (DFS) with backtracking. The algorithm explores potential paths in the maze and marks visited cells to prevent cycles. The DFS approach allows the algorithm to search through multiple paths efficiently until it reaches the destination or finds that there is no valid path.

**Implementation**
The solution is written in Python and encapsulated in a function hasPath(maze, start, destination). The function takes three parameters: maze, the 2D grid representing the maze; start, a tuple with the starting point coordinates; and destination, a tuple with the destination point coordinates.

Refer the Maze-DFS.py file for the running code and the Powerpoint Presentation for the detailed report of the Project.
