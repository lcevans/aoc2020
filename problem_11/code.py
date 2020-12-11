# PART 1

with open('input.txt') as f:
    grid = [list(line.strip()) for line in f]
HEIGHT = len(grid)
WIDTH = len(grid[0])

def step(grid):
    next_grid = [list('?' * WIDTH) for _ in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == '.':
                next_grid[i][j] = '.'
                continue
            neighbors = set((ii, jj) for ii in [i-1, i, i+1] for jj in [j-1, j, j+1] if 0<=ii<HEIGHT and 0<=jj<WIDTH) - {(i,j)}
            occupied = sum(1 for ii, jj in neighbors if grid[ii][jj] == '#')
            if grid[i][j] == 'L' and occupied == 0:
                next_grid[i][j] = '#'
            elif grid[i][j] == '#' and occupied >= 4:
                next_grid[i][j] = 'L'
            else:
                next_grid[i][j] = grid[i][j]
    return next_grid

while True:
    next_grid = step(grid)
    if grid == next_grid:
        break
    grid = next_grid

print(sum([row.count('#') for row in grid]))

# PART 2

# Load again since I changed grid in part 1...
with open('input.txt') as f:
    grid = [list(line.strip()) for line in f]
HEIGHT = len(grid)
WIDTH = len(grid[0])

def step(grid):
    next_grid = [list('?' * WIDTH) for _ in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == '.':
                next_grid[i][j] = '.'
                continue

            occupied = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ii = i + di
                    jj = j + dj
                    while 0<=ii<HEIGHT and 0<=jj<WIDTH:
                        if grid[ii][jj] == '#':
                            occupied += 1
                            break
                        elif grid[ii][jj] == 'L':
                            break
                        ii += di
                        jj += dj

            if grid[i][j] == 'L' and occupied == 0:
                next_grid[i][j] = '#'
            elif grid[i][j] == '#' and occupied >= 5:
                next_grid[i][j] = 'L'
            else:
                next_grid[i][j] = grid[i][j]
    return next_grid

while True:
    next_grid = step(grid)
    if grid == next_grid:
        break
    grid = next_grid

print(sum([row.count('#') for row in grid]))
