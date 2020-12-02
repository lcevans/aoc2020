# PART 1
good = 0
with open('input.txt') as f:
    for line in f:
        requirement, letter, password = line.strip().split(' ')
        letter = letter[0] # Strip colon
        lower = int(requirement.split('-')[0])
        upper = int(requirement.split('-')[1])

        num_letter = len([c for c in password if c == letter])
        if lower <= num_letter and num_letter <= upper:
            good += 1
print(good)

# PART 2
good = 0
with open('input.txt') as f:
    for line in f:
        requirement, letter, password = line.strip().split(' ')
        letter = letter[0] # Strip colon
        idx1 = int(requirement.split('-')[0]) - 1
        idx2 = int(requirement.split('-')[1]) - 1

        match1 = 1 if (password[idx1] == letter) else 0
        match2 = 1 if (password[idx2] == letter) else 0

        if match1 + match2 == 1: # Exactly one match
            good += 1
print(good)
