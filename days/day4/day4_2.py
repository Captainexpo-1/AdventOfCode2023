file: str = open("./../data/four.txt", "r").read()
test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
use_test = False
f = test if use_test else file


def count_cards(ls):
    t = [0] * (len(ls))
    for i in ls:
        a = i.replace(" ", "").replace("Card", "")
        current_num = int(a[:a.find(":")])
        print(int(a[:a.find(":")]), end=" ")
        t[current_num - 1] += 1
    print("\r")
result = 0

preload = [0]*len(f.split("\n"))

def getNums(n):
  o = []
  for i in n:
    try:
      int(i.replace(" ", ""))
      o.append(int(i))
    except:
      continue
  return o


def has_num(num, our):
  try:
    if (our.index(num) != -1):
      return True
  except:
    return False
  """
    for i in our:
        if i == num:
            return True
    return False
    """


def find_card(num, ar):
  for idx, i in enumerate(ar):
    a = i.replace(" ", "").replace("Card", "")
    if int(a[:a.find(":")]) == num: return idx
  return -1

for line in f.split("\n"):
    a = line.replace(" ", "").replace("Card", "")
    current_num = int(a[:a.find(":")])
    string_to_use = line[line.find(":") + 2:].replace("  ", " ")
    winning_nums = getNums(string_to_use[:string_to_use.find("|") - 1].replace(
        "  ", " ").split(" "))
    our_nums = getNums(string_to_use[string_to_use.find("|") + 2:].split(" "))
    count = 0
    for j in winning_nums:
        if has_num(j,our_nums):
            count+=1
    preload[current_num-1] = count
print(preload)
quit()

f = f.split("\n")
idx = 0
while idx < len(f):

    line = f[idx]
    try:
      a = line.replace(" ", "").replace("Card", "")
      current_num = int(a[:a.find(":")])
    except:
      print(line.replace(" ", "").replace("Card", ""), "WOHOO", line)
      quit()
    current = preload[current_num-1]
    """
    string_to_use = line[line.find(":") + 2:].replace("  ", " ")
    our_nums = getNums(string_to_use[string_to_use.find("|") + 2:].split(" "))
    winning_nums = getNums(string_to_use[:string_to_use.find("|") - 1].replace(
        "  ", " ").split(" "))
    for number in winning_nums:
      if has_num(number, our_nums):
        current += 1
    """
    for j in range(current):
      found = find_card(current_num + j + 1, f)
      #print("FOUND",found,current_num+j+1)
      f.insert(found, f[found])
    count_cards(f)
    #print(current, line, len(f))
    if idx == 999:
      #quit()
      pass
    idx += 1
    print(len(f), "Current Num:", current_num, end="\r", flush=False)

result = len(f)
print("\n\n\n\n\n\n\n\n",result)
