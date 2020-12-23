import numpy as np
tiles = []
with open('input2.txt') as f:
    for tile_info in f.read().split('\n\n'):
        title, tile = tile_info.split('\n', 1)
        id = int(title.split(' ')[1][:-1])
        tile = np.array([[1 if c == '#' else 0 for c in row] for row in tile.strip().split('\n')]).astype(int)
        tiles.append((id, tile))

# PART 1

def tile2edges(tile):
    # Order determines rotations and whether flip
    edges = []
    for rot in range(4):
        t = tile
        for _ in range(rot):
            t = np.rot90(t)
        edges.append(sum(bit * (2**i) for i, bit in enumerate(t[0]))) # Normal
        edges.append(sum(bit * (2**i) for i, bit in enumerate(reversed(t[0])))) # Flipped
    return edges

id2edges = {id: tile2edges(tile) for id, tile in tiles}

edge2ids = {}
for id, edges in id2edges.items():
    for edge in edges:
        ids = edge2ids.get(edge, set())
        edge2ids[edge] = ids | {id}


id2neighbors = {}
for id, edges in id2edges.items():
    neighbors = {id for edge in edges for id in edge2ids[edge]} - {id}
    id2neighbors[id] = neighbors

corners = [id for id, neighbors in id2neighbors.items() if len(neighbors) == 2]

from numpy import prod
print(prod(corners))


# PART 2

import math
WIDTH = int(math.sqrt(len(tiles)))

# Fill out grid
def solve(grid, remaining_ids):
    # @grid is grid as one long vector of (id, orientation)
    # This will fill out top-to-bottom then left-to-right
    assert len(grid) + len(remaining_ids) == WIDTH * WIDTH

    if not remaining_ids:
        return (True, grid)

    idx = len(grid) # Where to place
    i = idx % WIDTH
    j = idx // WIDTH

    if i > 0:
        # There is tile above
        id, orientation = grid[i-1 + WIDTH * j]
        edges = id2edges[id]
        # 2 rotations + flip is edge we need to match
        vert_edge = edges[(orientation + 2*2 + 1) % 8]
    if j > 0:
        # There is tile to the left
        id, orientation = grid[i + WIDTH * (j-1)]
        edges = id2edges[id]
        # 1 rotations + flip
        horiz_edge = edges[(orientation + 2*1 + 1) % 8]

    possible_ids = {id for id in remaining_ids if (i == 0 or id in edge2ids[vert_edge]) and (j == 0 or id in edge2ids[horiz_edge])}

    for id in possible_ids:
        edges = id2edges[id]
        for orientation in range(8):
            if (i == 0 or edges[orientation] == vert_edge) and (j == 0 or edges[(orientation + 2*3) % 8] == horiz_edge):
                # Found an orientation that works
                solvable, soln = solve(grid + [(id, orientation)], remaining_ids - {id})
                if solvable:
                    return (solvable, soln)
    # No solution
    return (False, [])

solvable, soln = solve([], set(id2edges.keys()))
print(solvable)
# print(soln[0][0] * soln[WIDTH-1][0] * soln[-WIDTH][0] * soln[-1][0])
