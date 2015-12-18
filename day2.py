def surface_area_gifts(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l


def smallest_area(l, w, h):
    a_list = [l*w, w*h, h*l]
    return min(a_list)

with open('gifts.txt') as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
content = [y.rsplit('x') for y in content]
content = [list(map(int, x)) for x in content]
gifts_minimal_area = [surface_area_gifts(*x) for x in content]
surplus_area = [smallest_area(*x) for x in content]
print(sum(gifts_minimal_area) + sum(surplus_area))
