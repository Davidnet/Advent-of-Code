def move(step, coord):
    moves = {
        ">": [1, 0],
        "<": [-1, 0],
        "^": [0, 1],
        "v": [0, -1],
    }

    diff = moves[step]
    return (coord[0] + diff[0], coord[1] + diff[1])


def get_visits(steps, n_movers=1):
    visited = {(0, 0)}

    coords = [(0, 0)] * n_movers
    for n_steps, step in enumerate(steps):
        idx = n_steps % n_movers
        coords[idx] = move(step, coords[idx])
        visited.add(coords[idx])

    return len(visited)


def main():
    with open("inputs/day_03_input.txt", "r") as input_file:
        steps = input_file.read()
    steps = steps.strip('\n')
    print("{} houses visited alone".format(get_visits(steps)))
    print("{} houses visited with robot".format(get_visits(steps, n_movers=2)))


if __name__ == "__main__":
    main()
