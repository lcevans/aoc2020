with open('input.txt') as f:
    cups = f.read().strip()
    cups = [int(c) for c in cups]


# PART 1

def step(cups):
    first = cups.pop(0)
    to_move = [cups.pop(0) for _ in range(3)]
    dest = (first - 1) or 9
    while dest not in cups:
        dest = (dest - 1) or 9
    dest_idx = cups.index(dest)
    cups = cups[0:dest_idx+1] + to_move + cups[dest_idx+1:] + [first]
    return cups

for _ in range(100):
    cups = step(cups)

idx = cups.index(1)
print(''.join([str(c) for c in cups[idx+1:] + cups[:idx]]))



# PART 2

with open('input.txt') as f:
    cups = f.read().strip()
    cups = [int(c) for c in cups] + list(range(10, 10 ** 6 + 1))

SIZE = len(cups)

# Linked list
cup2next = {}
for i, cup in enumerate(cups):
    cup2next[cup] = cups[(i + 1) % SIZE]

cup = cups[0] # Starting cup
for i in range(10 ** 7):
    if i % 10000 == 0:
        print(i/(10**7))
    # Pickup
    a = cup2next[cup]
    b = cup2next[a]
    c = cup2next[b]
    cup2next[cup] = cup2next[c]

    # Find dest
    dest = (cup - 1) or SIZE
    while dest in [a, b, c]:
        dest = (dest - 1) or SIZE

    temp = cup2next[dest]
    cup2next[dest] = a
    cup2next[c] = temp

    cup = cup2next[cup]

a = cup2next[1]
b = cup2next[a]
print(a * b)
