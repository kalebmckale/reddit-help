"""
I would recommend to shorten the code. Ex:

>>> macAddress

'2C:DB:07:16:9B:49'

>>> macAddress.split(':')

['2C', 'DB', '07', '16', '9B', '49']

>>> macAddress.split(':')[0] + macAddress.split(':')[1] + macAddress.split(':')[2] + macAddress.split(':')[3] + macAddress.split(':')[4] + macAddress.split(':')[5]

'2CDB07169B49'

>>> macAddress.replace(':', '')

'2CDB07169B49'
"""


macAddress = "2C:DB:07:16:9B:49"

# args = [iter(macAddress.replace(":",""))] * 4

# import itertools as it

# address = ".".join(
#    "".join(blk) for blk in it.zip_longest(*it.repeat(iter(macAddress.split(":")), 2))
# )

# print(other)
# import itertools as it
# from re import compile as createRegExPattern

# pattern = createRegExPattern(f"({':'.join(it.repeat('[0-9A-F]{2}', 2))})")
# address = ".".join(blk.replace(":", "") for blk in pattern.findall(macAddress))

from re import compile as createRegExPattern
pattern = createRegExPattern(":".join([f"([0-9A-F]{{2}})"] * 6))
address = pattern.sub(r"\1\2.\3\4.\5\6", macAddress)
# address = pattern.findall(macAddress)
print(address)
