# Here's a (very) slightly faster method.

from collections import Counter
import itertools as it

def counter(od_list, upper_bound=0):
    nd = dict.fromkeys(range(max(upper_bound + 1, *od_list)), 0)
    nd.update(cntr := Counter(od_list), sum=cntr.total())
    return nd
    
original_dict = {'GC': [2,1,1], 'GA': [2,2], 'GG': [1], 'GU': [1]}
mydict = {k: counter(v, upper_bound=4) for k, v in original_dict.items()}
print(mydict)

# This won't have the keys with 0 value, but you'd still be able to access those keys.

