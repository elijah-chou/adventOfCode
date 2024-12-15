import re

def parse_input(input_text):
    machines = []
    entries = input_text.strip().split('\n\n')
    for entry in entries:
        lines = entry.strip().split('\n')
        machine = {}
        for line in lines:
            if line.startswith('Button A'):
                vals = re.findall(r'X\+(\d+), Y\+(\d+)', line)[0]
                machine['A_x'] = int(vals[0])
                machine['A_y'] = int(vals[1])
            elif line.startswith('Button B'):
                vals = re.findall(r'X\+(\d+), Y\+(\d+)', line)[0]
                machine['B_x'] = int(vals[0])
                machine['B_y'] = int(vals[1])
            elif line.startswith('Prize'):
                vals = re.findall(r'X=(\d+), Y=(\d+)', line)[0]
                machine['P_x'] = int(vals[0]) + 10000000000000
                machine['P_y'] = int(vals[1]) + 10000000000000
        machines.append(machine)
    return machines

def solve_machine(machine):
    A_x, A_y = machine['A_x'], machine['A_y']
    B_x, B_y = machine['B_x'], machine['B_y']
    P_x, P_y = machine['P_x'], machine['P_y']
    D = A_x * B_y - A_y * B_x
    if D == 0:
        # Check if the system is consistent
        if A_x * P_y - A_y * P_x == 0 and B_x * P_y - B_y * P_x == 0:
            # Infinite solutions, find minimal non-negative solution
            for b in range(0, 100000):
                num = P_x - b * B_x
                if num % A_x == 0:
                    a = num // A_x
                    if a >= 0:
                        tokens = a * 3 + b * 1
                        return tokens
            return None
        else:
            return None
    else:
        numerator_b = A_x * P_y - A_y * P_x
        if numerator_b % D != 0:
            return None
        b = numerator_b // D
        if b < 0:
            return None
        numerator_a = P_x - b * B_x
        if numerator_a % A_x != 0:
            return None
        a = numerator_a // A_x
        if a < 0:
            return None
        tokens = a * 3 + b * 1
        return tokens

def main():
    with open('day13input.txt', 'r') as f:
        input_text = f.read()
    machines = parse_input(input_text)
    total_tokens = 0
    for machine in machines:
        tokens = solve_machine(machine)
        if tokens is not None:
            total_tokens += tokens
    print(f"The fewest tokens you would have to spend to win all possible prizes is {total_tokens}.")

if __name__ == "__main__":
    main()