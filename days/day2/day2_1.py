f = open("../data/two.txt", "r").read()
a = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
max_red = 12
max_green = 13
max_blue = 14
result = 0  
for idx,line in enumerate(f.split("\n")):
    current_id = idx+1
    pulls = line.replace("red","r").replace("blue","b").replace("green", "g")[line.find(":")+1:].split(";")
    possible = True
    for cb in pulls:
        cb = cb.replace(" ","")\
            .split(",")
        #print(pulls, end=" ")
        for i in cb:
            if i[-1] == "g":
                if int(i[:-1]) > max_green:
                    possible = False
                    break
            if i[-1] == "b":

                if int(i[:-1]) > max_blue:
                    possible = False
                    break
            if i[-1] == "r":
                #print(int(i[:-1]))
                if int(i[:-1]) > max_red:
                    possible = False
                    break
        if not possible:
            break
    if possible == True:
        #print(current_id)
        result += current_id
print(result)