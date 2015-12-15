# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

# Some of the GF2 problems require use of the value GF2.one so the stencil imports it.

from GF2 import one
from itertools import combinations
## 1: (Problem 2.14.1) Vector Addition Practice 1
#Please express each answer as a list of numbers
p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = [v + u for v, u in zip(p1_v, p1_u)]
p1_v_minus_u = [v - u for v, u in zip(p1_v, p1_u)]
p1_three_v_minus_two_u = [3*v - 2*u for v, u in zip(p1_v, p1_u)]

## 2: (Problem 2.14.2) Vector Addition Practice 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [v + u for v, u in zip(p2_v, p2_u)]
p2_v_minus_u = [v - u for v, u in zip(p2_v, p2_u)]
p2_two_v_minus_u = [2*v - u for v, u in zip(p2_v, p2_u)]
p2_v_plus_two_u = [v + 2*u for v, u in zip(p2_v, p2_u)]


## 3: (Problem 2.14.3) Vector Addition Practice 3
# Write your answer using GF2's one instead of the number 1
p3_v = [0, one, one]
p3_u = [one, one, one]
p3_vector_sum_1 = [v + u for v, u in zip(p3_v, p3_u)]
p3_vector_sum_2 = [v + u + u for v, u in zip(p3_v, p3_u)]

## 4: (Problem 2.14.4) GF2 Vector Addition A
# Please express your solution as a subset of the letters {'a','b','c','d','e','f'}.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# The answer should be an empty set, written set(), if the given vector u cannot
# be written as the sum of any subset of the vectors a, b, c, d, e, and f.
u_0010010 = set()
u_0100010 = set()

p4_dict = {'a':[one, one, 0, 0, 0, 0, 0], 'b':[0, one, one, 0, 0, 0, 0], \
           'c':[0, 0, one, one, 0, 0, 0], 'd':[0, 0, 0, one, one, 0, 0], \
           'e':[0, 0, 0, 0, one, one, 0], 'f':[0, 0, 0, 0, 0, one, one]}

def GF_sum(vec_a, vec_b): return [a + b for a, b in zip(vec_a, vec_b)]

p4_keys = p4_dict.keys()
p4_combinations = set()
for i in range(2, len(p4_keys)):
    combos = list(combinations(p4_keys, i))
    for combo in combos:
        p4_combinations.add(combo)

for combo in p4_combinations:
    sum_vec = p4_dict[combo[0]]
    for i in range(1, len(combo)):
        sum_vec = GF_sum(sum_vec, p4_dict[combo[i]])
    if sum_vec == [0, one, 0, 0, 0, one, 0]:
        u_0100010 = set(combo)
    elif sum_vec == [0, 0, one, 0, 0, one, 0]:
        u_0010010 = set(combo)

## 5: (Problem 2.14.5) GF2 Vector Addition B
# Use the same format as the previous problem

v_0010010 = set()
v_0100010 = set()

p5_dict = {'a':[one, one, one, 0, 0, 0, 0], 'b':[0, one, one, one, 0, 0, 0], \
           'c':[0, 0, one, one, one, 0, 0], 'd':[0, 0, 0, one, one, one, 0], \
           'e':[0, 0, 0, 0, one, one, one], 'f':[0, 0, 0, 0, 0, one, one]}

p5_keys = p5_dict.keys()
p5_combinations = set()
for i in range(2, len(p5_keys)):
    combos = list(combinations(p5_keys, i))
    for combo in combos:
        p5_combinations.add(combo)

for combo in p5_combinations:
    sum_vec = p5_dict[combo[0]]
    for i in range(1, len(combo)):
        sum_vec = GF_sum(sum_vec, p5_dict[combo[i]])
    if sum_vec == [0, one, 0, 0, 0, one, 0]:
        v_0100010 = set(combo)
    elif sum_vec == [0, 0, one, 0, 0, one, 0]:
        v_0010010 = set(combo)

## 6: (Problem 2.14.6) Solving Linear Equations over GF(2)
#You should be able to solve this without using a computer.
x_gf2 = [...]

## 7: (Problem 2.14.7) Formulating Equations using Dot-Product
#Please provide each answer as a list of numbers
v1 = [...]
v2 = [...]
v3 = [...]

## 8: (Problem 2.14.9) Practice with Dot-Product
uv_a = ...
uv_b = ...
uv_c = ...
uv_d = ...
