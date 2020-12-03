mountain = []
with open('input.txt') as f:
    for line in f:
        mountain.append(line.strip())

# PART 1
width = len(mountain[0])
slope = [3,1]
curr_pos = [0,0]
trees = 0
while curr_pos[1] < len(mountain):
    if mountain[curr_pos[1]][curr_pos[0] % width] == '#':
        trees += 1
    curr_pos[0] += slope[0]
    curr_pos[1] += slope[1]
print(trees)

# PART2
product = 1
for slope in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
    width = len(mountain[0])
    curr_pos = [0,0]
    trees = 0
    while curr_pos[1] < len(mountain):
        if mountain[curr_pos[1]][curr_pos[0] % width] == '#':
            trees += 1
        curr_pos[0] += slope[0]
        curr_pos[1] += slope[1]
    product *= trees
print(product)
