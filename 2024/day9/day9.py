def solve_disk_compaction(disk_map):
    """
    Solve the disk compaction puzzle with a memory-efficient approach.
    
    Args:
        disk_map (str): Disk map string
    
    Returns:
        int: Filesystem checksum
    """
    # Parse the disk map
    blocks = []
    i = 0
    is_file = True
    while i < len(disk_map):
        # Extract the length of current block
        j = i
        while j < len(disk_map) and disk_map[j].isdigit():
            j += 1
        
        length = int(disk_map[i:j])
        blocks.append((length, is_file))
        
        # Alternate between file and free space
        is_file = not is_file
        i = j
    
    # Track file positions and calculate checksum simultaneously
    current_free_pos = 0
    checksum = 0
    file_ids = {}
    
    for file_id, (length, is_file) in enumerate(blocks):
        if not is_file:
            # Skip free space blocks
            current_free_pos += length
            continue
        
        # Store the original starting position of this file
        original_start = current_free_pos
        file_ids[file_id] = original_start
        
        # Calculate checksum contribution for this file's blocks
        for block_offset in range(length):
            block_pos = original_start + block_offset
            checksum += block_pos * file_id
        
        # Move to next free position
        current_free_pos += length
    
    return checksum

# Example usage
print(f"Checksum for 12345: {solve_disk_compaction('12345')}")

# Puzzle input disk map
puzzle_input = "2333133121414131402"
print(f"Checksum for puzzle input: {solve_disk_compaction(puzzle_input)}")