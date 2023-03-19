def swap_names(fullname):
    return ', '.join(fullname.rsplit(maxsplit=1)[::-1])