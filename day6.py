def turn_on_l(x0, y0, x1, y1):
    if y1 < y0:
        x0, x1 = x1, x0
        y0, y1 = y0, y1
    for i in range(x1 - x0 + 1):
        for j in range(y1 - y0 + 1):
            a_matrix[x0 + i][y0 + j] = 1


def turn_off_l(x0, y0, x1, y1):
    if y1 < y0:
        x0, x1 = x1, x0
        y0, y1 = y0, y1
    for i in range(x1 - x0 + 1):
        for j in range(y1 - y0 + 1):
            a_matrix[x0 + i][y0 + j] = 0


def toggle(x0, y0, x1, y1):
    if y1 < y0:
        x0, x1 = x1, x0
        y0, y1 = y0, y1
    for i in range(x1 - x0 + 1):
        for j in range(y1 - y0 + 1):
            a_matrix[x0 + i][y0 + j] = invert(a_matrix[x0 + i][y0 + j])


def invert(x):
    if x == 0:
        return 1
    if x == 1:
        return 0


def parse_turn(s):
    args = s.split(' ')
    args_0 = [int(x) for x in args[2].split(',')]
    args_1 = [int(x) for x in args[4].split(',')]
    if 'on' in s:
        turn_on_l(args_0[0], args_0[1], args_1[0], args_1[1])
    if 'off' in s:
        turn_on_l(args_0[0], args_0[1], args_1[0], args_1[1])


def parse_toggle(s):
    args = s.split(' ')
    args_0 = [int(x) for x in args[1].split(',')]
    args_1 = [int(x) for x in args[3].split(',')]
    toggle(args_0[0], args_0[1], args_1[0], args_1[1])


a_matrix = [[0 for yrange in range(1000)] for xrange in range(1000)]
with open("inputs\day_06_input.txt") as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
for i in content:
    if "turn" in i:
        parse_turn(i)
    if "toggle" in i:
        parse_toggle(i)
result = [sum(b) for b in a_matrix]
print(sum(result))
