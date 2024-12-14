from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_equation_true(test_value, numbers):
    possible_operators = ['+', '*', '||']
    for operators in product(possible_operators, repeat=len(numbers) - 1):
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

def total_calibration_result(equations):
    total = 0
    for equation in equations:
        test_value, numbers = equation
        if is_equation_true(test_value, numbers):
            total += test_value
    return total

def read_equations_from_file(filename):
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split(':')
            test_value = int(parts[0].strip())
            numbers = list(map(int, parts[1].strip().split()))
            equations.append((test_value, numbers))
    return equations

# Read equations from the input file
equations = read_equations_from_file('day7input.txt')

print(total_calibration_result(equations))