rules = []
nearby_tickets = []
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        key, rest = line.split(': ')
        range1, range2 = rest.split(' or ')
        l1, r1 = range1.split('-')
        l2, r2 = range2.split('-')
        rules.append((key, int(l1), int(r1), int(l2), int(r2)))
    f.readline() # skip text
    for line in f:
        line = line.strip()
        if not line:
            break
        my_ticket = [int(val) for val in line.split(',')]
    f.readline() # skip text
    for line in f:
        line = line.strip()
        nearby_tickets.append([int(val) for val in line.split(',')])

# PART 1
highest = max(max(r1, r2) for key, l1, r1, l2, r2 in rules)
lowest = min(min(l1, l2) for key, l1, r1, l2, r2 in rules)
nums = set(range(lowest, highest+1))
for key, l1, r1, l2, r2 in rules:
    nums = nums - set(range(l1, r1+1)) - set(range(l2, r2+1))

total = 0
for ticket in nearby_tickets:
    for val in ticket:
        if val < lowest or val > highest or val in nums:
            total += val
print(total)


# PART 2
highest = max(max(r1, r2) for key, l1, r1, l2, r2 in rules)
lowest = min(min(l1, l2) for key, l1, r1, l2, r2 in rules)
nums = set(range(lowest, highest+1))
for key, l1, r1, l2, r2 in rules:
    nums = nums - set(range(l1, r1+1)) - set(range(l2, r2+1))

valid_tickets = []
for ticket in nearby_tickets:
    if not any(val < lowest or val > highest or val in nums for val in ticket):
        valid_tickets.append(ticket)

idx2possible_keys = {}
num_fields = len(rules)
for i in range(num_fields):
    possible_keys = []
    for key, l1, r1, l2, r2 in rules:
        if all(l1 <= ticket[i] <= r1 or l2 <= ticket[i] <= r2 for ticket in valid_tickets):
            possible_keys.append(key)
    idx2possible_keys[i] = possible_keys

idx2key = {}
while len(idx2key.keys()) < num_fields:
    for idx, keys in idx2possible_keys.items():
        if len(keys) == 1:
            break
    else:
        assert False
    key = keys[0]
    idx2key[idx] = key
    del idx2possible_keys[idx]
    idx2possible_keys = {idx: [k for k in keys if k != key]for idx, keys in idx2possible_keys.items()}

from numpy import prod
print(prod([my_ticket[i] for i in range(num_fields) if idx2key[i].startswith('departure')]))
