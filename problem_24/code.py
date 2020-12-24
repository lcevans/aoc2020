directions = []
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        i = 0
        tokens = []
        while i < len(line):
            if line[i] in ['n', 's']:
                tokens.append(line[i:i+2])
                i += 2
            else:
                tokens.append(line[i])
                i += 1
        directions.append(tokens)


# PART 1

import numpy as np
token2vec = {
    'e': np.array([1.0, 0]),
    'w': np.array([-1.0, 0]),
    'ne': np.array([0.5, 0.5]),
    'se': np.array([0.5, -0.5]),
    'nw': np.array([-0.5, 0.5]),
    'sw': np.array([-0.5, -0.5]),
}

from collections import defaultdict
pos2count = defaultdict(int)
for tokens in directions:
    pos = np.array([0.0,0.0])
    for token in tokens:
        pos += token2vec[token]
    pos_str = ','.join(str(d) for d in pos)
    pos2count[pos_str] += 1

print(len([val for val in pos2count.values() if val % 2 == 1]))


# PART 2

black_tiles = {key for key, val in pos2count.items() if val % 2 == 1}

def step(black_tiles):
    influence = defaultdict(int)
    for tile in black_tiles:
        tile = np.array([float(d) for d in tile.split(',')])
        for vec in token2vec.values():
            pos_str = ','.join(str(d) for d in tile + vec)
            influence[pos_str] += 1

    new_black_tiles = set()
    # black tiles staying black
    for pos_str in black_tiles:
        if influence[pos_str] in [1, 2]:
            new_black_tiles.add(pos_str)
    # white tiles turning black
    for pos_str in influence.keys() - black_tiles:
        if influence[pos_str] == 2:
            new_black_tiles.add(pos_str)

    return new_black_tiles

day = 0
while day < 100:
    black_tiles = step(black_tiles)
    day += 1
print(len(black_tiles))
