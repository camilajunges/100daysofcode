def solve_maze(maze, start, end):
    """
    Solves a maze using a simple depth-first search (DFS) algorithm.
    This version uses a simple while loop and a list as a stack.
    
    Args:
        maze (list of lists): The maze grid, where 1 is a wall and 0 is a path.
        start (tuple): The (row, col) starting coordinates.
        end (tuple): The (row, col) ending coordinates.
        
    Returns:
        list of tuples or None: A list of coordinates representing the path,
                                or None if no path is found.
    """
    stack = [start]
    visited = {start}
    path_history = {start: None}

    while stack:
        current_pos = stack.pop()
        if current_pos == end:
            path = []
            while current_pos is not None:
                path.append(current_pos)
                current_pos = path_history[current_pos]
            path.reverse()
            return path
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = current_pos[0] + dr, current_pos[1] + dc
            next_pos = (next_row, next_col)
            if is_valid_move(next_pos, maze, visited):
                stack.append(next_pos)
                visited.add(next_pos)
                path_history[next_pos] = current_pos
    return None

def is_valid_move(pos, maze, visited):
    """
    Checks if a position is a valid spot to move to.
    
    Args:
        pos (tuple): The (row, col) coordinates to check.
        maze (list of lists): The maze grid.
        visited (set): The set of visited coordinates.
        
    Returns:
        bool: True if the move is valid, False otherwise.
    """
    row, col = pos
    rows, cols = len(maze), len(maze[0])
    
    if not (0 <= row < rows and 0 <= col < cols):
        return False
    
    if maze[row][col] == 1:
        return False
    
    if pos in visited:
        return False
    return True

maze_grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
]

start_position = (1, 1)
end_position = (19, 18)

solution_path = solve_maze(maze_grid, start_position, end_position)

if solution_path:
    print("A path was found!")
    for i, (row, col) in enumerate(solution_path):
        print(f"Step {i+1}: Go to ({row}, {col})")
else:
    print("No path found to the end of the maze.")
