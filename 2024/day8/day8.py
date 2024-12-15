def parse_map(map_lines):
    antennas = []
    grid_height = len(map_lines)
    grid_width = len(map_lines[0])
    for y, line in enumerate(map_lines):
        for x, char in enumerate(line):
            if char != '.':
                antennas.append((x, y, char))
    return antennas, grid_width, grid_height

def compute_antinodes(antennas, grid_width, grid_height):
    antinodes = set()
    for i in range(len(antennas)):
        x1, y1, freq1 = antennas[i]
        for j in range(i + 1, len(antennas)):
            x2, y2, freq2 = antennas[j]
            if freq1 != freq2:
                continue
            dx = x2 - x1
            dy = y2 - y1
            distance = ((dx) ** 2 + (dy) ** 2) ** 0.5
            if distance == 0:
                continue
            # Antinodes between antennas
            for ratio in [1 / 3, 2 / 3]:
                ax = x1 + dx * ratio
                ay = y1 + dy * ratio
                if 0 <= ax < grid_width and 0 <= ay < grid_height:
                    antinodes.add((int(ax), int(ay)))
            # Antinodes beyond antennas
            for k in [-1, 1]:
                ax = x1 - dx * k
                ay = y1 - dy * k
                if 0 <= ax < grid_width and 0 <= ay < grid_height:
                    antinodes.add((int(ax), int(ay)))
    return antinodes

def main():
    with open('day8input.txt', 'r') as f:
        map_lines = [line.strip() for line in f]
    antennas, grid_width, grid_height = parse_map(map_lines)
    antinodes = compute_antinodes(antennas, grid_width, grid_height)
    print(len(antinodes))

if __name__ == "__main__":
    main()