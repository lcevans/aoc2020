import math

with open('input.txt') as f:
    instructions = [(line.strip()[0], int(line.strip()[1:])) for line in f]

# PART 1
orientation = [1, 0] # East
position = [0, 0]
for cmd, val in instructions:
    if cmd in ['N', 'E', 'W', 'S']:
        direction = {
            'N': [0, 1],
            'E': [1, 0],
            'W': [-1, 0],
            'S': [0, -1],
        }[cmd]
        position[0] += val * direction[0]
        position[1] += val * direction[1]
    elif cmd == 'F':
        position[0] += val * orientation[0]
        position[1] += val * orientation[1]
    elif cmd in ['L', 'R']:
        theta = math.radians(val) if cmd == 'L' else math.radians(-val)
        orientation[0], orientation[1] = math.cos(theta)*orientation[0] - math.sin(theta)*orientation[1], \
            math.sin(theta)*orientation[0] + math.cos(theta) * orientation[1]

print(abs(position[0]) + abs(position[1]))


# PART 2
waypoint = [10, 1]
ship = [0, 0]
for cmd, val in instructions:
    if cmd in ['N', 'E', 'W', 'S']:
        direction = {
            'N': [0, 1],
            'E': [1, 0],
            'W': [-1, 0],
            'S': [0, -1],
        }[cmd]
        waypoint[0] += val * direction[0]
        waypoint[1] += val * direction[1]
    elif cmd == 'F':
        ship[0] += val * waypoint[0]
        ship[1] += val * waypoint[1]
    elif cmd in ['L', 'R']:
        theta = math.radians(val) if cmd == 'L' else math.radians(-val)
        waypoint[0], waypoint[1] = math.cos(theta)*waypoint[0] - math.sin(theta)*waypoint[1], \
            math.sin(theta)*waypoint[0] + math.cos(theta) * waypoint[1]

print(abs(ship[0]) + abs(ship[1]))
