from collections import defaultdict, deque

def parse_input(input_text):
    sections = input_text.strip().split('\n\n')
    rules_section = sections[0].split('\n')
    updates_section = sections[1].split('\n')
    
    rules = []
    for rule in rules_section:
        x, y = map(int, rule.split('|'))
        rules.append((x, y))
    
    updates = []
    for update in updates_section:
        updates.append(list(map(int, update.split(','))))
    
    return rules, updates

def is_update_correct(rules, update):
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def topological_sort(rules, update):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def main(input_text):

    # Part 1
    rules, updates = parse_input(input_text)
    correct_updates = [update for update in updates if is_update_correct(rules, update)]
    middle_pages_sum = sum(find_middle_page(update) for update in correct_updates)
    print(middle_pages_sum)

    # Part 2
    incorrect_updates = [update for update in updates if not is_update_correct(rules, update)]
    corrected_updates = [topological_sort(rules, update) for update in incorrect_updates]
    middle_pages_sum = sum(find_middle_page(update) for update in corrected_updates)
    print(middle_pages_sum)


with open('day5input.txt', 'r') as file:
    input_text = file.read()

main(input_text)