from collections import deque

def bfs(start_x, start_y, grid):
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])
    visited = set()
    visited.add((start_x, start_y))
    queue = deque([(start_x, start_y)])
    score = 0
    
    while queue:
        x, y = queue.popleft()
        
        # If we reach a height 9, increment score
        if grid[x][y] == 9:
            score += 1
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:  # Only valid move to +1 height
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return score

def parse_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [[int(char) for char in line.strip()] for line in file]

def sum_of_scores(grid):
    rows, cols = len(grid), len(grid[0])
    total_score = 0
    
    # Find all trailheads (height 0)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                total_score += bfs(i, j, grid)
    
    return total_score

# Parse the grid from day10input.txt
grid = parse_grid_from_file('day10input.txt')

# Calculate the sum of scores
print(sum_of_scores(grid))


#######


def dfs(x, y, grid, memo):
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])
    
    # If this position has already been visited and computed, return the result
    if (x, y) in memo:
        return memo[(x, y)]
    
    # If we've reached height 9, this is a valid trail endpoint
    if grid[x][y] == 9:
        return 1
    
    # Initialize trail count to 0
    trail_count = 0
    
    # Explore the four cardinal directions
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            # Only move to cells with height exactly 1 greater than the current height
            if grid[nx][ny] == grid[x][y] + 1:
                trail_count += dfs(nx, ny, grid, memo)
    
    # Store the result in memo and return the count of trails
    memo[(x, y)] = trail_count
    return trail_count

def sum_of_ratings(grid):
    rows, cols = len(grid), len(grid[0])
    total_rating = 0
    memo = {}  # Memoization dictionary
    
    # Find all trailheads (height 0) and calculate their ratings
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:  # Start DFS from each trailhead
                total_rating += dfs(i, j, grid, memo)
    
    return total_rating

# Calculate the sum of ratings for all trailheads
print(sum_of_ratings(grid))

