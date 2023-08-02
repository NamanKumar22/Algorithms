def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(x, y):
        if [x, y] == destination:
            return True
        if visited[x][y]:
            return False

        visited[x][y] = True
        # Check for possible moves: up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] != 1:
                nx += dx
                ny += dy
            if dfs(nx, ny):
                return True
        return False
    return dfs(start[0], start[1])
# Test data
maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0]]
start = [4, 3]
destination = [0, 1]

print(hasPath(maze, start, destination))  # Output: True
