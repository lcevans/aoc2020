bag_mapping = {}
with open('input.txt') as f:
    for line in f:
        line = line.strip().strip('.')
        input_bag, output_bags = line.split(' contain ')
        if output_bags.startswith('no'):
            continue
        input_color = input_bag.split(' bag')[0]
        output_num_colors = [output_bag.split(' bag')[0].split(' ', 1) for output_bag in output_bags.split(', ')]
        bag_mapping[input_color] = output_num_colors


# PART 1
def color2descendants(color):
    descendants = {color}
    if color in bag_mapping:
        for num, col in bag_mapping[color]:
            descendants = descendants | color2descendants(col)
    return descendants

# Minus 1 because don't count the shiny gold bag itself
print(len([col for col in bag_mapping.keys() if 'shiny gold' in color2descendants(col)]) - 1)


# PART 2
def color2num_bags(color):
    num_bags = 1
    if color in bag_mapping:
        for num, col in bag_mapping[color]:
            num_bags += int(num) * color2num_bags(col)
    return num_bags

# Minus 1 because don't count the shiny gold bag itself
print(color2num_bags('shiny gold') - 1)
