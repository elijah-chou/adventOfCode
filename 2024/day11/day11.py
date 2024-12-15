def transform(stone):
    # Rule 1: If the stone is 0, it becomes 1
    if stone == 0:
        return [1]
    
    # Rule 2: If the stone has an even number of digits, split it
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]
    
    # Rule 3: Otherwise, multiply the stone by 2024
    return [stone * 2024]

def blink(stones):
    new_stones = []
    for stone in stones:
        new_stones.extend(transform(stone))
    return new_stones

# Initial arrangement of stones
stones = [6, 11, 33023, 4134, 564, 0, 8922422, 688775]

# Perform 25 blinks
for _ in range(75):
    stones = blink(stones)

# The number of stones after 25 blinks
print(len(stones))
