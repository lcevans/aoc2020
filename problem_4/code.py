passports = []
with open('input.txt') as f:
    passport = {}
    for line in f:
        line = line.strip()
        if len(line) == 0: # linebreak
            passports.append(passport)
            passport = {}
            continue
        for pair in line.split(' '):
            key, val = pair.split(':')
            passport[key] = val
    # End of file counts as end of passport
    passports.append(passport)

# PART 1
def is_valid(passport):
    REQ_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return len(set(passport.keys()) & REQ_FIELDS) == len(REQ_FIELDS)
print(len([passport for passport in passports if is_valid(passport)]))


# PART 2
def is_valid(passport):
    REQ_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if not len(set(passport.keys()) & REQ_FIELDS) == len(REQ_FIELDS):
        return False
    # Keys are present
    valid = (
        (len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002)
        and (len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020)
        and (len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030)
        and ((passport['hgt'][-2:] == "cm" and 150 <= int(passport['hgt'][:-2]) <= 193)
             or (passport['hgt'][-2:] == "in" and 59 <= int(passport['hgt'][:-2]) <= 76))
        and (len(passport['hcl']) == 7 and passport['hcl'][0] == '#' and all(ord(c) in list(range(48,58)) + list(range(97, 103)) for c in passport['hcl'][1:]))
        and (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        and (len(passport['pid']) == 9 and all(ord(c) in range(48,58) for c in passport['pid']))
    )
    return valid
print(len([passport for passport in passports if is_valid(passport)]))
