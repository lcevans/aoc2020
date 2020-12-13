with open('input.txt') as f:
    start = int(f.readline().strip())
    buses = f.readline().strip().split(',')

# PART 1
good_buses = [int(bus) for bus in buses if bus != 'x']
best = sorted([(bus - (start % bus), bus) for bus in good_buses])[0]
print(best[0] * best[1])

# PART 2

# Chinese Remainder Theorem
# c.f. https://www.codechef.com/wiki/tutorial-number-theory#:~:text=Fundamental%20Theorem%20of%20Arithmetic%20and%20the%20Division%20Algorithm&text=The%20fundamental%20theorem%20of%20arithmetic,3%20X%205%20X%2013.
#
# Note: The buses are all prime here

# t % n_i = a_i
a, n = zip(*[((int(bus) - i) % int(bus), int(bus)) for i, bus in enumerate(buses) if bus != 'x'])

# c_i = prod(n_i)/n_i
from numpy import prod
N = prod(n)
c = [int(N / n_i) for n_i in n]

# d_i solves c_i * x % n_i == 1
def c_to_d(c_i, n_i):
    for x in range(n_i):
        if (c_i * x) % n_i == 1:
            return x
d = [c_to_d(c_i, n_i) for c_i, n_i in zip(c, n)]

# Solution is a1c1d1 + a2c2d2 + ... + akckdk
# Smallest solution is this mod N
t = sum(a_i * c_i * d_i for a_i, c_i, d_i in zip(a, c, d)) % N
print(t)
