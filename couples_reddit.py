def rotate(lst, n=1):
    if n:
        return [*lst[n:], *lst[:n]]
    return lst

def pairs(lst):
    return [tuple(rotate(lst, n=i)[:2]) for i in range(len(lst))]
            