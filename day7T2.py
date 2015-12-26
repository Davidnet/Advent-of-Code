wires = {'b': 46065}


def value_of(v):
    try:
        return int(v)
    except ValueError:
        return wires[v]


def parse_expression(ex):
    dat_in_line = ex.strip().split()
    if len(dat_in_line) == 1:
        return value_of(dat_in_line[0])
    if len(dat_in_line) == 2:
        n = value_of(dat_in_line[1])
        return n ^ 65535  # Observe answer [1]
    o1, e, o2 = dat_in_line
    o1, o2 = value_of(o1), value_of(o2)
    if e == 'AND':
        return o1 & o2
    if e == 'OR':
        return o1 | o2
    if e == 'LSHIFT':
        return o1 << o2
    if e == 'RSHIFT':
        return o1 >> o2


def evaluate(line):
    ex, n = line.split(' -> ')
    if n != 'b':
        wires[n] = parse_expression(ex)

data = open("inputs/day_07_input.txt").read().splitlines()
while data:
    for i, d in enumerate(data):
        try:
            evaluate(d)
            del data[i]
        except KeyError:
            continue

print(wires['a'])
# [1] http://stackoverflow.com/questions/34477329/doing-bitwise-complement-on-a-16-bit-signal-python-operator/34477481#34477481
