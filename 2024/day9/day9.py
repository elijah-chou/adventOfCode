def main():
    with open('2024/day9/day9input.txt') as f:
        disk_map_str = f.read().strip()
    lengths = [int(ch) for ch in disk_map_str]
    disk = []
    file_id = 0
    is_file = True
    idx = 0
    while idx < len(lengths):
        length = lengths[idx]
        if is_file:
            disk.extend([file_id] * length)
            file_id += 1
        else:
            disk.extend(['.'] * length)
        is_file = not is_file
        idx += 1

    max_file_id = file_id - 1
    # Build file positions
    file_positions = {}
    for idx, block in enumerate(disk):
        if block != '.':
            file_positions.setdefault(block, []).append(idx)
    # Move files in decreasing file ID
    for fid in range(max_file_id, -1, -1):
        positions = file_positions[fid]
        file_length = len(positions)
        file_start = positions[0]
        # Find leftmost suitable space before the file
        leftmost_pos = None
        idx = 0
        while idx < file_start:
            if disk[idx] == '.':
                # Check if there's a span of free space
                span_start = idx
                span_end = idx
                while span_end < file_start and disk[span_end] == '.':
                    span_end += 1
                span_length = span_end - span_start
                if span_length >= file_length:
                    leftmost_pos = span_start
                    break
                idx = span_end
            else:
                idx += 1
        if leftmost_pos is not None:
            # Move the file
            # Clear old positions
            for pos in positions:
                disk[pos] = '.'
            # Update positions
            new_positions = list(range(leftmost_pos, leftmost_pos + file_length))
            for pos in new_positions:
                disk[pos] = fid
            file_positions[fid] = new_positions
    checksum = sum(position * block for position, block in enumerate(disk) if block != '.')
    print(checksum)

if __name__ == '__main__':
    main()