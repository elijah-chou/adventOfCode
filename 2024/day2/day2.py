def is_safe_report(levels):
    # Initialize flags to check if the levels are strictly increasing or decreasing
    increasing = True
    decreasing = True
    
    # Iterate through the levels to check the differences between consecutive levels
    for i in range(len(levels) - 1):
        diff = int(levels[i + 1]) - int(levels[i])
        
        # If the difference is not within the range [1, 3], the report is not safe
        if not (1 <= abs(diff) <= 3):
            return False
        
        # If the difference is positive, the sequence is not strictly decreasing
        if diff > 0:
            decreasing = False
        # If the difference is negative, the sequence is not strictly increasing
        elif diff < 0:
            increasing = False
    
    # The report is safe if it is either strictly increasing or strictly decreasing
    return increasing or decreasing

def is_safe_with_dampener(levels):
    # Check if the report is already safe
    if is_safe_report(levels):
        return True
    
    # Try removing each level and check if the resulting report is safe
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_report(modified_levels):
            return True
    
    return False

def main():
    # Define the path to the input file
    file_path = 'day2input.txt'

    # Initialize a counter for safe reports
    safe_count = 0

    # Open and read the text file
    with open(file_path, mode='r') as file:
        for line in file:
            # Split the line into levels
            levels = line.strip().split(' ')
            # Check if the levels are safe with the dampener and update the counter
            if is_safe_with_dampener(levels):
                safe_count += 1

    # Print the number of safe reports
    print(f"Number of safe reports: {safe_count}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
