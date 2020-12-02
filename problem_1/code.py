# PART 1
numbers = []
with open('input.txt') as f:
    for line in f:
        numbers.append(int(line.strip()))

for num1 in numbers:
    for num2 in numbers:
        if num1 + num2 == 2020:
            print(num1*num2)

# PART 2
numbers = []
with open('input.txt') as f:
    for line in f:
        numbers.append(int(line.strip()))

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1 + num2 + num3 == 2020:
                print(num1*num2*num3)
