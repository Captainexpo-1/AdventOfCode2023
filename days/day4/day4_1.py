file: str = open("../data/four.txt","r").read()
test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
use_test = False
f = test if use_test else file

result = 0
def getNums(n):
    o=[]
    for i in n:
        try:
            int(i.replace(" ", ""))
            o.append(int(i))
        except:
            continue
    return o
def has_num(num,our):
    try:
        if(our.index(num) != -1):
            return True
    except: return False

    """
    for i in our:
        if i == num:
            return True
    return False
    """
for idx,line in enumerate(f.split("\n")):
    current = 0
    string_to_use = line[line.find(":")+2:].replace("  ", " ")
    our_nums = getNums(string_to_use[string_to_use.find("|")+2:].split(" "))
    winning_nums = getNums(string_to_use[:string_to_use.find("|")-1].replace("  ", " ").split(" "))
    for number in winning_nums:
        if has_num(number, our_nums):
            if current == 0:
                current = 1
            else:
                current *= 2
   # print(idx+1,winning_nums,our_nums)
    result += current




print(result)