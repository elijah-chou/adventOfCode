def find_region(map_data, x, y, visited):
    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    region = []
    plant_type = map_data[x][y]

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) not in visited:
            visited.add((cx, cy))
            region.append((cx, cy))
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(map_data) and 0 <= ny < len(map_data[0]):
                    if map_data[nx][ny] == plant_type and (nx, ny) not in visited:
                        stack.append((nx, ny))
    
    return region

def calculate_sides(region, map_data):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sides = 0

    for x, y in region:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < len(map_data) and 0 <= ny < len(map_data[0]) and map_data[nx][ny] == map_data[x][y]):
                sides += 1

    return sides

def calculate_total_price(map_data):
    visited = set()
    total_price = 0

    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if (i, j) not in visited:
                region = find_region(map_data, i, j, visited)
                area = len(region)
                sides = calculate_sides(region, map_data)
                price = area * sides
                total_price += price

    return total_price

# Example map
map_data = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE"
]

# Convert map data to a list of lists
map_data = [list(row) for row in map_data]

# Calculate total price
total_price = calculate_total_price(map_data)
print("Total price:", total_price)
