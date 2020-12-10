with open('input.txt') as f:
    adaptors = [int(line.strip()) for line in f]
adaptors.sort()

# PART 1
jolts = [0] + adaptors + [max(adaptors) + 3]
diffs = [next_jolt - jolt for jolt, next_jolt in zip(jolts, jolts[1:])]
print(diffs.count(1) * diffs.count(3))

# PART 2
jolts = [0] + adaptors + [max(adaptors) + 3]
# Dynamic Programming
num_paths = [0] * len(jolts)
num_paths[0] = 1
for i in range(1, len(jolts)):
    paths = 0
    for j in reversed(range(0, i)):
        if jolts[-j-1] - jolts[-i-1] <= 3:
            paths += num_paths[j]
    num_paths[i] = paths
print(num_paths[-1])
