import re
import math

# Read the workflow and parsing rules from the file
with open("../data/19.txt", "r") as file:
    workflow, pr = file.read().split('\n\n')

# Parsing the rules using regular expressions
rules = {
    x: [r.split(':') if ':' in r else ['=', r] for r in r.split(',')
    ] for x, r in re.findall('^(\w*)\{(.*?)\}', workflow, re.M)
}
print(rules)

def accepted(tests):
    while tests:
        current_state, ranges = tests.pop()
        
        # Case A: Calculate product of the lengths
        if current_state == 'A':
            yield math.prod(len(r) + 1 for r in ranges.values())
        
        # Process rules for other cases
        elif current_state != 'R':
            for rule, next_state in rules[current_state]:
                match (*re.split('([<=>])', rule), next_state):
                    case variable, '=', number, destination_state:
                        tests.append((destination_state, ranges.copy()))
                    
                    case variable, '>', number, destination_state:
                        current_range = ranges.get(variable)
                        ranges[variable] = range(1 + max(current_range.start, int(number)), current_range.stop)
                        tests.append((destination_state, ranges.copy()))
                        ranges[variable] = range(current_range.start, min(current_range.stop, int(number)))
                    
                    case variable, '<', number, destination_state:
                        current_range = ranges.get(variable)
                        ranges[variable] = range(current_range.start, min(current_range.stop, int(number)) - 1)
                        tests.append((destination_state, ranges.copy()))
                        ranges[variable] = range(max(current_range.start, int(number)), current_range.stop)

# Initial test setup
initial_test = [('in', dict(zip('xmas', [range(1, 4000)] * 4)))]

# Calculate and print the sum
print(sum(accepted(initial_test)))
