num_lists = [
    [1, 0, 22, 0, 7],
    [4, 0, 38, 0, 1],
    [22, 0, 15, 0, 2],
    # … and so on
]

num_lists_total = [total for num_list in zip(*num_lists) if (total := sum(num_list))]
