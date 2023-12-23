import AOC_Helpers as util
import cProfile
profiler = cProfile.Profile()
profiler.enable()

f = util.read_file("../data/19.txt")
f = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
f = f.split("\n\n")

parts = [util.remove_all("{}", i).split(",") for i in f[1].split("\n")]

# X,M,A,S
parts = [{"xmas"[idx]: int(j[2:]) for idx, j in enumerate(i)} for i in parts]


# print(parts)

def parse_specific_input(input_str):
    # Splitting the input string into key and values
    key, values_str = input_str.split("{")
    values_str = values_str.rstrip("}")

    # Splitting values by ',' and then by ':' if present
    values = [value.split(":") if ':' in value else [value] for value in values_str.split(",")]

    return {key: parse_item(key, {key: values})}
def parse_bulk_input(input_str):
    # Splitting the input string into multiple lines
    lines = input_str.strip().split("\n")

    # Parsing each line separately
    parsed_result = {}
    for line in lines:
        key, values_str = line.split("{")
        values_str = values_str.rstrip("}")

        # Splitting values by ',' and then by ':' if present
        values = [value.split(":") if ':' in value else [value] for value in values_str.split(",")]

        parsed_result[key] = parse_item(key, {key: values})

    return parsed_result

def parse_item(item, workflows):
    def parse_branch(workflows, start_index):
        # Parses a branch starting from the given index
        # Returns the parsed branch and the index of the next unparsed element
        if start_index >= len(workflows[item]):
            return [], start_index

        entry = workflows[item][start_index]
        if len(entry) == 1:
            # Single item (no condition), return as is
            return entry[0], start_index + 1
        else:
            # Condition with true and false branches
            condition, true_action = entry
            # True branch is simple
            true_branch = [true_action]
            # Parse the false branch starting from the next element
            false_branch, next_index = parse_branch(workflows, start_index + 1)
            return [condition, true_branch, false_branch], next_index

    result, _ = parse_branch(workflows, 0)
    return result


workflows = parse_bulk_input(f[0])
print(workflows)


def list_contains(a, b):
    try:
        return a in b
    except:
        return False


def is_expression(e):
    return "<" in e or ">" in e


def do_lt_gt(exp, part):
    if "<" in exp:
        try:
            value = int(exp.split("<")[1])
            return part[exp[0]] < value
        except ValueError:
            return f"Malformed expression: {exp}"
    elif ">" in exp:
        try:
            value = int(exp.split(">")[1])
            return part[exp[0]] > value
        except ValueError:
            return f"Malformed expression: {exp}"
    else:
        return f"Invalid expression: {exp}"


def evaluate_workflow(expression, part):
    #print("EXP",expression[0])
    if list_contains(expression[0], list(workflows.keys())):
        return expression[0]
    if expression[0] == "A" or expression[0] == "R":
        return expression[0]
    if expression == "A" or expression == "R":
        return expression[0]
    if list_contains(expression, list(workflows.keys())):
        return expression

    if len(expression) == 1:
        return expression[0]

    if do_lt_gt(expression[0], part):
        return evaluate_workflow(expression[1], part)
    else:
        return evaluate_workflow(expression[2], part)

def solve_p1():
    overall = 0
    for part in parts:
        # print(part)
        # get initial result of workflow
        result = evaluate_workflow(workflows["in"], part)
        # print(result)
        # check if done on first try
        done = result == "A" or result == "R"
        # loop while not done
        while done == False:
            # get next expression result
            result = evaluate_workflow(workflows[result], part)
           #print(result)
            # print(result)
            done = result == "A" or result == "R"

        if result == "A":
            #print("XMAS", list(part.values()))
            for xmas in list(part.values()):
                overall += xmas
    print(overall)
def split_range(current, split, is_less_than):
    """
    Split a given range into two parts based on a split value.

    Args:
    current (tuple[int, int]): The current range as a tuple (low, high).
    split (int): The value to split the range at.
    is_less_than (bool): Flag indicating the comparison operation.
        - If True, compares with 'val < split'.
        - If False, compares with 'val > split'.

    Returns:
    tuple[tuple[int, int], tuple[int, int]]: Two ranges resulting from the split.
        - pos1 contains values where the condition evaluates to False.
        - pos2 contains values where the condition evaluates to True.
    """
    low, high = current

    if is_less_than:
        # For 'val < split', pos1 contains values >= split
        pos1 = (split, high)
        # pos2 contains values < split
        pos2 = (low, split - 1)
    else:
        # For 'val > split', pos1 contains values <= split
        pos1 = (low, split)
        # pos2 contains values > split
        pos2 = (split + 1, high)

    # Ensure the ranges are within the original bounds
    pos1 = (max(low, pos1[0]), min(high, pos1[1]))
    pos2 = (max(low, pos2[0]), min(high, pos2[1]))

    return pos1, pos2

def count_ranges(this_range,workflow_name,workflow):
    if workflow_name == "R":
        return 0
    elif workflow_name == "A":
        print("accepted ranges:",this_range)
        
def solve_p2():
    """finds all ranges that return A"""
    current_workflow = workflows["in"]

print(split_range((5,10),7,is_less_than=False))

# 7 > 7

profiler.disable()
#profiler.print_stats(sort='cumulative')
