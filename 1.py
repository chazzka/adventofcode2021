with open("inputs/1.txt") as file:
    data = [int(line) for line in file]

count = 0
for i, sample in enumerate(data):
    if i == len(data) - 1:
        break
    if data[i + 1] > data[i]:
        count += 1

# part 1
print(count)

countt = 0
previous_sum = 0
sum = 0
for i, sample in enumerate(data):
    if i == len(data) - 3:
        break
    for j in range(i, i + 3):
        sum += data[j]
    if sum > previous_sum:
        countt += 1
    previous_sum = sum
    sum = 0

# part 2
print(countt)
