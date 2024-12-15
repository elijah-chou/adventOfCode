def parse_input(input_text):
    lines = input_text.strip().split('\n')
    warehouse = [list(line) for line in lines[:-1]]
    moves = lines[-1].replace('\n', '')
    return warehouse, moves

def find_robot(warehouse):
    for y, row in enumerate(warehouse):
        for x, cell in enumerate(row):
            if cell == '@':
                return x, y
    return None

def move_robot(warehouse, robot_pos, direction):
    x, y = robot_pos
    dx, dy = direction
    new_x, new_y = x + dx, y + dy

    if warehouse[new_y][new_x] == '#':
        return robot_pos  # Hit a wall, no movement

    if warehouse[new_y][new_x] == 'O':
        box_x, box_y = new_x + dx, new_y + dy
        if warehouse[box_y][box_x] in ['#', 'O']:
            return robot_pos  # Box can't move, no movement
        warehouse[box_y][box_x] = 'O'
        warehouse[new_y][new_x] = '@'
        warehouse[y][x] = '.'
        return new_x, new_y

    warehouse[new_y][new_x] = '@'
    warehouse[y][x] = '.'
    return new_x, new_y

def simulate_warehouse(warehouse, moves):
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    robot_pos = find_robot(warehouse)

    for move in moves:
        direction = directions[move]
        robot_pos = move_robot(warehouse, robot_pos, direction)

    return warehouse

def calculate_gps_sum(warehouse):
    gps_sum = 0
    for y, row in enumerate(warehouse):
        for x, cell in enumerate(row):
            if cell == 'O':
                gps_sum += 100 * y + x
    return gps_sum

def main():
    with open('2024/day15/day15input.txt', 'r') as file:
        input_text = file.read()

    warehouse, moves = parse_input(input_text)
    warehouse = simulate_warehouse(warehouse, moves)
    gps_sum = calculate_gps_sum(warehouse)

    print("Sum of all boxes' GPS coordinates:", gps_sum)

if __name__ == "__main__":
    main()