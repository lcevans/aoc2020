with open('input.txt') as f:
    cube = [[[c for c in line.strip()] for line in f]]

# PART 1
SIZE = len(cube[0])
import numpy as np
space = np.zeros((24, 24, 24))
for z in range(0, 1):
    for y in range(0, SIZE):
        for x in range(0, SIZE):
            space[12 - (SIZE//2) + x, 12 - (SIZE//2) + y, 12 + z] = 1 if cube[z][y][x] == '#' else 0

for _ in range(6):
    new_space = np.zeros((24,24,24))
    for x in range(0, 24):
        for y in range(0, 24):
            for z in range(0, 24):
                neighbors = set((i, j, k) for i in [x-1,x,x+1] for j in [y-1,y,y+1] for k in [z-1,z,z+1] if 0<=i<24 and 0<=j<24 and 0<=k<24) - {(x,y,z)}
                active_neighbors = sum(space[i,j,k] for i,j,k in neighbors)
                if (space[x,y,z] == 1 and active_neighbors in [2,3]) or (space[x,y,z] == 0 and active_neighbors ==3):
                        new_space[x,y,z] = 1
    space = new_space

print(np.count_nonzero(space))


# PART 2
SIZE = len(cube[0])
AMBIENT_SIZE = 20
import numpy as np
space = np.zeros((AMBIENT_SIZE, AMBIENT_SIZE, AMBIENT_SIZE, AMBIENT_SIZE))
for z in range(0, 1):
    for y in range(0, SIZE):
        for x in range(0, SIZE):
            space[(AMBIENT_SIZE//2) - (SIZE//2) + x, (AMBIENT_SIZE//2) - (SIZE//2) + y, (AMBIENT_SIZE//2) + z, (AMBIENT_SIZE//2)] = 1 if cube[z][y][x] == '#' else 0

for step in range(6):
    print("STEP: ", str(step))
    new_space = np.zeros((AMBIENT_SIZE,AMBIENT_SIZE,AMBIENT_SIZE, AMBIENT_SIZE))
    for x in range(0, AMBIENT_SIZE):
        for y in range(0, AMBIENT_SIZE):
            for z in range(0, AMBIENT_SIZE):
                for w in range(0, AMBIENT_SIZE):
                    neighbors = set((i, j, k, l) for i in [x-1,x,x+1] for j in [y-1,y,y+1] for k in [z-1,z,z+1] for l in [w-1,w,w+1]
                                    if 0<=i<AMBIENT_SIZE and 0<=j<AMBIENT_SIZE and 0<=k<AMBIENT_SIZE and 0<=l<AMBIENT_SIZE) - {(x,y,z,w)}
                    active_neighbors = sum(space[i,j,k,l] for i,j,k,l in neighbors)
                    if (space[x,y,z,w] == 1 and active_neighbors in [2,3]) or (space[x,y,z,w] == 0 and active_neighbors ==3):
                        new_space[x,y,z,w] = 1
    space = new_space

print(np.count_nonzero(space))
