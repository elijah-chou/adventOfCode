import re

def find_valid_instructions(memory):
    # Regular expression to find valid mul(X,Y), do(), and don't() instructions
    pattern = re.compile(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))')
    matches = pattern.findall(memory)
    return matches

def calculate_sum_of_multiplications(matches):
    total_sum = 0
    mul_enabled = True  # Initially, mul instructions are enabled
    
    for match in matches:
        mul_instruction, x, y, do_instruction, dont_instruction = match
        if do_instruction:
            mul_enabled = True
        elif dont_instruction:
            mul_enabled = False
        elif mul_enabled and mul_instruction:
            x, y = int(x), int(y)
            total_sum += x * y
    
    return total_sum

def main():
    # Read the input from day3input.txt
    with open('day3input.txt', 'r') as file:
        memory = file.read()
    
    # Find all valid instructions
    matches = find_valid_instructions(memory)
    print(matches)
    
    # Calculate the sum of all enabled multiplications
    result = calculate_sum_of_multiplications(matches)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()