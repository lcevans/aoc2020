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
num_paths[-1] = 1
for i in reversed(range(0, len(jolts)-1)):
    num_paths[i] = sum(num_paths[j] for j in range(i, len(jolts)) if jolts[j] - jolts[i] <= 3)
print(num_paths[0])
