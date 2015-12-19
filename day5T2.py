def nice(s):
    lengths = len(s) - 2
    possiblecandidate = False
    for l in list(range(lengths)):
        candidate = s[l] + s[l+1]
        if s.count(candidate) > 1:
            possiblecandidate = True
            break
    if possiblecandidate:
        for l in list(range(lengths)):
            if s[l] == s[l+2]:
                return True
    return False


with open("inputs/day_04_input.txt") as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
nice_list = [x for x in content if nice(x)]
print(len(nice_list))
