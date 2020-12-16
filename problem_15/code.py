with open('input.txt') as f:
    numbers = [int(num) for num in  f.read().strip().split(',')]

# PART 1

num2time = {}
for i, num in enumerate(numbers):
    age = i - num2time[num] if num in num2time else 0
    num2time[num] = i
while i < 2020 - 1:
    i += 1
    num = age
    age = i - num2time[num] if num in num2time else 0
    num2time[num] = i
print(num)


# PART 2

num2time = {}
for i, num in enumerate(numbers):
    age = i - num2time[num] if num in num2time else 0
    num2time[num] = i
while i < 30000000 - 1:
    i += 1
    num = age
    age = i - num2time[num] if num in num2time else 0
    num2time[num] = i
print(num)
