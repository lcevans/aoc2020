instructions = []
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        op_code, val = line.split(' ')
        instructions.append((op_code, int(val)))

# PART 1
accumulator = 0
pc = 0
executed_commands = set()
while True:
    if pc in executed_commands:
        print(accumulator)
        break
    executed_commands.add(pc)
    op_code, val = instructions[pc]
    pc += 1
    if op_code == 'acc':
        accumulator += val
    elif op_code == 'jmp':
        pc += (val-1)


# PART 2
def run(instructions):
    accumulator = 0
    pc = 0
    executed_commands = set()
    while True:
        if pc == len(instructions):
            return (True, accumulator)
        if pc in executed_commands:
            return (False, -1)
        executed_commands.add(pc)
        op_code, val = instructions[pc]
        pc += 1
        if op_code == 'acc':
            accumulator += val
        elif op_code == 'jmp':
            pc += (val-1)

for i, instruction in enumerate(instructions):
    op_code, val = instruction
    if op_code == 'acc':
        continue
    elif op_code == 'jmp':
        new_instruction = ('nop', val)
    elif op_code == 'nop':
        new_instruction = ('jmp', val)

    duped = instructions.copy()
    duped[i] = new_instruction

    finished, accumulator = run(duped)
    if finished:
        print(accumulator)
