with open('santadir2.txt') as f:
    content = f.readline()


content = content.strip('\n')
sum = 0
position = 1
for i in content:
    if i == '(':
        sum += 1
    if i == ')':
        sum = sum - 1
    position += 1
    if sum == -1:
        print(position)
print(sum)
