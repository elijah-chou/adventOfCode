def parse_input(input_text):
    robots = []
    for line in input_text.strip().split('\n'):
        p_part, v_part = line.split(' ')
        p_x, p_y = map(int, p_part[2:].split(','))
        v_x, v_y = map(int, v_part[2:].split(','))
        robots.append(((p_x, p_y), (v_x, v_y)))
    return robots

def simulate_robots(robots, width, height, seconds):
    positions = []
    for (p_x, p_y), (v_x, v_y) in robots:
        new_x = (p_x + v_x * seconds) % width
        new_y = (p_y + v_y * seconds) % height
        positions.append((new_x, new_y))
    return positions

def count_robots_in_quadrants(positions, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1

    return quadrants

def calculate_safety_factor(quadrants):
    factor = 1
    for count in quadrants:
        factor *= count
    return factor

def main():
    with open('2024/day14/day14input.txt', 'r') as file:
        input_text = file.read()

    robots = parse_input(input_text)
    width, height = 101, 103
    seconds = 100

    positions = simulate_robots(robots, width, height, seconds)
    quadrants = count_robots_in_quadrants(positions, width, height)
    safety_factor = calculate_safety_factor(quadrants)

    print("Safety factor:", safety_factor)

if __name__ == "__main__":
    main()