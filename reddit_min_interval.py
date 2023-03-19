import timeit

list_size = 10 ** 2
num_trials = 10 ** 3
setup = f"""
import random
num_list = [random.randint(0, {list_size}) for i in range({list_size})]
"""
setup1 = (
    setup
    + """
import itertools as it
def min_interval(num_list):
    return min(abs(y - x) for x, y in it.combinations(num_list, 2))
"""
)

setup2 = (
    setup
    + """
def min_interval(num_list):
    sorted_list = sorted(num_list)
    return min(x - sorted_list[i] for i, x in enumerate(sorted_list[1:]))
"""
)

setup3 = (
    setup
    + """
def min_interval(num_list):
    sorted_list = sorted(num_list)
    return min(y - x for x, y in zip(sorted_list, sorted_list[1:]))
"""
)

setup4 = (
    setup
    + """
def min_interval(num_list):
    sorted_list = sorted(num_list)
    return min(sorted_list[i] - sorted_list[i-1] for i in range(1, len(sorted_list)))
"""
)

setup5 = (
    setup
    + """
import numpy as np
def min_interval(num_list):
    return np.min(np.diff(np.sort(np.array(num_list))))
"""
)

test_code = """
result = min_interval(num_list)
"""
print(f"list_size: {list_size}  num_trials: {num_trials}")
print(
    f"Timing of min_interval_enum(): {timeit.timeit(setup=setup2, stmt=test_code, number=num_trials)}"
)
print(
    f"Timing of min_interval_zip(): {timeit.timeit(setup=setup3, stmt=test_code, number=num_trials)}"
)
print(
    f"Timing of min_interval_rng(): {timeit.timeit(setup=setup4, stmt=test_code, number=num_trials)}"
)
print(
    f"Timing of min_interval_np(): {timeit.timeit(setup=setup5, stmt=test_code, number=num_trials)}"
)
print(
    f"Timing of min_interval_comb(): {timeit.timeit(setup=setup1, stmt=test_code, number=num_trials)}"
)

