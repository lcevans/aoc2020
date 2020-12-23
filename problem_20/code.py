import numpy as np
tiles = []
with open('input.txt') as f:
    for tile_info in f.read().split('\n\n'):
        title, tile = tile_info.split('\n', 1)
        id = int(title.split(' ')[1][:-1])
        tile = np.array([[1 if c == '#' else 0 for c in row] for row in tile.strip().split('\n')]).astype(int)
        tiles.append((id, tile))

# PART 1

def tile2edges(tile):
    # Order determines rotations and whether flip
    edges = []
    t = np.copy(tile)
    for rot in range(4):
        edges.append(sum(bit * (2**i) for i, bit in enumerate(t[0]))) # Normal
        edges.append(sum(bit * (2**i) for i, bit in enumerate(reversed(t[0])))) # Flipped
        t = np.rot90(t)
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
id2tile = {id: tile for id, tile in tiles}


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
        rots, flipped = divmod(orientation, 2)
        vert_edge = edges[(2*(rots+2) + (1-flipped)) % 8]
    if j > 0:
        # There is tile to the left
        id, orientation = grid[i + WIDTH * (j-1)]
        edges = id2edges[id]
        # 1 rotations + flip
        rots, flipped = divmod(orientation, 2)
        horiz_edge = edges[(2*(rots+(1-2*flipped)) + (1-flipped)) % 8]

    possible_ids = {id for id in remaining_ids if (i == 0 or id in edge2ids[vert_edge]) and (j == 0 or id in edge2ids[horiz_edge])}

    for id in possible_ids:
        edges = id2edges[id]
        for orientation in range(8):
            flipped = orientation % 2
            if (i == 0 or edges[orientation] == vert_edge) and (j == 0 or edges[(orientation + 2*3*(1-2*flipped)) % 8] == horiz_edge):
                # Found an orientation that works
                solvable, soln = solve(grid + [(id, orientation)], remaining_ids - {id})
                if solvable:
                    return (solvable, soln)
    # No solution
    return (False, [])

solvable, soln = solve([], set(id2edges.keys()))
print(solvable)


# Fill out full grid:
full_grid = np.zeros((WIDTH*8, WIDTH*8))
for idx, info in enumerate(soln):
    i = idx % WIDTH
    j = idx // WIDTH
    id, orientation = info
    tile = id2tile[id]
    rots, flipped = divmod(orientation, 2)
    for _ in range(rots):
        tile = np.rot90(tile)
    if flipped:
        tile = np.flip(tile, 1)
    for ii in range(0,8):
        for jj in range(0,8):
            full_grid[8*i + ii, 8*j + jj] = tile[ii + 1, jj + 1]

# Display grid
def prettify(arr):
    for row in arr:
        print(row)

# Find sea monsters!

monster = np.array([
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
[0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
])

def num_monsters(chart):
    # Returns (found_monsters, roughness)
    monster_mask = np.zeros(chart.shape)
    found = False
    for i in range(8*WIDTH - 3):
        for j in range(8*WIDTH - 20):
            if np.array_equal(chart[i:i+3, j:j+20]*monster, monster):
                found = True
                monster_mask[i:i+3, j:j+20] = np.maximum(monster_mask[i:i+3, j:j+20], monster)
    chart_without_monsters = chart * (1-monster_mask)
    return (found, int(np.sum(chart_without_monsters)))

chart = full_grid
for rot in range(4):
    print(num_monsters(chart))
    chart = np.flip(chart, 1)
    print(num_monsters(chart))
    chart = np.flip(chart, 1)
    chart = np.rot90(chart)
