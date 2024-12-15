def parse_map(map_str):
    map_lines = map_str.strip().split('\n')
    map_grid = [list(line) for line in map_lines]
    return map_grid

def find_guard(map_grid):
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    for y, row in enumerate(map_grid):
        for x, cell in enumerate(row):
            if cell in directions:
                return (x, y), directions[cell]
    return None, None

def turn_right(direction):
    turns = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    return turns[direction]

def move_guard(map_grid, start_pos, start_dir):
    x, y = start_pos
    direction = start_dir
    visited = set()
    visited.add((x, y))
    direction_changes = []

    while True:
        next_x, next_y = x + direction[0], y + direction[1]
        if not (0 <= next_x < len(map_grid[0]) and 0 <= next_y < len(map_grid)):
            break
        if map_grid[next_y][next_x] == '#':
            direction = turn_right(direction)
            direction_changes.append((x, y))
        else:
            x, y = next_x, next_y
            visited.add((x, y))
    
    return visited, direction_changes

def count_visited_positions(map_str):
    map_grid = parse_map(map_str)
    start_pos, start_dir = find_guard(map_grid)
    visited_positions, _ = move_guard(map_grid, start_pos, start_dir)
    return len(visited_positions)

def count_loop_positions(map_str):
    map_grid = parse_map(map_str)
    start_pos, start_dir = find_guard(map_grid)
    visited_positions, direction_changes = move_guard(map_grid, start_pos, start_dir)
    
    loop_positions = set()
    for pos in direction_changes:
        if pos == start_pos:
            continue
        x, y = pos
        map_grid[y][x] = '#'
        new_visited_positions, _ = move_guard(map_grid, start_pos, start_dir)
        if len(new_visited_positions) < len(visited_positions):
            loop_positions.add(pos)
        map_grid[y][x] = '.'
    
    return len(loop_positions)

# Example usage
with open('day6input.txt', 'r') as file:
    map_str = file.read()
    
print(count_visited_positions(map_str))
print(count_loop_positions(map_str))