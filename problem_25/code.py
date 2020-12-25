with open('input.txt') as f:
    num1 = int(f.readline().strip())
    num2 = int(f.readline().strip())

# PART 1

n = 1
i = 0
i1 = None
i2 = None
while True:
    i += 1
    n *= 7
    n = n % 20201227
    if n == num1:
        i1 = i
    if n == num2:
        i2 = i
    if i1 and i2:
        break

n = 1
for _ in range(i1):
    n *= num2
    n = n % 20201227
print(n)
