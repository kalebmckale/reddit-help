def split(number_list, split_on_num=0):
    """
    split: Takes number_list and creates new split_list
    with sublists from number_list, split on split_on_num.
    """
    # Locate first index to split number_list
    try:
        split_index = number_list.index(split_on_num) + 1
    except ValueError:
        return [number_list]

    # Create split_list from left-hand sublist
    split_list = [number_list[:split_index]]

    # If right-hand sublist is non-empty, continue to split
    # sublist and extend split_list
    if (number_list := number_list[split_index:]):
        split_list.extend(split(number_list, split_on_num))
    return split_list

def split_str(string, num_partitions=1):
    """
    split_str: Takes a string and partitions into a list of
    num_partitions.
    """
    # check: number of partitions has to be positive integer
    if num_partitions < 1:
        raise ValueError('num_partitions must be positive integer')
    # check: cannot split string into more partitions than its length
    if num_partitions > (strlen := len(string)):
        raise ValueError(
            f'cannot partition a string of length {strlen} into'
            f' {num_partitions} partitions'
        )

    # Create partition
    partitions = [string[:(split_index := strlen // num_partitions)]]

    # Return if final partition
    if num_partitions == 1:
        return partitions
    
    # Split remainder and add to current partitions
    partitions.extend(split_str(string[split_index:], num_partitions - 1))
    return partitions