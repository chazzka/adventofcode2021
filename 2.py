with open('inputs/2.txt') as f:
    mylist = [tuple(map(str, i.strip('\n').split(' '))) for i in f]

# part 1
horizontal = 0
depth = 0

for tup in mylist:
    op = tup[0]
    val = int(tup[1])
    if op == 'forward':
        horizontal += val
    if op == 'down':
        depth += val
    if op == 'up':
        depth -= val

print(horizontal * depth)

# part 2
horizontal = 0
depth = 0
aim = 0

for tup in mylist:
    op = tup[0]
    val = int(tup[1])
    if op == 'forward':
        horizontal += val
        depth += aim * val
    if op == 'down':
        aim += val
    if op == 'up':
        aim -= val

print(horizontal * depth)
