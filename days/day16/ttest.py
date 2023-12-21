# print(max(map(fn, ([(pos-dir, dir)] for dir in (1,1j,-1,-1j)
# for pos in g if pos-dir not in g))))


g = {complex(i, j): c for j, r in enumerate(open('../data/16.txt'))
     for i, c in enumerate(r.strip())}


def fn(todo):
    done = set()
    while todo:
        pos, dir = todo.pop()  # get of top of stack
        while not (pos, dir) in done:
            done.add((pos, dir))  # add pos and dir to the done
            pos += dir  # add the direction to pos
            match g.get(pos):  # switch statement with the square at pos "pos"
                case '|':  # if pipe
                    dir = 1j # set dir to 1,1
                    todo.append((pos, -dir)) # append new to do because of split
                case '-':  # if dash
                    dir = -1
                    todo.append((pos, -dir))  # set dir to -1 (up) and append a new to do value because of split
                case '/':  # if slash
                    dir = -complex(dir.imag, dir.real)  # negative invert dir
                case '\\':  # if backslash
                    dir = complex(dir.imag, dir.real)  # invert dir
                case None:
                    break

    return len(set(pos for pos, _ in done)) - 1


print(fn([(-1, 1)]))
