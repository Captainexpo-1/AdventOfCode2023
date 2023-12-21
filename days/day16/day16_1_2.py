g = {complex(i,j): c for j, r in enumerate(open('../data/16.txt'))
                     for i, c in enumerate(r.strip())}


def solve(stack):
    done = set()
    while stack:
        position, direction = stack.pop()
        while not (position,direction) in done:
            done.add((position,direction))
            position += direction
            square = g.get(position)
            match square:
                case '|':  # if pipe
                    direction = 1j  # set dir to 1,1
                    stack.append((position, -direction))  # append new to do because of split
                case '-':  # if dash
                    direction = -1
                    stack.append((position, -direction))  # set dir to -1 (up) and append a new to do value because of split
                case '/':  # if slash
                    direction = -complex(direction.imag, direction.real)  # negative invert dir
                case '\\':  # if backslash
                    direction = complex(direction.imag, direction.real)  # invert dir
                case None:
                    break
    return len(set(pos for pos, _ in done)) -1


print(solve([(-1, 1)]))
print(max(map(solve,([(pos-direction,direction)] for direction in (-1,1,1j,-1j) for pos in g if pos-direction not in g))))
print(max(map(solve, ([(pos-dir, dir)] for dir in (1,1j,-1,-1j) for pos in g if pos-dir not in g))))
