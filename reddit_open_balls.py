"""
How can I compare a list of tuples that contain an int range?

The idea is to write a func that takes two lists (they can be different len) that contain tuples indicating ranges of ints of one digit as inputs, lets say:

List1 = [(0,2), (5,6), (7,8), (8,9)]
List2 = [(1,3), (4,6), (8,9)]

it should return a list of all the ranges you could fit into both lists without everlaping with an existing range, in this case for example:

Output = [(3,4), (6,7)]

Also, note that while the input can separate ranges in two parts (7,8),(8,9)... the output should return it in only one range if possible, for example, returning (7,8),(8,9) would be wrong, it should return (7,9).

I am struggling to find how I should even tackle this, any ideas?
"""
import itertools as it
import more_itertools as mit

List1 = [(0, 2), (5, 6), (7, 8), (8, 9)]
List2 = [(1, 3), (4, 6), (8, 9)]

balls1 = [(a, b) for a, b in mit.grouper(sum(List1, ())[1:-1], n=2) if b - a > 0]
balls2 = [(a, b) for a, b in mit.grouper(sum(List2, ())[1:-1], n=2) if b - a > 0]

nums = [set(range(a, b + 1)) for a, b in sorted(balls1 + balls2)]

results = [
    (a, b)
    for a, b in filter(None, (i.intersection(j) for i, j in it.combinations(nums, 2)))
]
