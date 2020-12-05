passes = []
with open('input.txt') as f:
    for line in f:
        passes.append(line.strip())


# PART 1
def pass2seat_id(boarding_pass):
    seat_id = 0
    for char in boarding_pass:
        seat_id *= 2
        x = 1 if char in ['B', 'R'] else 0
        seat_id += x
    return seat_id

print(max(pass2seat_id(p) for p in passes))

# PART 2
missing_seats = set(range(0, 1023)) - set(pass2seat_id(p) for p in passes)
my_seat = missing_seats - {s-1 for s in missing_seats} - {s+1 for s in missing_seats}
print(my_seat)
