f = open("../data/two.txt", "r").read()
a = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

result = 0
for idx,line in enumerate(f.split("\n")):
    current_id = idx+1
    pulls = line.replace("red","r").replace("blue","b").replace("green", "g")[line.find(":")+1:].split(";")
    needed_red = 0
    needed_green = 0
    needed_blue = 0
    possible = True
    for cb in pulls:
        max_red = 0
        max_green = 0
        max_blue = 0
        cb = cb.replace(" ","")\
            .split(",")
        #print(cb, end= " ")
        for i in cb:
            if i[-1] == "g":
                max_green += int(i[:-1])
                if needed_green < max_green:
                    needed_green = max_green
            if i[-1] == "b":
                max_blue += int(i[:-1])
                if needed_blue < max_blue:
                    needed_blue = max_blue
            if i[-1] == "r":
                max_red += int(i[:-1])
                if needed_red < max_red:
                    needed_red = max_red
    #print(f"{max_red} {max_green} {max_blue}")
    result += needed_red*needed_green*needed_blue
print(result)