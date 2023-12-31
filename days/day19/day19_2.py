
import re, json, math

f =open("../data/19.txt","r").read()
fm = """px{a<2006:qkq,m>2090:A,rfg}
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
workflow, parts = f.split("\n\n")

def split_all(string: str, vals: list[chr] | str, remove_vals: bool=False):
    split = re.split(f"([{''.join(vals)}])",string)
    new = []
    for i in split: 
        if remove_vals :
            if (i not in vals):
                new.append(i)
        else:
            new.append(i)
    return new
rules = {
    x: [r.split(':') if ':' in r else ['=', r] for r in r.split(',')
    ] for x, r in re.findall('^(\w*)\{(.*?)\}', workflow, re.M)
}
#print(json.dumps(rules, indent=4))

def get_all_accepted_workflows(tests_to_run):
    while tests_to_run:
        current_state, ranges = tests_to_run.pop()
        
        # Case A: Calculate product of the lengths
        if current_state == 'A':
            yield math.prod(len(r) + 1 for r in ranges.values())
        
        # Process rules for other cases
        elif current_state != 'R':
            for rule, next_state in rules[current_state]:
                splitted = split_all(rule,"<>=")

                match (*splitted,next_state):
                    case variable, '=', number, destination_state:
                        tests_to_run.append((destination_state,ranges.copy()))

                    case variable, '>', number, destination_state:
                        current_range = ranges.get(variable)
                        ranges[variable] = range(1 + max(current_range.start, int(number)), current_range.stop)
                        tests_to_run.append((destination_state, ranges.copy()))
                        ranges[variable] = range(current_range.start, min(current_range.stop, int(number)))
                    
                    case variable, '<', number, destination_state:
                        current_range = ranges.get(variable)
                        ranges[variable] = range(current_range.start, min(current_range.stop, int(number)) - 1)
                        tests_to_run.append((destination_state, ranges.copy()))
                        ranges[variable] = range(max(current_range.start, int(number)), current_range.stop)

                    


accepted = get_all_accepted_workflows([("in", dict(zip("xmas", [range(1, 4000)] * 4)))])

print(sum(accepted))