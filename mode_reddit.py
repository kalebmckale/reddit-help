from collections import Counter
from collections.abc import Sequence
from typing import Union


#def calculate_mode(num_list: Sequence[int]) -> Union[None, int, Sequence[int]]:
#    if not isinstance(num_list, Sequence):
#        raise ValueError(
#            f"Expected a sequence-type for num_list: '{type(num_list).__name__}' given."
#        )
#    if len(num_list) == 0:
#        raise ValueError("num_list cannot be empty.")
#    counter = Counter(num_list)
#    if len(counts := set(counter.values())) == 1:
#        return None
#    modes = [num for num, count in counter.items() if count == max(counts)]
#    return modes if len(modes) > 1 else modes.pop()

#def calculate_mode(num_list: Sequence[int]) -> Sequence[int]:
#    if not isinstance(num_list, Sequence):
#        raise ValueError(
#            f"Expected a sequence-type for num_list: '{type(num_list).__name__}' given."
#        )
#    counter = Counter(num_list)
#    _, max_count = counter.most_common(1).pop()
#    if len(num_list) == 0 or len(set(counter.values())) == 1:
#        return []
#    return [num for num, count in counter.items() if count == max_count]

def calculate_mode(num_list):
#def calculate_mode(num_list: Sequence[int]) -> Sequence[int]:
    if not isinstance(num_list, Sequence):
        raise ValueError(
            f"Expected a sequence-type for num_list: '{type(num_list).__name__}' given."
        )
    if len(trivial_set := set(num_list)) <= 1:
        return list(trivial_set)
    counter = Counter(num_list)
    if len(counts := set(counter.values())) == 1:
        return []
    return [num for num, count in counter.items() if count == max(counts)]


# def calculate_mode(num_list):
#    counter = {num: num_list.count(num) for num in set(num_list)}
#    if len(counts := set(counter.values())) == 1:
#       return None
#    modes = [num for num, count in counter.items() if count == max(counts)]
#    return modes if len(modes) > 1 else modes.pop()


def main(num_list):
    if (modes := calculate_mode(num_list)) is None:
        print("No mode found!")
    else:
        print(modes)


def getmode(values: list) -> int:
    modes = {}
    highest = 0
    for x in values:
        if values.count(x) not in modes:
            modes[values.count(x)] = []

        modes[values.count(x)].append(x)
        if values.count(x) > highest:
            highest = values.count(x)

        values.pop(values.index(x))

    return modes[highest] if len(modes[highest]) > 1 else modes[highest][0]


"""
Some examples:

    >>> calculate_mode([10, 13, 5, 4, 17])
    No Mode Found!
    
    >>> calculate_mode([10, 13, 5, 4, 17, 17])
    17
    
    >>> calculate_mode([10, 13, 5, 4, 4, 17, 17])
    [4, 17]
    
    >>> main([10, 13, 5, 4, 17])
    No mode found!
    >>> main([10, 13, 5, 4, 17, 17])
    17
    >>> main([10, 13, 5, 4, 4, 17, 17])
    [4, 17]
    >>> 
    
"""
