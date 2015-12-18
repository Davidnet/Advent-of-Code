with open('santadir.txt') as f:
    content = f.readline()


content = content.strip('\n')
sum = 0
for i in content:
    if i == '(':
        sum += 1
    if i == ')':
        sum = sum - 1
print(sum)
