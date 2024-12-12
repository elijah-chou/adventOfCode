# Part 1
def count_xmas_occurrences(grid):
    word = "XMAS"
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1), # down-left
        (0, -1), # left
        (-1, 0), # up
        (-1, -1),# up-left
        (-1, 1)  # up-right
    ]
    
    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True
    
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1
    
    return count

# Read the grid from day4input.txt
with open('day4input.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

print(count_xmas_occurrences(grid))

# Part 2
def count_x_mas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    def search_pattern(x, y):
        # Check the main diagonal (top-left to bottom-right)
        main_diag = (grid[x][y], grid[x+1][y+1], grid[x+2][y+2])
        anti_diag = (grid[x][y+2], grid[x+1][y+1], grid[x+2][y])
        
        if (main_diag == ('M', 'A', 'S') or main_diag == ('S', 'A', 'M')) and \
           (anti_diag == ('M', 'A', 'S') or anti_diag == ('S', 'A', 'M')):
            return True
        return False
    
    count = 0
    for x in range(rows - 2):
        for y in range(cols - 2):
            if search_pattern(x, y):
                count += 1
    
    return count

# Read the grid from day4input.txt
with open('day4input.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

print(count_x_mas_occurrences(grid))