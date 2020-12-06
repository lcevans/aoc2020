with open('input.txt') as f:
    forms = [x.split('\n') for x in f.read().strip().split('\n\n')]

# PART 1
counts = [len({char for idv_response in form for char in idv_response}) for form in forms]
print(sum(counts))

# PART 2
counts = [len(set.intersection(*[set(idv_response) for idv_response in form])) for form in forms]
print(sum(counts))
