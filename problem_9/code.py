with open('input.txt') as f:
    numbers = [int(line.strip()) for line in f]

# PART 1
preamble = 25
for i, number in enumerate(numbers):
    if i < preamble:
        continue
    start = max(i - preamble, 0)
    sums = {numbers[j] + numbers[k] for j in range(start, i) for k in range(start, i)}
    if number not in sums:
        print(number)
        break

# PART 2
preamble = 25
for i, number in enumerate(numbers):
    if i < preamble:
        continue
    start = max(i - preamble, 0)
    sums = {numbers[j] + numbers[k] for j in range(start, i) for k in range(start, i)}
    if number not in sums:
        bad_num = number
        break

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if sum(numbers[i:j]) == bad_num:
            print(max(numbers[i:j]) + min(numbers[i:j])) # Note: This will also print 2 * bad_num
