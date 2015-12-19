def nice(s):
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    vowelcount = 0
    if 'a' in s:
        vowelcount += s.count('a')
    if 'e' in s:
        vowelcount += s.count('e')
    if 'i' in s:
        vowelcount += s.count('i')
    if 'o' in s:
        vowelcount += s.count('o')
    if 'u' in s:
        vowelcount += s.count('u')
    if vowelcount < 3:
        return False
    lengths = len(s) - 1
    for l in list(range(lengths)):
        if s[l] == s[l+1]:
            return True
    return False


with open("inputs/day_04_input.txt") as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
nice_list = [x for x in content if nice(x)]
print(len(nice_list))
