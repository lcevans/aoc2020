# PART 1
def masked_val(val):
    bit_str = '{0:036b}'.format(val)
    masked_bit_str = ''.join([bit if mask_bit == 'X' else mask_bit for bit, mask_bit in zip(bit_str, mask)])
    return int(masked_bit_str, 2)

memory = {}
with open('input.txt') as f:
    for line in f:
        if line.startswith('mask'):
            mask = line.strip().split(' = ')[1]
        else:
            cmd, val = line.strip().split(' = ')
            addr = cmd[4:-1]
            memory[int(addr)] = masked_val(int(val))
print(sum(memory.values()))

# PART 2
import itertools
def masked_addr(addr):
    # Returns all memory addresses
    bit_str = '{0:036b}'.format(addr)
    lists = []
    for bit, mask_bit in zip(bit_str, mask):
        if mask_bit == '0':
            lists.append([bit])
        elif mask_bit == '1':
            lists.append([mask_bit])
        else:
            lists.append(['0', '1'])
    addresses = [int(''.join(addr_bits), 2) for addr_bits in itertools.product(*lists)]
    return addresses

memory = {}
with open('input.txt') as f:
    for line in f:
        if line.startswith('mask'):
            mask = line.strip().split(' = ')[1]
        else:
            cmd, val = line.strip().split(' = ')
            base_addr = cmd[4:-1]
            for addr in masked_addr(int(base_addr)):
                memory[addr] = int(val)
print(sum(memory.values()))
